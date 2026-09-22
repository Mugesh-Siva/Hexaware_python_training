def grade(mark):
    if mark>100 or mark<0:
        print("Not Valid")
    elif mark>=90:
        print("Excellent")
    elif mark>=75:
        print("Good")
    elif mark>=50:
        print("Needs Improvement")
    else :
        print("poor")
grade(-1)
