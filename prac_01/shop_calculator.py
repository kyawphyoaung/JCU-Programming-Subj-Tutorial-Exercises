quantity = int(input("Amount of Item :"))
i=1
total = 0
while i < quantity+1:
    price = int(input("Price of Item :"))
    total += price
    i += 1
print("Subtotal :", total)
if total > 100:
    amount = total*0.1
    total -= amount
print("Discount : ",amount)
print("Total : ", total)