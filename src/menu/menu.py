#! /usr/bin/python3
from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
from src.menu.logo import logo, toolsLogo
from src.core.whitepages import whitepages
from src.core.phishing import pyphisher
from src.core.toLazyToTypeOver.clear import clear

def Mainmenu():
    choice ='0'
    while choice =='0':
        print(Fore.WHITE + u"""
    1.tools
    2.Check for updates
    3.TrAiN
    4.exit
                """)
        choice = input ("Please make a choice: ")
        if choice == "4":
            print()
            exit(Fore.WHITE + u"thanks for stalking by")
        elif choice == "3":
            TrAiN()
            sleep(1)
            clear()
            logo()
            Mainmenu()
        elif choice == "2":
            print("im working on it")
            #cmd("git clone --depth=1 https://github.com/TIBTHINK/Dead-Watchman.git")
        elif choice == "1":
            clear()
            toolsLogo()
            tools()   
        else:
            print("I don't understand your choice.")
            sleep(4)
            clear()
            logo()
            Mainmenu()

def TrAiN():
    cmd("sl")

def tools():
    Tchoice = '0'
    while Tchoice =='0':
        print(Fore.WHITE + u"""
    1.Whitepages lookup
    2.Pyphisher
    99.go back
                """)
        Tchoice = input("Please make a choice: ")
        if Tchoice == "1":
            whitepages.info()
        elif Tchoice == "2":
            pyphisher()
        elif Tchoice == "99":
            Mainmenu()
        else:
            print("I don't understand your choice.")
            sleep(4)
            clear()
            toolsLogo()
            tools()