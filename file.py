import os

# exists(), isfile(), isdir()

dname="Fol"

if os.path.exists(dname):
    print("Already exists")
else:
    os.mkdir(dname) #remove,rmdir

fname=open("Fol//file.txt","w")

print("Please type in data, to stop just press enter.")
with fname as file:
    ch=""
    while True:
        ch=input()
        if ch=='':
            break
        file.write(ch+'\n')

fname=open("Fol//file.txt")
with fname as file:
    out=file.read()
print(out)


    

