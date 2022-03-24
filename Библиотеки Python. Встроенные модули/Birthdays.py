import datetime as dt
drdate = dt.datetime.now() + dt.timedelta(days=int(input()))
print(f'{drdate.day} {drdate.month}')
