def _get_new_month():
    while True:
        try:
            month = input("Enter a new month: ")
            int_month = int(month)
            if int_month in range(1, 13):
                if int_month < 10:
                    return '0' + month
                return month
            else:
                print("INVALID MONTH\n")
        except:
            print("ENTER A MONTH USING DIGITS\n")
        
def _get_new_day():
    while True:
        try:
            day = input("Enter a new day: ")
            int_day = int(day)
            if int_day in range(0, 32):
                if int_day < 10:
                    return '0' + day
                return day
            else:
                print("INVALID DAY\n")
        except:
            print("ENTER A DAY USING DIGITS\n")


def _get_new_year():
    while True:
        year = input("Enter a valid 4 digit year (YYYY): ")
        if len(year) == 4 and year.isdigit():
            return year
        else:
            print("INVALID YEAR\n")


def get_new_date():
    return [_get_new_month(), _get_new_day(), _get_new_year()]
    
def get_directory():
    return input("Enter a valid directory (Q to quit): ")
