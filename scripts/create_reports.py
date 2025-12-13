#!/usr/bin/env python3
"""
Script to create reports from crewai logs and JSON data.

Usage:
  python scripts/create_reports.py                    # Generate both usage and markdown reports (default)
  python scripts/create_reports.py --txt             # Generate only usage report
  python scripts/create_reports.py --md              # Generate only markdown report
  python scripts/create_reports.py [json_file]       # Create markdown report from specific JSON file

If no arguments provided, generates both reports from latest log and corresponding JSON files.
"""

import os
import glob
import re
import ast
import json
import sys
from datetime import datetime
from glob import glob as glob_glob


def unescape_newlines(text):
    """Unescape newline sequences like \\n, \\\\n, etc., to actual newlines."""
    if isinstance(text, str):
        return text.encode().decode('unicode_escape').encode('latin1').decode('utf-8')
    return text


def find_latest_log(directories=["logs"], prefix="crewai"):
    """Find the latest log file with the given prefix in the given directories."""
    all_files = []
    for directory in directories:
        pattern = os.path.join(directory, f"{prefix}*.log")
        files = glob_glob(pattern)
        all_files.extend(files)
    if not all_files:
        return None
    # Sort by modification time, latest first
    all_files.sort(key=os.path.getmtime, reverse=True)
    return all_files[0]


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


def extract_usage_report(log_content, log_file_path):
    """Extract usage records and generate ASCII report."""
    usage_records = []
    lines = log_content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        parts = line.split(' - ', 3)
        if len(parts) < 4:
            i += 1
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
                    # Look for the next TASK DONE JSON entry to get agent info
                    agent = "Unknown"
                    for j in range(i + 1, min(i + 50, len(lines))):  # Look up to 50 lines ahead
                        next_line = lines[j]
                        if '[TASK DONE JSON]' in next_line:
                            # Extract the JSON starting from this line
                            json_lines = []
                            # Find the start of JSON
                            json_start = next_line.find('{')
                            if json_start != -1:
                                json_lines.append(next_line[json_start:])
                                # Continue reading lines until we have complete JSON
                                brace_count = next_line[json_start:].count('{') - next_line[json_start:].count('}')
                                k = j + 1
                                while k < len(lines) and brace_count > 0:
                                    json_lines.append(lines[k])
                                    brace_count += lines[k].count('{') - lines[k].count('}')
                                    k += 1
                                try:
                                    json_str = '\n'.join(json_lines)
                                    json_data = json.loads(json_str)
                                    agent_type = json_data.get('type', 'Unknown')
                                    # Convert model types to agent names
                                    agent_map = {
                                        'muse_model': 'Muse',
                                        'gardener_model': 'Gardener',
                                        'poet_model': 'Poet',
                                        'psychologist_model': 'Psychologist',
                                        'architect_model': 'Architect',
                                        'editor_model': 'Editor',
                                        'critic_model': 'Critic',
                                        'publisher_model': 'Publisher'
                                    }
                                    agent = agent_map.get(agent_type, agent_type.replace('_model', '').title())
                                    break
                                except (json.JSONDecodeError, KeyError):
                                    pass
                            break

                    usage_records.append({
                        'timestamp': timestamp,
                        'usage': usage_dict,
                        'agent': agent
                    })
                except (ValueError, SyntaxError):
                    pass  # Skip invalid
        i += 1

    # Generate the ASCII report
    report_lines = []
    report_lines.append("Token Usage Report")
    report_lines.append("=" * 100)
    report_lines.append(f"{'Timestamp':<20} {'Agent':<12} {'Prompt Tokens':<15} {'Completion Tokens':<18} {'Total Tokens':<15}")
    report_lines.append("-" * 100)

    total_prompt = 0
    total_completion = 0
    total_tokens = 0

    for usage in usage_records:
        prompt = usage['usage'].get('prompt_tokens', 0)
        completion = usage['usage'].get('completion_tokens', 0)
        total = usage['usage'].get('total_tokens', 0)
        agent = usage.get('agent', 'Unknown')
        report_lines.append(f"{usage['timestamp']:<20} {agent:<12} {prompt:<15} {completion:<18} {total:<15}")
        total_prompt += prompt
        total_completion += completion
        total_tokens += total

    report_lines.append("-" * 100)
    report_lines.append(f"{'TOTALS':<20} {'':<12} {total_prompt:<15} {total_completion:<18} {total_tokens:<15}")
    report_lines.append("=" * 100)

    return "\n".join(report_lines)


def get_most_recent_json_in_logs():
    """Get the most recent .json file in the logs directory."""
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        print(f"Error: Logs directory '{logs_dir}' does not exist.")
        sys.exit(1)

    json_files = glob_glob(os.path.join(logs_dir, '*.json'))
    if not json_files:
        print(f"Error: No .json files found in '{logs_dir}'.")
        sys.exit(1)

    # Sort by modification time, most recent first
    json_files.sort(key=os.path.getmtime, reverse=True)
    return json_files[0]


