##def z():
##    k=input("Enter your phone number\n+91")
##    return k
##n=0
##while n!=1:
##    number=z()
##    if phone(number)==True:
##        print('valid number')
##        n=1
##        break
##    else:
##        print("Try again")
##        z()
##def phone(number):
##    if len(number)!=10:
##        return False
##    for i in range(11):
##        if not number[i].isdecimal:
##            return False
##    return True
##    if text[3]!='-':
##        return False
##    for i in range(4, 7):
##        if not text[i].isdecimal():
##            return False
##    if text[7] != '-':
##        return False
##    for i in range(8, 12):
##        if not text[i].isdecimal():
##            return False
##print('415-555-4242 is a phone number:')
##print(isPhoneNumber('415-555-4242'))
##print('Moshi moshi is a phone number:')
##print(isPhoneNumber('Moshi moshi'))
##def isPhoneNumber(text):
##    if len(text)!=10:
##        return False
##    for i in range(0,10):
##        if not text[i].isdecimal():
##            return False
##    return True
##message = input("Enter your name number:")
##for i in range(len(message)):
##    chunk = message[i:i+10]
##    if isPhoneNumber(chunk):
##        print('Phone number found: ' + chunk)
##print('Done')



##import re
##DOB=re.compile(r'(\d\d).(\d\d).(\d\d\d\d)')
##k=input('Enter your text:\n')
##match=DOB.search(k)
##print('Date of birth found:\n'+match.group())
##z=input('What you want me to print from your date of birth\n1.date\n2.month\n3.year\n')
##if z==1:
##    print(match.group(1))
##elif z==2:
##    print(match.group(2))
##else:
##    print(match.group(3))



##print("Hello")
n=int(input("Enter an integer:"))
k=1
while k<=10:
    print(str(n)+"x"+str(k)+"="+str(n*k))
    k=k+1






























    









































































































