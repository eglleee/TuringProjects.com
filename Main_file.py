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
    
    while True:
        
        choice  = input("Select: " ).strip().lower()

        if choice == "a":
            create_period_finances.main()
            break

        elif choice == "b":
            recording_period.main()
            break

        elif choice == "c":
            current_period_report.main()
            break

        elif choice == "d":
            savings.main()
            break

        elif choice == "f":
            sys.exit("Bye!")
            break
        else:
            print("You must select one of the options above!")
            continue


if __name__ == "__main__":
    main()