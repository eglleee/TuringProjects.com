import create_period_finances
import savings
import sys
import recording_period
import current_period_report
import report_sending

def main():

    print("What do you want to do?")
    print("a) Edit new period finances")
    print("b) Get a report of current period")
    print("c) Record existing period as finalized")
    print("d) Check savings")
    print("e) Receive a report for previous period")
    print("f) Exit")
    
    while True:
        
        choice  = input("Select: " ).strip().lower()

        if choice == "a":
            create_period_finances.main()
            break

        elif choice == "c":
            recording_period.main()
            break

        elif choice == "b":
            current_period_report.main()
            break

        elif choice == "d":
            savings.main()
            break

        elif choice == "e":
            report_sending.main()
            break

        elif choice == "f":
            sys.exit("Bye!")
            break
        else:
            print("You must select one of the options above!")
            continue


if __name__ == "__main__":
    main()