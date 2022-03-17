def get_child_instance(obj, cls):
    for child_class in cls.__subclasses__():
        property_name = child_class.__name__.lower()
        child = getattr(obj, property_name, None)
        if child is not None:
            if len(child_class.__subclasses__()) > 0:
                return get_child_instance(child, child_class)
            else:
                return child