import yaml
from pathlib import Path
from crewai_poetry_crew.config.templates import AGENT_TEMPLATE, TASK_TEMPLATE
from crewai_poetry_crew.utilities.globals import GLOBALS
# from crewai_poetry_crew.utilities.save_to_file import save_to_file

def flatten_dictionary(dictionary: dict, task: str) -> dict:
    result = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            # Logic to handle comma-separated keys in the YAML
            found = False
            for k, v in value.items():
                # Split "task_a, task_b" into ["task_a", "task_b"]
                if task in [s.strip() for s in k.split(',')]:
                    result[key] = v
                    found = True
            # Fallback to default if no specific task match found
            if not found and "default" in value:
                result[key] = value["default"] 
            #
            # if task in [k.strip() for k in value.split(",")]:
            #     result[key] = value[task]
            # elif "default" in value:
            #     result[key] = value["default"]                
        else:
            result[key] = value
    return result

def apply_substitutions(data: dict, subs: dict) -> dict:
    result = {}
    for key, value in data.items():
        if isinstance(value, str):
            # Direct string substitution: {FOO} → subs["FOO"]
            result[key] = value.format(**subs)
        elif isinstance(value, dict):
            # Recurse into nested dicts
            result[key] = apply_substitutions(value, subs)
        elif isinstance(value, list):
            # Recurse into lists
            new_list = []
            for item in value:
                if isinstance(item, str):
                    new_list.append(item.format(**subs))
                elif isinstance(item, dict):
                    new_list.append(apply_substitutions(item, subs))
                else:
                    new_list.append(item)
            result[key] = new_list
        else:
            # Scalars (int, float, None) pass through unchanged
            result[key] = value
    return result

# agent | task, Muse | Gardener | etc
def load_dictionary(actor: str, discard: str) -> dict[str, any]:
    dictionary = {}
    filename = Path("src", "crewai_poetry_crew", "config", actor + ".yaml")
    with open(filename, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        dictionary.update({
            key: value for key, value in data[actor].items()
        })
    substitute = GLOBALS | dictionary
    dictionary = {
        key: value
        for key, value in dictionary.items()
        if not key.startswith(discard)
    }
    dictionary = apply_substitutions(dictionary, substitute)
    # save_to_file(
    #     str(dictionary) + "\n" +
    #     str(substitute) + "\n" +
    #     AGENT_TEMPLATE + "\n" +
    #     TASK_TEMPLATE,
    #     f"dictionaries.py"
    # )
    return {
        key.upper().replace("-", "_"): value
        for key, value in dictionary.items()
    }
    
def load_agent_template(actor: str) -> dict[str, any]:
    dictionary = load_dictionary(actor, "task-")
    template = "\n".join(
        line for line in AGENT_TEMPLATE.splitlines()
        if not line.strip().startswith("#")
    )
    return {
        "actor": actor,
        "role": dictionary.get("AGENT_ROLE", ""),
        "goal": dictionary.get("AGENT_GOAL", ""),
        "backstory": template.format(**dictionary),
    }

def load_task_template(actor: str, task: str) -> dict[str, any]:
    dictionary = load_dictionary(actor, "agent-")
    dictionary = flatten_dictionary(dictionary, task)
    template = "\n".join(
        line for line in TASK_TEMPLATE.splitlines()
        if not line.strip().startswith("#")
    )
    return {
        "actor": actor,
        "task": task,
        "description": template.format(**dictionary),
    }
