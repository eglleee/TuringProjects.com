import os
import create_period_finances
import csv
import Main_file


def main():
    check_if_income_exists()
    get_income_data()
    file_name, income_amount = get_income_data()
    create_recording_file(file_name, income_amount)
    main_pt2(file_name)


def main_pt2(file_name):
    check_if_fundamental_expenses_exist(file_name)        
    get_expenese_data("fundamental", file_name)
    main_pt3(file_name)


def main_pt3(file_name):
    check_if_fun_expenses_exist(file_name)
    get_expenese_data("fun", file_name)
    if check_if_savings_exist():
        get_expenese_data("savings", file_name)    
    delete_files()
    print("Expenses recorded!")
    Main_file.main()


def delete_files():
    os.remove("current_period.txt")
    os.remove("fundamental_expenses.csv")
    os.remove("fun_expenses.csv")
    if check_if_savings_exist():
        os.remove("savings_expenses.csv")


def check_if_savings_exist():
    return os.path.exists("savings_expenses.csv")

    
def check_if_income_exists():
    income_exists = os.path.exists("current_period.txt")
    
    if not income_exists:
        print("You do not have any income recorded this month. If you do not have any income, you can enter 0, but you must enter a file name!")
        create_period_finances.main()

     
def check_if_fundamental_expenses_exist(file_name):
    
    fundamental_expenses_exist = os.path.exists("fundamental_expenses.csv")

    if not fundamental_expenses_exist:
        print("You have not recorded fundamental expenses. Would like to record them now or did you not have any this period?")
        print("a) Record now")
        print("b) No fundamental expenses this period")
        while True:
            record_fundamental_expenses = input("Answer: ").strip()
            if record_fundamental_expenses == "a":
                create_period_finances.main()
                break
            elif record_fundamental_expenses == "b":
                filename = "fundamental_expenses.csv"
                expense_name = "Everything"
                expense_amount = 0
                create_period_finances.write_down_expenses(filename, expense_name, expense_amount)
                break
            else:
                print("Please selce a or b!")
                continue
        main_pt3(file_name)
        

def check_if_fun_expenses_exist(file_name):
    fun_expenses_exist = os.path.exists("fun_expenses.csv")

    if not fun_expenses_exist:
        print("You have not recorded fun expenses. Would like to record them now or did you not have any this period?")
        print("a) Record now")
        print("b) No fun expenses this period")
        while True:
            record_fun_expenses = input("Answer: ").strip()
            if record_fun_expenses == "a":
                create_period_finances.main()
                break
            elif record_fun_expenses == "b":
                filename = "fun_expenses.csv"
                expense_name = "Everything"
                expense_amount = 0
                create_period_finances.write_down_expenses(filename, expense_name, expense_amount)
                break
            else:
                print("Please selce a or b!")
                continue
        main_pt2(file_name)


def get_income_data():
    with open("current_period.txt", "r") as file:
        lines = file.readlines()    
        file_name = lines[0].strip()
        income_amount = lines[1].strip()
        return file_name, income_amount


def get_expenese_data(expense_type, file_name):
    total_expense_amount = count_expense_total(expense_type)
    text_to_write = f"Total {expense_type} expenses,{total_expense_amount}\n"
    update_recording_file(file_name, text_to_write)
    
    with open(f"{expense_type}_expenses.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            text_to_record = f"{row['expense_name']},{row['expense_amount']}\n"
            update_recording_file(file_name, text_to_record)
            

def count_expense_total(expense_type):
    total_expense_amount = 0
    with open(f"{expense_type}_expenses.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_expense_amount += float(row["expense_amount"])
    return total_expense_amount
        

def create_recording_file(file_name, income_amount):
    with open(f"{file_name}.txt", "w") as file:
        file.write(f"Income:{income_amount}\n")


def update_recording_file(file_name, text_to_write):
    with open(f"{file_name}.txt", "a") as file:
        file.write(text_to_write)


if __name__ == "__main__":
    main()
