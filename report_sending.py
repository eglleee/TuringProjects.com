from pathlib import Path

def main():
    which_report_to_send()


def which_report_to_send():
    report_list = get_report_list()
    if not report_list:
        print("You currently have no reports saved. Try recording a period as done and then you can receive it via email.")
    else:
        print("Your current reports are:")
        for report in report_list:
            print(report)   #.remove(".txt")
        print("Which one would you like to receive via email?")



def get_report_list():
    directory = Path(r"C:\Users\eglet\OneDrive\Desktop\Coding\Module 1 main Project")
    txt_files = [file.name for file in directory.glob("*.txt")]
    try:
        txt_files.remove("current_period.txt")
        txt_files.remove("README.txt")  
    except ValueError:
        txt_files.remove("README.txt") 
    return txt_files


if __name__ == "__main__":
    main()