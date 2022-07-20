# PYTHON MODULE DECLARATION
import random
import smtplib
import re
import datetime
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from sys import exit
from art import *
from rich.progress import Progress
from rich.console import Console
from rich.markdown import Markdown
from colorama import Fore
from os import system, name


# UNIVERSAL CLEAR SCREEN FUNCTION
def crossClear():
    
    if name == 'nt':
        system('cls')
    
    else:
        system('clear')


# CLEAR SCREEN FUNCTION
def clearScreen():
    
    # Obligates to clear screen at begginning of execution
    crossClear()

# ABOUT FUNCTION
def about():
    
    try:
        
        # Identify the rich console
        console = Console() 
        
        # Reads the markdown file 
        with open('README.md') as read:
            read_markdown = Markdown(read.read())
        
        # Print the markdown
        console.print(read_markdown)
        
        print()
        print()
    
        while True:
            print(Fore.BLUE + "[Type 'b' to back to main menu]")
            response = input("> ")
            response = response.lower()
    
            if response == 'b':
                crossClear()
                mainMenu()
                break
        
            else:
                print()
                print(Fore.RED + "[Invalid keyword please try again]")
                print()
    
    except Exception as ex:
        print(Fore.RED , ex)
        
    
# SEND THRU USER EMAIL FUNCTION
def sendThruEmail():
    
    try:
        
        console = Console()
        
        # REGULAR EXPRESSION PATTERN
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        
        # EMAIL CONTENT
        email_content = "Hello user, this is your generated password from pypazz console app. Thank you"
    
        # SETUP THE SENDER AND RECEIVER
        sender_email_address = 'your_email@email.com'
        sender_password = 'your_password'
        
        print(Fore.WHITE + "Email Address")
        receiver_email_address = input(Fore.WHITE + "> ")
        
        print()
        
        if re.match(pattern, receiver_email_address):
            
            with console.status("[bold green] Sending email please wait . . .") as stat:
                while True:
                    sleep(3)
                    break
            
            print()
            print(Fore.GREEN + "[Email sent ! Please check your email]")
    
            # SETUP THE MIME
            message = MIMEMultipart()
            message['From'] = sender_email_address
            message['To'] = receiver_email_address
            message['Subject'] = "PYPAZZ VER 1.1 GENERATED PASSWORD DATA"
    
            # SUBJECT LINE
            # BODY AND THE ATTACHMENTS FOR EMAIL
            message.attach(MIMEText(email_content, 'plain'))
            attach_file = 'password.txt'
            attach = open(attach_file, 'rb')
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach).read())
    
            # ENCODE THE ATTACHMENT
            encoders.encode_base64(payload)
    
            # ADD PAYLOAD HEADER WITH FILENAME
            payload.add_header('Content-Disposition', 'attachment', filename = attach_file)
            message.attach(payload)
    
            # CREATE SMTP TO SEND EMAIL
            session = smtplib.SMTP('smtp.gmail.com', 587)
    
            # ENABLE SECURITY
            session.starttls()
    
            # LOGIN WITH EMAIL AND PASSWORD
            session.login(sender_email_address, sender_password)
    
            text = message.as_string()
            session.sendmail(sender_email_address, receiver_email_address, text)
            session.quit()
            
        else:
            
            crossClear()
            print(Fore.RED + "[Email is not allow to sent. Please check your email address first if it is valid or invalid]")
            print()
            sendThruEmail()
        
        
        while True:
            
            print()
            print(Fore.BLUE + "Please type 'x' to exit")
            response = input(Fore.BLUE + "> ")
            response = response.lower()
            
            if response == 'x':
                exit()
            
            else:
                print()
                print(Fore.RED + "[Invalid keyword please try again]")
                print()
    
    except Exception as ex:
        print()
        print(Fore.RED , ex)
        print()
        

