principle =0
rate =0
time =0

while principle <= 0 :
    principle =float(input ("principle amount is: "))
if principle <= 0:
    print ("principle amount can not be zero or negative")

while rate <= 0 :
    rate =float(input("rate amount is: "))
if rate <= 0:
    print (" rate amount can not be zero or negative")

while time <= 0 :
    time= int(input("time is: "))
if time <= 0:
    print ("time can not be zero or negative")


total = principle*pow((1+rate/100), time)
print (f"amount is{time} :${total:.2f} ")