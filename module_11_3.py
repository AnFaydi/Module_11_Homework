from inspect import getmodule, getmodulename
from pprint import pprint

class WorkWithObj:
    def __init__(self, obj):
        self.obj = obj
    def introspection_info(self):
        return {'Тип объекта': type(self.obj), 'Атрибуты и методы объекта': dir(self.obj),
                'Модуль, которому принадлежит:': getmodule(self)}

my_list = WorkWithObj(42)
pprint(my_list.introspection_info())
