f = open("demofile3.txt", "w")
f.write("substituir ")
f.close()

f = open("demofile3.txt", "r")
print(f.read())