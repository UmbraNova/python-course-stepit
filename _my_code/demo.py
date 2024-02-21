f = open("_my_code/demofile.txt", "r+")

# print(f.readlines())

x = f.readlines()

print(x[-1])

f.close()