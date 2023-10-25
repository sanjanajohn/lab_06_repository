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

# Credit: Nathan Padriga
def decoder(encoded_password):
    raw_password = ""
    for encoded_digit in encoded_password:
        # Add 10 to encoded digit to ensure subtracting 3 does not result in a negative
        # Undo encode offset by subtracting 3
        # Convert new, decoded digit back to string
        # Ex. 2 -> 12 -> 9
        buffer = str((int(encoded_digit)+ 10) - 3)

        # If the tens digit still remains after subtraction, remove it from the string
        # Ex. 15 -> 5
        raw_digit = buffer[-1]

        raw_password += raw_digit

    return raw_password

if __name__ == '__main__':
    bool_var = True
    stored_password = ''

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
            stored_password = encoder(input('Please enter your password to encode: '))
            print(f'Your password has been encoded and stored!\n')

        elif menu_choice == 2:
            print(f"The encoded password is {stored_password}, and the original password is {decoder(stored_password)}.")

        elif menu_choice == 3:
            bool_var = False


