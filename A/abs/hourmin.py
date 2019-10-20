def HourMinute(num):
    hr = int(num/60)
    min = num % 60
    print(str(hr)+':'+str(min))

HourMinute(0)