class InvalidTemplate(Exception):
    """Template folder don't have required files"""
    pass


class LabelWithoutValue(Exception):
    """Value is not provided for a template label"""
    pass
