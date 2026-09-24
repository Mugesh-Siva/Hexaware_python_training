file=open("./day4/file_handeling/employee_system.txt","w")
file.write("Hello world\nHi everyone\nHow are you")
file.close()
with open("./day4/file_handeling/employee_system.txt","r") as file_read:
    
    print("The curser in",file_read.tell())
    print("The Line: ", file_read.readline())
    file_read.seek(0)
    print("The Lines: ",file_read.readlines())
    file_read.seek(2)
    print(file_read.tell())
    