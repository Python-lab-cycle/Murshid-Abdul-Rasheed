startyear=int(input("enter start year : "))
endyear=int(input("enter end year : "))
print("list of leap years  : ")
for year in range(startyear,endyear):
    if((year%4==0)and(year%100!=0)or(year%400==0)):
       print(year)
