def introspection_info(obj):
    _dict = {}
    _dict['type'] = type(obj).__name__
    _list_atr = []
    _list_met = []
    for i in dir(obj):
        if callable(getattr(obj, i)):
            _list_met.append(i)
        if not callable(getattr(obj, i)):
            _list_atr.append(i)
    _dict['attributes'] = _list_atr
    _dict['methods'] = _list_met
    try:
        _dict['module'] = obj.__module__
    except AttributeError:
        _dict['module'] = __name__
    return _dict


number_info = introspection_info(42)
print(number_info)

