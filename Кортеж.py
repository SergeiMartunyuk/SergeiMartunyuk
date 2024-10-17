immutable_var = ('chair', 123, True, 'table')
print(immutable_var)
# immutable_var[0] = 'armchair' - при изменении элемента выводится ошибка кортежа, он не изменяем.

mutable_list = ['name', 'size', 'quantity']
print(mutable_list)
mutable_list[2] = 'organization'
print(mutable_list)