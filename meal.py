x = input("What time is it?")
hours,minutes = x.split(":")
hours = int(hours)
minutes = int(minutes)

if hours == 7 and 60 > minutes >= 0:
    print("breakfast time")
elif hours == 8  and  minutes == 0:
    print("breakfast time")
elif hours == 12 and 60 > minutes >= 0:
    print("lunch time")
elif hours == 13 and minutes == 0:
    print("lunch time")
elif hours == 18 and 60 > minutes >= 0:
    print("dinner time")
elif hours == 19 and minutes == 0:
    print("dinner time")
else:
    print()