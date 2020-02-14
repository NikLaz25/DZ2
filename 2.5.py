my_list = [9,7,6,5,2]
value = int(input('введите значения для определения рейтинга: '))
for el, n in enumerate(my_list):
    if value <= my_list[el]:
        continue
    my_list.insert(el, value)
    print(my_list)
    break
print(my_list[1])