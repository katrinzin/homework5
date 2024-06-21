immutable_var = (1, 3, 5, True, 'run', [10, 9, 8])
print('immutable_var:', immutable_var)
# immutable_var[0] = 2
# невозможно изменить элемент в кортеже, т.к. это неизменяемая величина.
# можно изменить только список в [] скобках
mutable_list = [2, 4, 6, 'stop']
print('mutable_list:', mutable_list)
mutable_list[3] = 'hello'
print('mutable_list new:', mutable_list)

