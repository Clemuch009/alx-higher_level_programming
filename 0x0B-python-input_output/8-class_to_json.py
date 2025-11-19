def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
       obj: instance of a Class with serializable attributes
    
    """
    return obj.__dict__
