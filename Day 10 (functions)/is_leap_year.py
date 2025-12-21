def is_leap_year(year):
    if not year % 4 == 0:
        return False
    if not year % 100 == 0:
        return True
    if year % 400 == 0:
        return True
    else:
        return False
    
    
print(is_leap_year(2400))
print(is_leap_year(1989))