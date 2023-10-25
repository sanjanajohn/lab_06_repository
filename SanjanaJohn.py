def encoder(password):
    list = []
    for char in password:
        list.append(char)

    new_list = []
    for ele in list:
        int_ele = int(ele) + 3
        new_list.append(int_ele)

    string = ''
    for ele in new_list:
        string = string + str(ele)

    return string


if __name__ == '__main__':
    bool_var = True
    while bool_var:
        print(f'''
Menu
-------------
1. Encode
2. Decode
3. Quit
        ''')

        menu_choice = int(input('Please enter an option: '))

        if menu_choice == 1:
            password = input('Please enter your password to encode: ')
            print(f'Your password has been encoded and stored!\n')

        elif menu_choice == 2:
            answer = encoder(password)
            print(f"The encoded password is {answer}, and the original password is {password}.\n")

        elif menu_choice == 3:
            bool_var = False


