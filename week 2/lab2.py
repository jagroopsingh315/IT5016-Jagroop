"""author : jagroop"""
name = "jagroop"
extra = 3

name_length =len(name)
stars_length = name_length + extra *2

print("*"*stars_length)
print(""*extra + name + ""*extra)
print("*"*stars_length)