import os

def input_editor():
    space = '\n'
    differentiator = " : "
    inp = input("Enter Website:- ")
    file_raw.write(space+inp + space)
    inp = input("Enter Email:- ")
    file_raw.write(inp + differentiator)
    inp = input("Enter Password:- ")
    file_raw.write(inp + space+space)


path_raw = r'D:\Projects\PycharmProjects\CryptoGun\Generator.txt'
path_output = r'D:\Projects\PycharmProjects\CryptoGun\Encrypted Passkey.txt'
file_raw = open(path_raw, "w")
file_output = open(path_output,"a+")
looper = input("Enter input (Y/N):- ")
while(looper.lower() == 'y'):
    input_editor()
    looper = input("Enter Again (Y/N):- ")
file_raw.seek(0,0)
str_list = [ c for c in file_raw.read()]
char_list = [ord(c) for c in str_list]
new_list = []
for c in char_list:
    if c == 10 :
        new_list.append(c)
    else:
        new_list.append(c+3)
new_char = [chr(c) for c in new_list]
new_char_string = ''.join(new_char)
file_output.write(new_char_string)
file_raw.close()
os.remove(path_raw)
file_output.close()