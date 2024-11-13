input_string = input('Masukkan sebuah string: ')
jumlah_kapital = 0
for karakter in input_string:
    if 65 <= ord(karakter) <= 90:
        jumlah_kapital += 1
print('Jumlah huruf kapital adalah ', jumlah_kapital)