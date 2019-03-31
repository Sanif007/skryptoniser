
import os
import sys
import termcolor
from termcolor import colored

print("     _                     _              _ ")
print(" ___| | ___ __ _   _ _ __ | |_ ___  _ __ (_)___  ___ _ __ ")
print("/ __| |/ / '__| | | | '_ \| __/ _ \| '_ \| / __|/ _ \ '__| ")
print("\__ \   <| |  | |_| | |_) | || (_) | | | | \__ \  __/ | ")
print("|___/_|\_\_|   \__, | .__/ \__\___/|_| |_|_|___/\___|_| ")
print("               |___/|_| ")
print(colored("####################################", "green"))
print (colored(" 01. Metasploit ", "red"))
print (colored(" 02. Make playload by Ghost-Droid ", "red"))
print(colored("####################################", "green"))
opt = input(" >>> ")
if opt == "01" or opt == "1" :
        q1 = input("Had you installed it earlier??(y/n) : ")
        if q1 == "no" or q1 == "n":
                 print(" ##### INSTALLING Metasploit ")
                 print(" Remember!! you can't make playload without metasploit ")
                 os.system(" cd && pkg upgrade && pkg install git && pkg install curl && pkg install wget && pkg install nmap && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh ")
                 print (colored(" \n INSTALATION Completed!! ", "green"))
        elif q1 == "y" or q1 == "yes" :
             print(" Trying to run Metasploit ..... ")
             os.system(" msfconsole ")
        else :
             print(" Invalid answer!! type y or n ")
elif opt == "02" or opt == "2" :
       q2 = input(" Had u installed it earlier? (y/n) : ")
       if q2 == "y" or q2 == "yes" :
             print(" Trying to use Ghost-Droid..... ")
             os.system(" cd Ghost-Droid && ./ghost-droid ")
       elif q2 == "n" or q2 == "no" :
            print(" ##### INSTALLING Ghost-Droid \n")
            os.system("pkg upgrade && pkg update ")
            os.system(" git clone https://github.com/GhosTmaNHarsh/Ghost-Droid ")
            os. system(" cd Ghost-Droid && chmod 777 setup.sh && ./setup.sh && ./ghost-droid ")
       else :
            print(" Invalid answer!! type y or n ")
else :
         print(" Enter valid number 1 or 2")