# GENERATE PASSWORD FUNCTION
def generatePassword():
    
    # EXECUTE LOOP IF ERROR CATCHES WHILE INPUTTING NUMBER
    while True:
        
        try:
            
            console = Console()
            
            password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            user_id = '0123456789'
            
            print(Fore.WHITE + "Password Length")
            password_length = int(input(Fore.WHITE + "> "))
            
            print()
            
            with console.status("[bold green] Generating your password please wait . . .") as stat:
                
                while True:
                    sleep(3)
                    break
            
            print(Fore.GREEN + "[Password generated successfully ! Read the next step and follow it to get your password]")
                    
            print()
            print()
            
            with open('password.txt', 'w') as password_file:
                
                try:
                    
                    if password_file:
                        
                        password_file.write("PYPAZZ GENERATED PASSWORD DATA")
                        password_file.write('\n\n')
                        
                        password_file.write("User ID: ")
                        
                        
                        for user_id_limit in range(1):
                            
                            for user_id_length in range(10):
                                
                                randomize_user_id = random.choice(user_id)
                                password_file.write(randomize_user_id)
                            password_file.write('\n\n')
                        
                        password_file.write("Password: ")
                        
                        for password_limit in range(1):
                            
                            for password_len in range(password_length):
                                
                                randomize_password = random.choice(password_characters)
                                password_file.write(randomize_password)
                            password_file.write('\n\n')
                        
                        date = datetime.datetime.now()
                        
                        password_file.write("Date Generated: " + date.strftime("%A, %d %B %Y, %I:%M %p"))
                        password_file.write('\n')
                        
                        password_file.write("=======================================")
                        password_file.write('\n\n')
                        
                        password_file.close()
                    
                    else:
                        
                        crossClear()
                        print(Fore.RED + "[Something went wrong]")
                        print()
                
                except Exception as ex:
                    print(Fore.RED + ex)
                
                while True:
                    
                    print(Fore.BLUE + "[Please type 'E' to redirect in email page]")
                    response = input(Fore.BLUE + "> ")
                    response = response.lower()
                    
                    if response == 'e':
                        
                        crossClear()
                        sendThruEmail()
                        break
                    
                    else:
                        print(Fore.RED + "[Invalid keyword please try again]")
                        print()
        
        except ValueError:
            crossClear()
            print(Fore.RED + "[Strings or other characters are not accepted only INTEGERS are valid.]")
            print()


# MAIN MENU FUNCTION
def mainMenu():
    
    while True:
        console_app_title = "PyPazz"
        tprint(console_app_title)
        print()
    
        print(Fore.WHITE + "(C) Veruz Rux Ceyenne. All rights reserved")
        print(Fore.WHITE + "[Version 1.1]")
        print()
        
        print(Fore.WHITE + "MAIN MENU")
        print()
        print(Fore.WHITE + "[A] Generate Password")
        print(Fore.WHITE + "[B] About")
        print(Fore.WHITE + "[C] Quit")
        print()
        
        print(Fore.WHITE + "Enter your choice")
        choice = input(Fore.WHITE + "> ")
        
        
        if choice == 'a':
            crossClear()
            generatePassword()
            break
        
        elif choice == 'b':
            crossClear()
            about()
            break
        
        elif choice == 'c':
            exit()
        
        else:
            crossClear()
            print()
            print(Fore.RED + "[Invalid input please try again]")
            print()
            

# LOADING SCREEN FUNCTION
def loading():
    
    with Progress() as load:
        
        print()
        print()
        
        task = load.add_task("[bold green] Initializing", total = 100)
        
        while not load.finished:
            
            load.update(task, advance = 0.3)
            sleep(0.01)
    
    crossClear()
    mainMenu()
    

# CONSOLE FUNCTION
def consoleFunction():
    
    global console
    
    console = Console()


# MAIN FUNCTION
def main():
    
    clearScreen()
    loading()


# HANDLES MAIN FUNCTION
if __name__ == '__main__':
    
    main()