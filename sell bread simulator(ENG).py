print("You go to the bakery, you need bread. You choose how many kilograms you want")
print(" ")

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

budget = random.choice([3, 5, 10, 20, 25, 50, 100])
running = True

day_count = 1
day_index = 0
current_day = days[day_index]

storage = 0


while running:
    print(current_day)
    print(f"Day {day_count}")
    print(f"Your budget is €{budget}")

    try:
        while True:
            if day_index in (0, 1, 2, 3, 4):
                bread = float(input("How many kg of bread do you want? (€2/kg) "))
            if day_index in (5, 6):
                bread = float(input("How many kg of bread do you want? (€3/kg) "))

            if bread < 100:
                break
            else:
                print("The bakery only has 100 loaves available")

    except ValueError:
        print("Invalid input")
        print(" ")
        continue

    if bread <= 0:
        print(" ")
        print("You must choose a positive amount of kg!")
        continue

    if day_index in (0, 1, 2, 3, 4):
        max_price_bread = random.uniform(3, 6)
    elif day_index in (5, 6):
        max_price_bread = random.uniform(4.5, 7.5)

    if day_index in (0, 1, 2, 3, 4):
        bread_price = bread * 2
    elif day_index in (5, 6):
        bread_price = bread * 3

    total = bread_price
    print(f"Your total is €{total}")

    remaining = budget - total
    print(f"You have €{remaining} left")

    if remaining < 0:
        print("You're in debt, buddy.")
        print("Now you have to work to earn money.")

        while remaining < 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            try:
                answer = int(input(f"What is {a} + {b}? "))
            except ValueError:
                print("Invalid input")
                continue

            if answer == a + b:
                print("Correct, + €5")
                remaining += 5
            else:
                print("Incorrect, try again.")

            print(f"Your balance is now €{remaining}")

        budget = remaining
        print("You're out of debt!")

    print(" ")

    while True:
        bread_action = input("What do you want to do with the bread? (sell/eat/store) ").lower()
        if bread_action in ("sell", "eat", "store"):
            break
        else:
            print("Invalid choice, type 'sell' or 'eat' or 'store'.")

    if bread_action == "sell":
        while True:
            try:
                if day_index in (0, 1, 2, 3, 4):
                    print("maximum price = €3 - €6")
                elif day_index in (5, 6):
                    print("maximum price = €4.5 - €7.5")

                resale_price = float(input("At what price per kg do you want to sell the bread? "))

                if resale_price <= max_price_bread:
                    break
                else:
                    print("Your price is too high, try selling at a lower price")

            except ValueError:
                print("Invalid input! Enter a number.")

        bread_profit = bread * resale_price
        budget = remaining + bread_profit

        print(f"You earn €{bread_profit}")
        print(f"Your new budget is €{budget}")

    elif bread_action == "eat":
        print("Enjoy your meal!")
        budget = remaining

    elif bread_action == "store":
        storage += bread
        budget -= remaining
        print(f"You now have {storage} kg of bread in storage.")

    while True:
        manage = input("Do you want to manage your storage? (yes/no) ")
        if manage in ("yes", "no"):
            break
        else:
            print("Invalid input, type 'yes' or 'no'.")

    if manage == "yes":
        while True:
            storage_sell = input(f"Your storage is {storage}, do you want to sell it? (yes/no) ")
            if storage_sell in ("yes", "no"):
                break
            else:
                print("Invalid input, type 'yes' or 'no'.")

        if storage_sell == "yes":
            while True:
                try:
                    if day_index in (0, 1, 2, 3, 4):
                        print("maximum price = €3 - €6")
                    elif day_index in (5, 6):
                        print("maximum price = €4.5 - €7.5")

                    resale_price = float(input("At what price per kg do you want to sell the bread? "))

                    if resale_price <= max_price_bread:
                        break
                    else:
                        print("Your price is too high, try selling at a lower price")

                except ValueError:
                    print("Invalid input! Enter a number.")

            bread_profit = storage * resale_price
            budget = budget + bread_profit
            storage = 0

            print(f"You earn €{bread_profit}")
            print(f"Your new budget is €{budget}")

        if storage_sell == "no":
            continue

    while True:
        again = input("Do you want to go to the store again tomorrow? (yes/no) ").lower()
        if again == "yes":
            print(" ")
            break
        elif again == "no":
            print("End of simulation")
            running = False
            break
        else:
            print("Invalid input, type 'yes' or 'no'")

    day_count += 1
    day_index += 1

    if day_index >= len(days):
        day_index = 0

    current_day = days[day_index]
