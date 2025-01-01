import recording_period
import os
import create_period_finances


def main():

    income = get_income()
    check_expenses("fundamental")
    fundamental_expenses = count_total_expenses("fundamental")
    check_expenses("fun")
    fun_expenses = count_total_expenses("fun")
    check_expenses("savings")
    savings_expenses = count_total_expenses("savings")
    get_report(income, fundamental_expenses, fun_expenses, savings_expenses)



def get_report(income, fundamental_expenses, fun_expenses, savings_expenses):
    if income == 0:
        print("You have no income this month")
        print(f"Your fundamental expenses are {fundamental_expenses} this period.")
        print(f"Your fun expenses are {fun_expenses} this period.")
        print(f"Your sacings expenses are {savings_expenses} this period.")

    else:
        print(f"Your income this period is {income}")
        count_percentage(fundamental_expenses, income, "fundamental")
        count_percentage(fun_expenses, income, "fun")
        count_percentage(savings_expenses, income, "savings")


def count_percentage(expense_amount, income, expense_type):
    if expense_amount > 0:
        percentage = round(float(expense_amount)/float(income)*100,2)
        print(f"Your {expense_type} expenses are {expense_amount} this period.")
        print(f"It means, {expense_type} expenses are {percentage}% of your income.")
    else:
        print(f"You have has no {expense_type} expense this month")


def count_total_expenses(expense_type):
    return recording_period.count_expense_total(expense_type)


def get_income():
    recording_period.check_if_income_exists()
    with open("current_period.txt", "r") as file:
        lines = file.readlines()    
        income_amount = lines[1].strip()
        return income_amount
    

def check_expenses(expense_type):
    expenses_exist = os.path.exists(f"{expense_type}_expenses.csv")

    if not expenses_exist:
        print(f"You have not recorded any {expense_type} expenses. Would like to record them now or did you not have any this period?")
        print("a) Record now")
        print(f"b) No {expense_type} expenses this period")
        while True:
            record_expenses = input("Answer: ").strip()
            if record_expenses == "a":
                create_period_finances.main()
                break
            elif record_expenses == "b":
                filename = f"{expense_type}_expenses.csv"
                expense_name = "Everything"
                expense_amount = 0
                create_period_finances.write_down_expenses(filename, expense_name, expense_amount)
                break

if __name__ == "__main__":
    main()
