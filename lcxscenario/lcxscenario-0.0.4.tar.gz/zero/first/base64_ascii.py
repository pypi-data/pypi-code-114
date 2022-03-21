import base64

miwen = '4nXna/V7t2LpdLI44mn0fQ=='
mingwen = base64.b64decode(miwen)
print(mingwen)

for i in mingwen:
    # print(type(i))
    print(i, end=" ")

print()
j = 1
for i in mingwen:
    # print(type(i))

    if(j % 2 == 1):
        print(chr(i-128), end="")
    else:
        print(chr(i), end="")
    j += 1
