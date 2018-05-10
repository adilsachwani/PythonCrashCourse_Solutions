dose = 4
order = input("Enter doctor's order(mg): ")
water = input("Enter Dilution Water(ml): ")
weight = input("Enter patient's weight(kg): ")

order = float(order)
water = float(water)
weight = float(weight)

concentration = (dose/water)*1000

drug_rate = (order*weight*60)/concentration

print("Drug should be given to patient at " + str(drug_rate) + " ml/hr")

