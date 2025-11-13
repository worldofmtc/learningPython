#array ile farkı şu ki tuple değiştirilemez (immutable)

list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)    

print(list1)
print(tuple1)
print(type(list1))
print(type(tuple1))

print(tuple1[0])

tuple[0] = 10  # hata verir çünkü tuple değiştirilemez
print(tuple1)   