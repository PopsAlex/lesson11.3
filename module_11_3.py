from pprint import pprint
import requests


class Introspectoin:
    _dict = {}

    def __init__(self, obj):
        global _dict
        self.obj = obj

    def introspection_info(self):
        self._type()
        self.att()
        self.met()
        self.mod()
        return self._dict

    def _type(self):
        self._dict['type'] = type(self.obj)

    def att(self):
        self._dict['attributes'] = list(set(dir(self.obj)) - set(dir(type(self.obj))))

    def met(self):
        self._dict['methods'] = dir(self.obj)

    def mod(self):
        try:
            self._dict['module'] = self.obj.__module__
        except AttributeError:
            self._dict['module'] = __name__  # или __file__? не совсем понял, о каком модуле речь


intro = Introspectoin(42)
pprint(intro.introspection_info())
