year = int(input("Enter year YYYY:"))

def leapyear(yyyy):
    if yyyy % 4 == 0:
        return "Yes"
    elif yyyy % 4 != 0:
        return "no"
    else:
        return "invalid"

leap_year = leapyear(year)

print (leap_year+", leap year")

