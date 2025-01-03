import create_period_finances
import os
import csv
import savings_functions
import Main_file

def main():
    monthly_savings()


def monthly_savings():
    current_savings = savings_functions.current_savings_list()
    if not current_savings:
        print("You currently have no recurring savings. What would you like to do?")    
        print("a) Create a new recurring saving")
        print("b) Register one off monthly savings")
        print("c) Go back")

    else:
        print("Your current recurring savings are:")
        for current_saving in current_savings:
            print(current_saving)
        print("what would you like to do?")
        print("a) Create a new recurring saving")
        print("b) Register one off monthly savings")
        print("c) Go back")
        print("d) Add an amount for an existing recurring saving")
    
        what_to_do_with_savings(current_savings)

    
def create_new_saving():
    print("You can create as many savings as you want.")
    savings_name =  get_savings_name()
    savings_current_amount = get_savings_current_amount()
    savings_total_amount = get_savings_total_amount()
    saving_info = get_saving(savings_name, savings_current_amount, savings_total_amount)
    write_down_saving(saving_info)


def what_to_do_with_savings(current_savings):
    while True:
        user_input_for_savings = input("Select: ")
        if user_input_for_savings == "a":
            create_new_saving()
            monthly_savings()
            break

        elif user_input_for_savings == "b":
            expense_type = "Savings"
            filename = "savings_expenses.csv"
            create_period_finances.get_expense(expense_type, filename)
            Main_file.main()
            break

        elif user_input_for_savings == "c":
            Main_file.main()
            break

        elif user_input_for_savings == "d":
            print("Which of the existing savings you would like to add to?")       
            current_savings_lower = []
            for saving in current_savings:
                current_savings_lower.append(saving.lower())
            for current_saving in current_savings:
                print(current_saving)
            while True:
                user_input_for_savings_editing = input("Saving: ").lower().strip()
                if user_input_for_savings_editing not in current_savings_lower:
                    print("Reccuring saving does not exist. Try again")
                    continue
                else:
                    savings_functions.change_saved_amount(user_input_for_savings_editing)
                    Main_file.main()
                    break
        else:
            print("You must select one of the options above!")
            continue
                
   
def get_savings_name():
    while True:
        print("Enter the name for your saving:")
        savings_name = input("Name: ").strip()
        if not savings_name:
            print("You must enter a name!")
            continue
        else:
            return savings_name
    

def get_savings_current_amount():
    while True:
        print("Enter amount, which you already have saved for this:(NOT including this period's amount)")
        savings_current_amount = input("Amount: ").strip()
        savings_current_amount = create_period_finances.validate_number(savings_current_amount)
        
        if savings_current_amount == None:
            ("You must enter a number!")
            continue 
        else:
            return savings_current_amount


def get_savings_total_amount():
    while True:
        print("Enter total amount, which you would like to save for this:")
        savings_total_amount = input("Amount: ").strip()
        savings_total_amount = create_period_finances.validate_number(savings_total_amount)
        
        if savings_total_amount == None:
            ("You must enter a number!")
            continue 
        else:
            return savings_total_amount


def get_saving(savings_name, savings_current_amount, savings_total_amount):
    return{
        "savings_name": savings_name,
        "savings_current_amount" : savings_current_amount,
        "savings_total_amount": savings_total_amount,
        }


def write_down_saving(saving_info):
    file_exists = os.path.exists("savings.csv")  

    with open ("savings.csv", "a", newline ="") as file:
        writer = csv.DictWriter(file, fieldnames = ["savings_name", "savings_current_amount", "savings_total_amount"])

        if not file_exists:
            writer.writeheader()

        writer.writerow(saving_info)
    print("Savings info recorded")
    

if __name__ == "__main__":
    main()