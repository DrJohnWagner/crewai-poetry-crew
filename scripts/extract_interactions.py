import re
import json

def extract_agent_interactions(log_file_path):
    with open(log_file_path, 'r', encoding='utf-8') as f:
        log_content = f.read()

    # Pattern to find agent started sections
    agent_started_pattern = r'Agent:\s*(.*?)\s*\n.*?\n│\s*Task:\s*([\s\S]*?)\s*│\s*\n╰'
    
    # Pattern to find final answers
    final_answer_pattern = r'Agent:\s*(.*?)\s*\n.*?\n│\s*Final Answer:\s*([\s\S]*?)\s*│\s*\n╰'

    # Find all agent started
    agent_starts = re.findall(agent_started_pattern, log_content, re.DOTALL)
    print(f"Agent starts: {len(agent_starts)}")
    
    # Debug
    agent_started_debug = re.findall(r'Agent:\s*(.*?)\s*\n.*?\n│\s*Task:', log_content, re.DOTALL)
    print(f"Agent started debug: {len(agent_started_debug)}")
    
    tasks = re.findall(r'│\s*Task:\s*(.*?)\s*│\s*\n╰', log_content, re.DOTALL)
    print(f"Tasks found: {len(tasks)}")
    
    final_answers_debug = re.findall(r'│\s*Final Answer:\s*(.*?)\s*│\s*\n╰', log_content, re.DOTALL)
    print(f"Final answers debug: {len(final_answers_debug)}")
    
    # Find all final answers
    final_answers = re.findall(final_answer_pattern, log_content, re.DOTALL)
    print(f"Final answers: {len(final_answers)}")

    interactions = []
    min_len = min(len(agent_starts), len(final_answers))
    
    for i in range(min_len):
        agent_name, task = agent_starts[i]
        agent_name_fa, answer = final_answers[i]
        if agent_name.strip() == agent_name_fa.strip():
            interactions.append({
                'agent': agent_name.strip(),
                'input': task.strip(),
                'output': answer.strip()
            })

    return interactions

if __name__ == "__main__":
    log_file = 'log.txt'
    interactions = extract_agent_interactions(log_file)
    
    # Print as JSON
    print(json.dumps(interactions, indent=4))
    
    # Optionally, save to file
    with open('agent_interactions.json', 'w') as f:
        json.dump(interactions, f, indent=4)