def leap_year(year):
    
    if (year%4==0)&(year%100!=0)&(year%400!=0):
        print('The year', year, 'is a leap year')
    else:
        print('The year', year, 'is not a leap year')