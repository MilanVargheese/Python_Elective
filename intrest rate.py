amount=float(input("Enter amount: "))
rate=float(input("Enter intrest Rate: "))
print("%-5s %-15s %-15s" % ("Year", "Base Amount", "Final Amount"))
for i in range (1,11):
    final_amount=amount+(amount*rate/100)
    print("%-5d %-15.2f %-15.2f" % (i, amount, final_amount))
    amount=final_amount

    
