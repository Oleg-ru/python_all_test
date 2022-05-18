name = "Milk in my learn capacity"

#print(name.upper())
#print(name.replace('a', 'o'))
print(name.__len__())
print(len(name))

print(name == "carava1")

print("my " not in name)
print("__________________")

comment = """Hello my
dear
men
kiss my"""
print(comment)
print("__________________")
email = """
Hello my dear {}
Welcome my course
I gift you my {} a new study"""
name = "Oleg"

print(email.format(name, name))

name = "Ne Name"
if "{}" in email:
    print("true")
    email.replace("{}", name)
print(email)

email = f"""
Hello my dear {name}
Welcome my course
I gift you my {name} a new study"""
print(email)
