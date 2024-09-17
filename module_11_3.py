import time
import inspect


class Faculty:
    def __init__(self, faculty_name, number_students, average_mark):
        self.faculty_name = faculty_name
        self.number_students = number_students
        self.average_mark = average_mark

    def faculty_rating(self):
        rez = {self.faculty_name: self.number_students * self.average_mark}
        return rez


def introspection_info(obj):
    spin_info = {}
    attrs = []
    meths = []
    # print(type(obj).__name__)
    for atr in dir(obj):
        if callable(getattr(obj, atr)):
            meths.append(atr)
            # print(atr)
        else:
            attrs.append(atr)

    try:
        mod = inspect.getmodule(obj).__name__
    except:
        mod = '__main__'

    spin_info['type'] = type(obj).__name__
    spin_info['attributes'] = attrs
    spin_info['methods'] = meths
    spin_info['module'] = mod
    return spin_info


e = 22.4
print(f'Характеристики вещественного числа {e}.')
print(introspection_info(e))
print()
k = (3, 'r')
print(f'Характеристики {k}.')
print(introspection_info(k))
print()
l = ['f', 'r']
print(f'Характеристики {l}.')
print(introspection_info(l))
print()
print(f'Характеристики функции print().')
print(introspection_info(print))
print()
print(f'Характеристики класса object.')
print(introspection_info(object))
print()
print(f'Характеристики модуля time.')
print(introspection_info(time))
print()
print(f'Характеристики функции time.sleep().')
print(introspection_info(time.sleep))
print()
facultet_1 = Faculty('physics', 211, 4.3)
print(f'Характеристики экземпляра facultet_1 {facultet_1}.')
print(introspection_info(facultet_1))
print()
print(f'Характеристики класса {Faculty}.')
print(introspection_info(Faculty))
