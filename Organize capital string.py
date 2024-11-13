input_string = input('Masukkan sebuah kalimat: ')
char_list = list(input_string)

if 'a' <= char_list[0] <= 'z':
    char_list[0] = chr(ord(char_list[0]) - 32) 
for i in range(1, len(char_list)):
    if 'A' <= char_list[i] <= 'Z':
        char_list[i] = chr(ord(char_list[i]) + 32)  

output_string = ''.join(char_list)
print(output_string)