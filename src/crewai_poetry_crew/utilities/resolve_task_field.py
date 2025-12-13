def resolve_task_field(config: dict, key: str, task_name: str) -> str:
    """
    config[key] can be:
        - a scalar/block (applies to all tasks), or
        - a dict of {task_name: value, "default": value}.
    """
    value = config[key]

    if not isinstance(value, dict):
        return value

    if task_name in value:
        return value[task_name]

    if "default" in value:
        return value["default"]

    raise KeyError(f"No value for {key!r} in task {task_name!r} and no default")
