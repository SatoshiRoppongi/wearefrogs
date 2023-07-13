import re

with open('numbers.txt') as f:
    s = f.read()

compressed_str = ''
inscription_numbers = re.split('(......)', s)[1::2]
prev_number = 0
is_continuous = False
for i in inscription_numbers:
    current_number = int(i)

    if current_number == prev_number + 1:
        # 一致している場合 = 連続している
        is_continuous = True
    else:
        # 一致していない場合
        if is_continuous == True:
            compressed_str += '-' + str(prev_number) + str(current_number)
        else:
            compressed_str += str(current_number)
        is_continuous = False
    
    prev_number = current_number

if is_continuous == True:
    compressed_str += '-' + str(prev_number) + str(current_number)


print(compressed_str)

# 2段階目の圧縮

two_digits_list = ['38', '39', '40', '41']
td_index = 0
td_count = 0
count_info = ''

compressed_str2 = ''

for i in compressed_str.split('-'):
    inscription_numbers = re.split('(......)', i)[1::2]
    for j in inscription_numbers:
        if j[0:2] == two_digits_list[td_index]:
            td_count += 1
        else:
            td_index += 1
            
            count_info += str(td_count) + '/'
            td_count = 1

        compressed_str2 += j[2:]

    compressed_str2 += '-'

count_info += str(td_count) + '/'

# 38, 39, 40, 41 それぞれの個数
print(count_info)



with open('numbers_compressed.txt', mode='w') as f:
    f.write(compressed_str2)
