# bir stringi biçimlendirmek için kullanılan yöntemler
name = "M.talha"
surname = "Çorbacı"

print("Benim adım " + name + " ve soyadım " + surname)
#yukarıdaki normal kullanım

# format method
print("Benim adım {} ve soyadım {}" . format(name , surname))

print("Benim adım {0} ve soyadım {1}" . format(name , surname))

print("Benim adım {1} ve soyadım {0}" . format(surname , name))

#f-strings
print(f"Benim adım {name} ve soyadım {surname}")

print(f"Benim adım {name.upper()} ve soyadım {surname.lower()}")