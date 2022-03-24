import uuid


def generate_code(model, uid_field="uid", max_len=8):
    """
    Generate a unique code for model instance

    :model: Model
    :uid_fields: Character set to choose from
    :max_len: Max length default 8
    """
    code = str(uuid.uuid4())[:max_len]
    # Ensure code does not aleady exist
    try:
        kwargs = {uid_field: code}
        model.objects.get(**kwargs)
    except model.DoesNotExist:
        return code
    return generate_code(model, uid_field, max_len)
