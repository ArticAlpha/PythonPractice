# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

num1=20000

if num1<=10000:
    print("0 Taxable income")
else:
    print("Taxable income: $",10000*0 + 10000*0.1  + (num1-20000)*0.2)
