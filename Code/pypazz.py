# MODULE DECLARATION
import getpass
import os
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




# CLEAR SCREEN FUNCTION
def clearScreen():
    
    os.system('cls')


# ABOUT FUNCTION
def about():
    
    print("[+] ABOUT THIS PROGRAM: ")
    print()
    print("This program is generate password that helps you secured your password. The password generated will send thru your gmail. This program also is free")
    print()
    
    print("[+] DEVELOPER: ")
    print()
    print("Veruz Rux Ceyenne")
    print()
    
    print()
    
    while 1:
    
        response = input("[>] Type 'b' to back to main menu: ")
        response = response.lower()
    
        if response == 'b':
        
            os.system('cls')
            mainMenu()
            break
        
        else:
            print()
            print("[x] Invalid keyword please try again")
            print()
    
# SEND THRU USER EMAIL FUNCTION
def sendThruEmail():
    
    try:
        
        # REGULAR EXPRESSION PATTERN
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        
        # EMAIL CONTENT
        email_content = "Hello user, this is your generated password from pypazz console app. Thank you"
    
        # SETUP THE SENDER AND RECEIVER
        sender_email_address = 'youremail@email.com'
        sender_password = '[yourpassword]'
        receiver_email_address = input("[>] Enter email address: ")
        
        
        
        if re.match(pattern, receiver_email_address):
            
            sleep(3)
            print()
            print("[i] Email Sent !")
            print()
    
            # SETUP THE MIME
            message = MIMEMultipart()
            message['From'] = sender_email_address
            message['To'] = receiver_email_address
            message['Subject'] = "PYPAZZ VER 1.0 GENERATED PASSWORD DATA"
    
            # SUBJECT LINE
            # BODY AND THE ATTACHMENTS FOR EMAIL
            message.attach(MIMEText(email_content, 'plain'))
            attach_file = 'generated_password.txt'
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
            
            os.system('cls')
            print("[x] Invalid email address. Please check your email address and try again")
            print()
            sendThruEmail()
        
        
        while True:
            
            response = input("[>] Please type 'x' to exit: ")
            response = response.lower()
            
            if response == 'x':
                exit()
            
            else:
                print()
                print("[x] Invalid keyword please try again")
                print()
    
    except Exception as ex:
        print(ex)



# GENERATE PASSWORD FUNCTION
def generatePassword():
    
    # EXECUTE LOOP IF ERROR CATCHES WHILE INPUTTING NUMBER
    while True:
        
        try:
            
            password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            user_id = '0123456789'
            
            password_length = int(input("[>] Password Length: "))
            
            print()
            
            print("[i] Generating your password please wait . . .")
            
            sleep(3)
            
            print()
            
            print("[i] Password generated successfully")
            
            print()
            
            with open('generated_password.txt', 'w') as password_file:
                
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
                        
                        os.system('cls')
                        print("[x] Something went wrong")
                        print()
                
                except Exception as ex:
                    print(ex)
                
                while True:
                    
                    response = input("[>] Type 's' to send generated password in your email then type 'b' to back to main menu: ")
                    response = response.lower()
                    
                    if response == 's':
                        
                        os.system('cls')
                        sendThruEmail()
                        break
                    
                    elif response == 'b':
                        
                        os.system('cls')
                        mainMenu()
                        break
                    
                    else:
                        print("[x] Invalid keyword please try again")
                        print()
        
        except ValueError:
            os.system('cls')
            print("[x] Strings or other characters are not accepted only INTEGERS are valid.")
            print()


# MAIN MENU FUNCTION
def mainMenu():
    
    # EXECUTE LOOP IF INVALID INPUT IS MET
    while True:
        
        print("========================================================================================================================")
        print("\t\t\t\tPYPAZZ [Version 1.0]")
        print("\t\t\t\t(c) Veruz Rux Ceyenne. All rights reserved")
        print("========================================================================================================================")
        print()
        
        print("MAIN MENU")
        print()
        print("[A] Generate Password")
        print("[B] About")
        print("[C] Quit")
        print()
        
        choice = input("[>] ")
        choice = choice.lower()
        
        # CHECKS THE CHOICES
        if choice == 'a':
            
            os.system('cls')
            generatePassword()
            break
        
        elif choice == 'b':
            
            os.system('cls')
            about()
            break
        
        elif choice == 'c':
            
            exit()
        
        else:
            os.system('cls')
            print("[x] Invalid choice please try again")
            print()

# LOGIN FUNCTION
def login():
    
    # EXECUTE LOOP IF PASSWORD IS NOT MET
    while True:
        
        # INFORMATION TITLE
        notes = "[i]: Please type 'pypazz' as a password to get access within this program."
        print(notes)
        print()
        
        # PASSWORD VARIABLE DECLARATION
        password = getpass.getpass("[>] Please enter password: ")
        print()
        print("[i] Checking password . . .")
        sleep(2)
        
        # CONDITION THAT CHECKS PASSWORD
        if password == 'pypazz':
            os.system('cls')
            print("[+] Initializing pypazz . . .")
            sleep(3)
            os.system('cls')
            mainMenu()
            break
        
        else:
            os.system('cls')
            print("[x] Incorrect password please try again")
            print()


# MAIN FUNCTION
def main():
    
    clearScreen()
    login()


# HANDLES MAIN FUNCTION
if __name__ == '__main__':
    
    main()