import csv
csv_col=['ID','Name','Place']
dict_data=[{'ID':1,'Name':'Alan','Place':'thrissur'},
           {'ID':2,'Name':'Najmal','Place':'malappuram'},
           {'ID':3,'Name':'Murshid','Place':'thrissur'},
           {'ID':4,'Name':'Ajmal','Place':'idukki'},
           {'ID':5,'Name':'Mahendran','Place':'muvattupuzha'},]

csv_file="Names.csv"
try:
    with open(csv_file,'w')as file1:
        writer=csv.DictWriter(file1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)

except IOError:
    print("ioeror")

data1=csv.DictReader(open(csv_file))
print("csv file as dictionary:\n")
for row in data1:
    print(row)
