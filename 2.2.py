list1 = list(input('Введите список из n элементов: '))
print (list1)
for n in range(1, len(list1),2):  # на занятии range небыло. В методичке есть, но только в теме bytearrey, где непонятно что к чему.
    list1[n - 1], list1[n] = list1[n], list1[n - 1] # в итоге подсмотрел по видео
print(list1)
#for n in range(0, len(list1),2):
#    list1[n], list1[n+1] = list1[n+1], list1[n]

#print(list1[2][1])
#print(list1)
#list1[0], list1[1] = list1[1], list1[0]

#list.reverse((1, 2) == (2, 1))
#print (list)

#list2 = ((el[1], el[0]) for el in list)
#list2.next()
#print (list2)

#print (list)



#g = ((t[1], t[0]) for t in mylist)
#g.next()

#list[1], list[0] = list[0], list[1]