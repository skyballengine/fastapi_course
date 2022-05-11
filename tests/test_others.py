my_str = "6 cents"
# dig_str = "5"
# print(dig_str.isdigit() > 5)


char_list = [char for char in my_str]
for char in char_list:
    if char == " " or char.isdigit() > 5:
        char_list.remove(char)
    else:
        continue
print(char_list)
