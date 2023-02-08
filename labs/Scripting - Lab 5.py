from datetime import datetime, timedelta

def calculate_seconds_alive(birth_date):
    today = datetime.now()
    delta = today - birth_date
    return delta.total_seconds()

birth_date = input("Enter your date of birth (DD-MM-YYYY): ")
birth_date = datetime.strptime(birth_date, "%m-%d-%Y")

seconds_alive = calculate_seconds_alive(birth_date)
print("You have been alive for {} seconds.".format(int(seconds_alive)))
