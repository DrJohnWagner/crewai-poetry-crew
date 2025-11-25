import os
import glob
import json
import re
import ast
from datetime import datetime

def find_latest_log(directories=["logs"], prefix="crewai"):
    """Find the latest log file with the given prefix in the given directories."""
    all_files = []
    for directory in directories:
        pattern = os.path.join(directory, f"{prefix}*.log")
        files = glob.glob(pattern)
        all_files.extend(files)
    if not all_files:
        return None
    # Sort by modification time, latest first
    all_files.sort(key=os.path.getmtime, reverse=True)
    return all_files[0]

def extract_request_options(log_content, log_file_path):
    """Extract request options from the log content."""
    request_options = []
    lines = log_content.splitlines()
    for line in lines:
        if "Request options:" in line:
            # Extract timestamp and request options
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (.+)', line)
            if match:
                timestamp = match.group(1)
                options_str = line.split("Request options:", 1)[1].strip()
                try:
                    options = ast.literal_eval(options_str)
                    request_options.append({
                        "timestamp": timestamp,
                        "request_options": options
                    })
                except (ValueError, SyntaxError):
                    pass  # Skip invalid
    return request_options

def calculate_runtime(log_content):
    """Calculate the runtime from the first to last timestamp in the log."""
    lines = log_content.splitlines()
    first_timestamp = None
    last_timestamp = None
    for line in lines:
        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})', line)
        if match:
            timestamp_str = match.group(1)
            if first_timestamp is None:
                first_timestamp = timestamp_str
            last_timestamp = timestamp_str
    if first_timestamp and last_timestamp:
        first_dt = datetime.strptime(first_timestamp, '%Y-%m-%d %H:%M:%S,%f')
        last_dt = datetime.strptime(last_timestamp, '%Y-%m-%d %H:%M:%S,%f')
        delta = last_dt - first_dt
        return str(delta)
    return "Unable to calculate runtime"

def extract_usage_report(log_content, log_file_path, request_options):
    """Extract usage records and generate ASCII report with agent info."""
    usage_records = []
    lines = log_content.splitlines()
    for line in lines:
        parts = line.split(' - ', 3)
        if len(parts) < 4:
            continue
        timestamp = parts[0]
        logger = parts[1]
        level = parts[2]
        message = parts[3]
        
        if level == 'INFO' and 'OpenAI API usage:' in message:
            if 'OpenAI API usage:' in message:
                usage_str = message.split('OpenAI API usage:', 1)[1].strip()
                usage_str = usage_str.strip(' .,')
                try:
                    usage_dict = ast.literal_eval(usage_str)
                    usage_records.append({
                        'timestamp': timestamp,
                        'usage': usage_dict
                    })
                except (ValueError, SyntaxError):
                    pass  # Skip invalid
    
    # Function to extract agent from system prompt
    def get_agent_from_request(request):
        messages = request.get('request_options', {}).get('json_data', {}).get('messages', [])
        for msg in messages:
            if msg.get('role') == 'system':
                content = msg.get('content', '')
                if content.startswith('You are '):
                    # Extract agent name
                    line = content.split('\n', 1)[0]  # First line
                    agent_full = line.replace('You are ', '').split('.')[0].strip()
                    # Shorten to key name
                    if 'Muse' in agent_full:
                        return 'Muse'
                    elif 'Summariser' in agent_full:
                        return 'Summariser'
                    elif 'Editor' in agent_full:
                        return 'Editor'
                    elif 'Poet' in agent_full:
                        return 'Poet'
                    elif 'Architect' in agent_full or 'breath' in agent_full.lower():
                        return 'Architect'
                    elif 'Critic' in agent_full:
                        return 'Critic'
                    elif 'Publisher' in agent_full:
                        return 'Publisher'
                    else:
                        return agent_full[:12]  # Truncate if long
        return '<UNKNOWN>'
    
    # Match usage to request options by timestamp
    usage_with_agent = []
    req_sorted = sorted(request_options, key=lambda x: x['timestamp'])
    for usage in usage_records:
        usage_time = datetime.strptime(usage['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
        # Find the closest request in time
        agent = '<UNKNOWN>'
        min_diff = float('inf')
        for req in req_sorted:
            req_time = datetime.strptime(req['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
            diff = abs((usage_time - req_time).total_seconds())
            if diff < min_diff:
                min_diff = diff
                agent = get_agent_from_request(req)
        usage['agent'] = agent
        usage_with_agent.append(usage)
    
    # Generate the ASCII report
    report_lines = []
    report_lines.append("Token Usage Report")
    report_lines.append("=" * 80)
    report_lines.append(f"{'Timestamp':<20} {'Prompt Tokens':<15} {'Completion Tokens':<18} {'Total Tokens':<15} {'Agent':<12}")
    report_lines.append("-" * 80)
    
    total_prompt = 0
    total_completion = 0
    total_tokens = 0
    
    for usage in usage_with_agent:
        prompt = usage['usage'].get('prompt_tokens', 0)
        completion = usage['usage'].get('completion_tokens', 0)
        total = usage['usage'].get('total_tokens', 0)
        agent = usage['agent']
        report_lines.append(f"{usage['timestamp']:<20} {prompt:<15} {completion:<18} {total:<15} {agent:<12}")
        total_prompt += prompt
        total_completion += completion
        total_tokens += total
    
    report_lines.append("-" * 80)
    report_lines.append(f"{'TOTALS':<20} {total_prompt:<15} {total_completion:<18} {total_tokens:<15} {'':<12}")
    report_lines.append("=" * 80)
    
    return "\n".join(report_lines)

if __name__ == "__main__":
    log_file = find_latest_log()
    if not log_file:
        print("No log file found.")
        exit(1)
    
    print(f"Processing log file: {log_file}")
    
    # Read the log file once
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
    
    # Calculate and print runtime
    runtime = calculate_runtime(log_content)
    print(f"Runtime: {runtime}")
    
    # Extract request options and save to .json
    request_options = extract_request_options(log_content, log_file)
    log_basename = os.path.basename(log_file)
    json_output_file = os.path.join(os.path.dirname(log_file), log_basename.replace('.log', '.json'))
    with open(json_output_file, 'w') as f:
        json.dump(request_options, f, indent=4)
    print(f"Saved request options to {json_output_file}")
    
    # Extract usage report and save to .txt
    usage_report = extract_usage_report(log_content, log_file, request_options)
    txt_output_file = os.path.join(os.path.dirname(log_file), log_basename.replace('.log', '.txt'))
    with open(txt_output_file, 'w') as f:
        f.write(usage_report)
    print(f"Saved usage report to {txt_output_file}")