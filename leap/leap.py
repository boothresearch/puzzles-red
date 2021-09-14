def leap_year(year):
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                print('The year', year, 'is a leap year')
                return(True)
            else:
                print('The year', year, 'is not a leap year')
                return(False)
        else:
            print('The year', year, 'is not a leap year')
            return(True)
    else:
        print('The year', year, 'is not a leap year')
        return(False)