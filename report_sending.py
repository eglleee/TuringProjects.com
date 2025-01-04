from pathlib import Path
import Main_file
import smtplib
from email.mime.text import MIMEText
import passwords


def main():
    which_report_to_send()


def which_report_to_send():
    report_list = get_report_list()
    if not report_list:
        print("You currently have no reports saved. Try recording a period as complete and then you can receive it via email.")
        Main_file.main()
    else:
        print("Your current reports are:")
        for report in report_list:
            print(report.replace(".txt", ""))   
        print("Which one would you like to receive via email?")
        report = get_user_input(report_list)
        read_report(report)
        report_body = read_report(report)
        body = (f"Hello!\n\nHere is your report:\n\n{report_body}")
        subject = "Financial report"
        sender = "egletestingpython@gmail.com"
        recipients = "egletestingpython@gmail.com"
        password = passwords.password
        send_email(subject, body, sender, recipients, password)


def get_user_input(list):
    while True:
        user_selected_report = input("Report: ").strip().lower()
        user_selected_report = user_selected_report +".txt"
        if user_selected_report not in list:
            print("This report does not exist")
            continue
        else:
            return user_selected_report 


def read_report(report):
    body = []
    with open(report, "r") as file:
        lines = file.readlines()    
        body.append(lines)
    return body


def get_report_list():
    directory = Path(r"C:\Users\eglet\OneDrive\Desktop\Coding\Module 1 main Project")
    txt_files = [file.name for file in directory.glob("*.txt")]
    try:
        txt_files.remove("current_period.txt")
        txt_files.remove("README.txt")  
    except ValueError:
        txt_files.remove("README.txt") 
    return txt_files


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

if __name__ == "__main__":
    main()