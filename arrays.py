list= [1,2,3,4,5]

print(list)
print(list[0])

len_list = len(list)
print(len_list)

list_2 = ['M.Talha', 24, True, 2001, 5.6]
print(list_2)
print(list_2[0])

full_lit = list + list_2
print(full_lit)

list_2.append('Çorbacı')
print(list_2)
list_2.insert(0,'Hello')
print(list_2)

double_list = list_2 * 2
print(double_list)

object_count = double_list.count('M.Talha')
print(object_count)

list_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2d)
print(list_2d[0])
print(list_2d[0][1])

number_list = [5,2,9,1,7]
number_list.sort()
print(number_list)
number_list.reverse()
print(number_list)
number_list.clear()
print(number_list)
it_gonna_append =  ['asdasd' , 123123   , True]
number_list.append(it_gonna_append)
print(number_list)
print(len(number_list))
number_list.extend([7,8,9])
print(number_list)
print(number_list.index(8))
number_list[0].remove(123123)
print(number_list)
number_list.pop()
print(number_list)

#