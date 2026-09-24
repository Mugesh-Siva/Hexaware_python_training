file=open("./day4/file_handeling/exployee.txt","r")

print("curser is here", file.tell())
file.seek(5)
print("curser is here now", file.tell())
data=file.read()
print(data)
file.close()
