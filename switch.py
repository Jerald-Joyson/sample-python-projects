def get_week_day(argument):
  switcher = {
    0: "Sunday" ,
    1: "Monday" ,
    5: "Friday" ,
    4: "Thursday" ,
    3: "Wednesday" ,
    2: "Tuesday" ,
    6: "Saturday"
  }
  return switcher.get(argument, "Invalid day")

print (get_week_day(6))
print (get_week_day(8))
print (get_week_day(0))

def odd(n):
  return n % 2 == 1

list(filter(odd, range(10)))
odd(10)
