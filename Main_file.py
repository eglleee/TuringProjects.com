import create_period_finances
import savings
import sys
import recording_period
import current_period_report

def main():

    print("What do you want to do?")
    print("a) Edit new period finances")
    print("b) Record existing period as finalized")
    print("c) Get a report of current period")
    print("d) Check savings")
    print("f) Exit")
    
    choice  = input("Select: " ).strip()

    if choice == "a":
        create_period_finances.main()

    elif choice == "b":
        recording_period.main()

    elif choice == "c":
        current_period_report.main()

    elif choice == "d":
        savings.main()

    elif choice == "f":
        sys.exit("Bye!")


if __name__ == "__main__":
    main()