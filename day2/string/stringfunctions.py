firstName="Mugesh "
lastName="Siva "
concat=firstName+lastName
print(f"{concat}")
print(len(concat))
print(concat.lower())
print(concat.upper())
print(len(concat.strip()))

#split syntax ## string.split(separator, maxsplit)
print(concat.lower().split("s",1))


#replace
concat=concat.replace("h","M")
print(concat)

#find
print(concat.find("S"))

#Max and Min
#space has the lowest   ASCII VALUE of all the values
print(max(concat))
print(min(concat))