def create_markdown_report(json_file_path):
    """Create a markdown report from JSON data."""
    if not os.path.exists(json_file_path):
        print(f"Error: File {json_file_path} does not exist.")
        sys.exit(1)

    # Load JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Determine output path
    base_name = os.path.splitext(json_file_path)[0]
    md_file_path = base_name + '.md'

    # Open output file
    with open(md_file_path, 'w') as md_file:
        md_file.write(f"# CrewAI Execution Report\n\n")
        md_file.write(f"Generated from: {json_file_path}\n\n")

        # Iterate through the JSON objects
        for item in data:
            item_type = item.get('type')
            if item_type == 'muse_model':
                concepts = item.get('concepts', [])
                md_file.write("## Muse Concepts\n\n")
                for concept in concepts:
                    text = unescape_newlines(concept.get('text', ''))
                    md_file.write(f"- {text}\n")
                md_file.write("\n")
            elif item_type == 'gardener_model':
                seeds = item.get('seeds', [])
                md_file.write("## Gardener Seeds\n\n")
                for seed in seeds:
                    md_file.write(f"- {seed.get('text', '')}\n")
                md_file.write("\n")
            elif item_type == 'poet_model':
                seed = item.get('seed')
                poem = item.get('poem')
                if poem and poem.get('version'):
                    md_file.write(f"## Poem (Version {poem.get('version')})\n\n")
                else:
                    md_file.write("## Poem\n\n")
                if seed and seed.get('text'):
                    text = unescape_newlines(seed['text'])
                    md_file.write(f"**Seed:** {text}\n\n")
                if poem and poem.get('text'):
                    text = unescape_newlines(poem['text'])
                    md_file.write("```markdown\n")
                    md_file.write(text)
                    md_file.write("\n```\n\n")
            elif item_type == 'architect_model':
                architect_notes = item.get('architect_notes', {})
                poem = item.get('poem')
                md_file.write("## Architect Notes\n\n")
                bullets = architect_notes.get('bullets', [])
                for note in bullets:
                    md_file.write(f"- {note}\n")
                md_file.write("\n")
                if poem and poem.get('text'):
                    text = unescape_newlines(poem['text'])
                    md_file.write("```markdown\n")
                    md_file.write(text)
                    md_file.write("\n```\n\n")
            elif item_type == 'editor_model':
                editor_notes = item.get('editor_notes', {})
                md_file.write("## Editor Notes\n\n")
                bullets = editor_notes.get('bullets', [])
                for note in bullets:
                    md_file.write(f"- {note}\n")
                md_file.write("\n")
            elif item_type == 'critic_model':
                review = item.get('review', {})
                md_file.write(f"## {review.get('title', 'Review')}\n\n")
                body = unescape_newlines(review.get('body', ''))
                md_file.write(f"{body}\n\n")
            elif item_type == 'publisher_model':
                file_path = item.get('file_path', '')
                md_file.write(f"## Published File\n\n{file_path}\n\n")

    print(f"Markdown report generated: {md_file_path}")
    return md_file_path


def process_logs():
    """Process log files to generate usage report."""
    log_file = find_latest_log()
    if not log_file:
        print("No log file found.")
        return None

    print(f"Processing log file: {log_file}")

    # Read the log file once
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()

    # Calculate and print runtime
    runtime = calculate_runtime(log_content)
    print(f"Runtime: {runtime}")

    # Extract usage report and save to .txt
    usage_report = extract_usage_report(log_content, log_file)
    log_basename = os.path.basename(log_file)
    txt_output_file = os.path.join(os.path.dirname(log_file), log_basename.replace('.log', '.txt'))
    with open(txt_output_file, 'w') as f:
        f.write(usage_report)
    print(f"Saved usage report to {txt_output_file}")
    return txt_output_file


def main():
    if len(sys.argv) == 1:
        # Default: do both reports
        usage_file = process_logs()
        if usage_file:
            # Try to find corresponding JSON file
            json_file = usage_file.replace('.txt', '.json')
            if os.path.exists(json_file):
                create_markdown_report(json_file)
            else:
                print("No corresponding JSON file found for markdown report.")
    elif len(sys.argv) == 2:
        if sys.argv[1] == '--txt':
            # Generate only usage report
            process_logs()
        elif sys.argv[1] == '--md':
            # Generate only markdown report
            json_file = get_most_recent_json_in_logs()
            print(f"Using most recent JSON file: {json_file}")
            create_markdown_report(json_file)
        else:
            # Assume it's a JSON file path
            json_file = sys.argv[1]
            create_markdown_report(json_file)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()