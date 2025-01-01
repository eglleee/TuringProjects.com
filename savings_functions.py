import savings
import csv
import os
import create_period_finances
import Main_file


def saved_percentage(savings_name):    
    with open("savings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["savings_name"] == savings_name:
                savings_current_amount = float(row["savings_current_amount"])
                savings_total_amount = float(row["savings_total_amount"])
                saved_percentage = round(savings_current_amount/savings_total_amount*100,2)
        return (f"Total amount needed is {savings_total_amount}."
                f"Current saved amount is {savings_current_amount}."
                f"Saved percentage is {saved_percentage}%")
    

def how_long_will_it_take(savings_current_amount, savings_total_amount, additional_savings_amount):
    not_saved_amount = savings_total_amount - savings_current_amount
    time = int(not_saved_amount/additional_savings_amount)
    return(f"If you keep saving {additional_savings_amount} per month,"
           f"you will save {savings_total_amount} in about {time} months")


def current_savings_list():
    savings_list = []
    file_exists = os.path.exists("savings.csv")
    if not file_exists:
        return savings_list
    else:
        with open("savings.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                savings_list.append(row["savings_name"])
        return savings_list


def change_saved_amount(saving_to_be_changed):
    new_savings = []
    with open("savings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["savings_name"].lower() == saving_to_be_changed:
                savings_current_amount = float(row["savings_current_amount"])
                savings_total_amount = float(row["savings_total_amount"])    
                print(f"You currently have saved {savings_current_amount} out of {savings_total_amount}")
                print("What amount will you add this month?")            
                while True:
                    additional_savings_amount = input("Amount: ")
                    additional_savings_amount = create_period_finances.validate_number(additional_savings_amount)
                    if additional_savings_amount == None:
                        print("You must enter a number")
                        continue
                    elif additional_savings_amount == 0:
                        print("You cannot add 0!")
                        continue
                    else:
                        break
                    
                row["savings_current_amount"] = savings_current_amount + additional_savings_amount
                print(f"Amount recorded. Your new saved amount is {row['savings_current_amount']}. ")
                create_period_finances.write_down_expenses("savings_expenses.csv", saving_to_be_changed, additional_savings_amount)
                if compare_amounts(savings_current_amount, savings_total_amount):
                    Main_file.main()
                else:
                    time = how_long_will_it_take(savings_current_amount, savings_total_amount, additional_savings_amount)
                    print(time)                
            new_savings.append({
                "savings_name": row["savings_name"],
                    "savings_current_amount" : row["savings_current_amount"],
                    "savings_total_amount": row["savings_total_amount"],
                })
                
    
    with open ("savings.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["savings_name", "savings_current_amount", "savings_total_amount"])
        writer.writeheader()
        writer.writerows(new_savings)


def compare_amounts(savings_current_amount, savings_total_amount):
    if savings_current_amount >= savings_total_amount:
        print("Saved amount is higher than total saving amount! You already saved what is needed! Congratulations!")
        return True

