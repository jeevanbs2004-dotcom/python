rice_price=45
Sugar_price=40
Oil_price=130
import random

rice_qty=3
sugar_qty=2.5
oil_qty=1.8
a=rice_price*rice_qty
b=Sugar_price*sugar_qty
c=Oil_price*oil_qty
print("rice total is=",a)
print("sugar total is=",b)
print("oil total is=",c)
total_price=a+b+c
print(total_price)
print("total bill as an integer",int(total_price))
print("total bill as an string",str(total_price))



del_charge=random.randint(5, 10)
final_bill=total_price+del_charge
print(final_bill)