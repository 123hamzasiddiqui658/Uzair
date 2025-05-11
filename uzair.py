age=int(input("Enter your age"))
if age<13:
    print("Child")
elif 13>=age and age<=19:
   print("young")
elif age>=20 and age<=59:
    print("adult")
else:
   print("Aged")

car={
   "Brand":"Toyata",
     "Model":"Civic",
      "Year":2024
}
car.pop("year")
car.update({"year":"2022"})
print=("updatecar:",car)

number= [99,5,4,8,66,79,10,44,53,89,57,60]
print("first Number",number[0])
print("Last Number",number[-1])
print("maximun Number",max(number))

num=int(input("Enter your no"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
   print("zero")
