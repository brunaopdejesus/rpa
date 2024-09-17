f = open("demofile2.txt", "a")
f.write("AAAAAA")
f.close()

f = open("demofile2.txt", "r")
print(f.read())