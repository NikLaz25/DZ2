line1 = (input('введите несколько слов через пробел: '))
line2 = line1.split( )
print(line2)
for el, line2 in enumerate(line2):
    print(el+1, line2[:10])

#for el in line2:
 #   for n in enumerate(line2):
 #       n2 = n + 1
   #     print(n2, el[:10])