from copy import copy


class Blub:
    index = 1


a = Blub()
b = Blub()

lista = [a, b]
listb = copy(lista)

print([1, 2, 3, 4][-1])
