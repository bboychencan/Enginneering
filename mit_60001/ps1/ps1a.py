def house_hunting():
	annual_salary = float(input("Enter your annual salary: "))
	portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
	total_cost = float(input("Enter the cost of your dream home: "))

	down_payment = total_cost * 0.25
	r = 0.04
	cur = 0
	month = 0
	while cur < down_payment:
		month += 1
		cur += cur * r / 12
		money = annual_salary / 12 * portion_saved
		cur += money

	print("Number of months:", month)

if __name__ == "__main__":
	house_hunting()
