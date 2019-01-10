path_input = r'F:\Google Drive\Other Documents\Encrypted Passkey.txt'
file_input = open(path_input,"r")
str = file_input.read()
char_list = [ord(c) for c in str]
new_list = []
for c in char_list:
    if(c==10):
        new_list.append(c)
    else:
        new_list.append(c-3)
new_char_list = [chr(c) for c in new_list]
new_char_str = ''.join(new_char_list)
print(new_char_str)