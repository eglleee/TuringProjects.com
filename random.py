from pathlib import Path

    #report_list = get_report_list()
report_list = ["one.txt"]
if not report_list:
    print("You currently have no reports saved. Try recording a period as done and then you can receive it via email.")
else:
    print("Your current reports are:")
    for report in report_list:
        print(report)   #.remove(".txt")
    print("Which one would you like to receive via email?")

