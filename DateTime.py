##from datetime import timedelta,date
##today=date.today()
##nxtweek=timedelta(days=7)+today
##print("Date after 1 week is",nxtweek)

##from datetime import datetime
##now=datetime.now()
##print(now)

##from datetime import date
##today=date.today()
##date=today.strftime("(%d)(%m)(%Y)")
##print(date)

from datetime import datetime
def ValidPassport(passport,today):
    if len(passport)<10:
        return "Invalid"
    Country=passport[:3]
    ValidCountry=["USA","IND","GBR","CAN"]
    if Country not in ValidCountry:
        return "Invalid"
    PassportNumber=passport[3:12]
    if not PassportNumber.isdigit() or len(PassportNumber)!=9:
        return "Invalid"
    EndDate=passport[12:22]
    try:
        EndDate=datetime.strptime(EndDate,"%Y-%m-%d")
    except ValueError:
        return "Invalid"
    Date=datetime.strptime(today,"%Y-%m-%d")
    if EndDate<Date:
        return "Invalid"
    Symbols="!@#$%^&*()_+-=~"
    if not any(char in Symbols for char in passport):
        return "Invalid"
    if " " in passport:
        return "Invalid"
    if not ("GOV" in passport or "EMB" in passport or "CONS" in passport):
        return "Invalid"
    return "Valid"
passport1 = "USA1234567892025-12-31!GOV"
passport2 = "CAN9876543212022-05-15CONS"
passport3 = "IND9871234562024-10-10@"
today = "2024-10-03"
print(ValidPassport(passport1, today))
print(ValidPassport(passport2,today))
print(ValidPassport(passport3,today))
