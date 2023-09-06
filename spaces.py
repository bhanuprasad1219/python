def string_(n):
    count = 0
    for i in n:
        if i == " ":
            count += 1
    return count
print(string_("bhanu kn af "))
print(string_(""))

