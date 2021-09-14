def say(number):
    # if (number>999999999999)|(number<0):
    #     print('Number not in correct range')
    #     return False
    # else:
    dict_one_ten = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten'
    }
    dict_multiples_ten = {
        2:'twenty',
        3:'thirty',
        4:'fourthy',
        5'fivty,
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety'
    }

    first_digit = number%10
    second_digit = number - first_digit*10
         
