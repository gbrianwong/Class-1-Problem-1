#Calculate the tip

def main():
    cost = cost_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("How much would you like to tip? "))
    tip = cost * percent
    print(f"You will tip ${tip:.2f}")

def cost_to_float(c):
    return float(c.replace("$", ""))

def percent_to_float(p):
    return float(p.replace("%", "")) / 100

main()
