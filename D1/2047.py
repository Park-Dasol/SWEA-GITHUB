letter = 0 
L = input()
result = ''
for l in L:
    if 97 <= ord(l) <= 122:
     
        letter = ord(l) - 32
        result += chr(letter)
    else: 
        result += l
 
print(result)