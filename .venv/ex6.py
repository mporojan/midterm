my_list = [1, 2, 3]
my_list[0] = 10
my_list.append(4)

print(my_list)

s = "hello"

s[0] = "H" # will give error

s2 = "H" + s[1:]
print(s2)