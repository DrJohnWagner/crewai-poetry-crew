from pydantic import BaseModel

# Returns: ["type", "title", "text", "version"]
def model_field_names(model_cls: type[BaseModel]) -> list[str]:
    return list(model_cls.model_fields.keys())

# Returns: Poem (type, title, text, version).
def generate_object_definition(model_cls: type[BaseModel]) -> str:
    fields = ", ".join(model_field_names(model_cls))
    return f"{model_cls.__name__.removesuffix("Model")} ({fields})"

# Returns: PoemModel = JSON with fields: type, title, text, version.
def generate_model_definition(model_cls: type[BaseModel]) -> str:
    fields = ", ".join(model_field_names(model_cls))
    return f"{model_cls.__name__} = JSON with fields: {fields}."

# Returns: PoemModel = JSON with fields: type, title, text, version.
def generate_model_fields(model_cls: type[BaseModel]) -> str:
    return "".join([
        "- " + field + "\n"
        for field in model_cls.model_fields.keys()
        if field != "type"
    ])
