def say(number):
    def return_string(number):
        dict_one_ten = {
            0: '',
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine',
            10:'ten',
            11:'eleven',
            12:'twelve',
            13:'thriteen',
            14:'fourteen',
            15:'fiveteen',
            16:'sixteen',
            17:'seventeen',
            18:'eighteen',
            19:'nineteen'
        }
        dict_multiples_ten = {
            2:'twenty',
            3:'thirty',
            4:'fourthy',
            5:'fivty',
            6:'sixty',
            7:'seventy',
            8:'eighty',
            9:'ninety'
        }

        if number==0:
            words = 'zero'
        elif number<20:
            words = dict_one_ten[number]  
        elif (number>=20)&(number<=99):
            first_digit = int(number/10)
            second_digit = number - first_digit*10
            if second_digit==0:
                words = dict_multiples_ten[first_digit]  
            else:
                words = dict_multiples_ten[first_digit] + '-' + dict_one_ten[second_digit]  
        elif number>99:
            first_digit = int(number/100)
            second_digit = number - first_digit*100
            words = dict_one_ten[number] + ' hundred ' + return_string(second_digit)
        return(words)

    def split_number(number):
        import re
        str_number = str(number)
        chunk = re.findall('.{1,3}', str_number[::-1])
        for i, string in enumerate(chunk):
            print(i)
            print(string)
            chunk[i] = int(string[::-1])
            chunk = chunk[::-1]
        return(chunk)

    def add_scaling(chunks):
        if len(chunks)==2:
            return chunks[0] + 'thousand' + chunks[1]
        elif len(chunks)==3:
            return chunks[0] + 'million' + chunks[1] + 'thousand' + chunks[2]
        elif len(chunks)==4:
            return chunks[0] + 'billion' + chunks[1] + 'million' + chunks[2] + 'thousand' + chunks[3]
        elif len(chunks)==5:
            return  chunks[0] + 'trillion'+ chunks[1] + 'billion' + chunks[2] + 'million' + chunks[3] + 'thousand' + chunks[4]




    if (number>999999999999)|(number<0):
         print('Number not in correct range')
         return False
    else:
        say = return_string(number)
        return(say)
