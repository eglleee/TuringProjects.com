import csv
import os
import Main_file
import savings

def main():
    print("What would you like to input?")
    print("a) Period name and income")
    print("b) Current period fundamental expenses")
    print("c) Current period fun expenses")
    print("d) Current period savings")
    print("e) Go back")
    user_choice()


def user_choice():
    user_choice = input("Select: ").strip().lower()

    if user_choice == "a":
        if check_file():
            print("You have already sumbitted you income for this month. Would you like to overwrite it?")
            while True:
                create_new_income = input("y/n: ").strip().lower()
                if create_new_income == "y":
                    delete_income()
                    get_name()
                    get_income()
                    main()                    
                    break
                elif create_new_income == "n":
                    main()
                    break
                else:
                    print("Enter 'y' for 'YES' or 'n' for 'NO'")
                    continue
        else:
            get_name()
            get_income() 
            main()           

    elif user_choice == "b":
        get_fundamental_expenses()
        main()
    elif user_choice == "c":
        get_fun_expenses()
        main()
    elif user_choice == "d":
        savings.main()
    elif user_choice == "e":
        Main_file.main()
    

def delete_income():
    os.remove("current_period.txt")


def check_file():
    income_exists = os.path.exists("current_period.txt")
    return income_exists


def get_name():
    print("Enter the current period name (i.e. '2024 12'):")
    while True:
        period_name = input("Name: ")
        if not period_name:
            print("You must enter a name!")
            continue
        else:
            with open("current_period.txt", "a") as file:
                file.write(f"{period_name}")
            print("Name recorded!")
            break

    
def get_income():
    print("Enter income for the current period:")
    while True:
        period_income = input("Income: ")
        period_income = validate_number(period_income)
        if period_income == None:
            continue
        else:          
            with open("current_period.txt", "a") as file:
                file.write(f"\n{period_income}")
            print("Income recorded!")
            break


def get_fundamental_expenses():
    expense_type = "Fundamental"
    filename = "fundamental_expenses.csv"
    get_expense(expense_type, filename)


def get_fun_expenses():
    expense_type = "Fun"
    filename = "fun_expenses.csv"
    get_expense(expense_type, filename)


def get_expense(expense_type, filename):
    print(f"Enter {expense_type} expenses. You will be prompted to enter {expense_type} "
          f"expense name and then the amount. If you want to stop, press CTRL + Z and enter.")
    while True:
        print(f"Enter {expense_type} expense name and amount (separated by colon, i.e. 'utilities : 541.25')")
        try:
            expense = input("'Name: amount -'").strip()            
            expense_name,  expense_amount = expense.rsplit(":",1)
            expense_name = expense_name.strip()
            expense_amount = validate_number(expense_amount)


            if not expense_name:
                print("You must enter a name!")
                continue  

            if expense_amount == None:
                continue 
  
        except EOFError:
            print("Done")
            break

        except ValueError:
            print("You must enter expense name and amount, separated by colon!")
            continue
        
        write_down_expenses(filename, expense_name, expense_amount)


def write_down_expenses(filename, expense_name, expense_amount):
    file_exists = os.path.exists(filename)  

    with open (filename, "a", newline ="") as file:
        writer = csv.DictWriter(file, fieldnames = ["expense_name", "expense_amount"])

        if not file_exists:
            writer.writeheader()

        writer.writerow({"expense_name": expense_name, "expense_amount": round(expense_amount,2)})
    print("Expense recorded")


def validate_number(number):
    try:
        number = float(number)
        if number >= 0:
            return round(number, 2)
        else:
            print("You should not enter negative values! Try again.")
            number = None
            return number
    except ValueError:
        print("You must enter a number! Try again.")
        number = None   
        return number 
    

if __name__ == "__main__":
    main()