'''
Matchsticks problem Solution By @Siddhant Sharma
'''
from colorama import Fore
import os
os.system("clear")
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
green = Fore.GREEN
cyan = Fore.CYAN
banner = '''
                            ┌┬┐╔═╗┌┬┐╔═╗┬ ┬╔═╗┌┬┐╦┌─┐╦╔═┌─┐
                            │││╠═╣ │ ║  ├─┤╚═╗ │ ║│  ╠╩╗└─┐
                            ┴ ┴╩ ╩ ┴ ╚═╝┴ ┴╚═╝ ┴ ╩└─┘╩ ╩└─┘                        
'''
print(yellow,banner,end="")
print(red,'                             Game Created By- SiDDh@nt Sharma')
TotalMatches = 21
box = "-"*20
while TotalMatches >1:
    print(blue,"Matches left", TotalMatches)
    print(green,box)
    UserChance = int(input("enter the number of matchstics you want to take\nThere are four options\n1|\n2|\n3|\n4|\nYOUR CHANCE ::> "))
    if UserChance >4:
        print(red,"***Cheat only take 4 or less than four matchsticks")
        continue
    print(blue,box)
    print(cyan,"You have choosen:",UserChance)
    TotalMatches -= UserChance
    if UserChance == 1:
        print(" Computer chooses 4")
        TotalMatches -=4
    if UserChance == 2:
        print(" Computer chooses 3")
        TotalMatches -=3
    if UserChance == 3:
        print(" Computer chooses 2")
        TotalMatches -=2
    if UserChance == 4:
        print(" Computer chooses 1")
        TotalMatches -=1

print(red,"|---------------------------------------------|")
print(" |Matches left ",1,"                  🤯         |")
print(" |You have to choose last matches you Lose!😭  |")
print(" |Better Luck next time                    😿  |")    
print(" |---------------------------------------------|")
print(Fore.RESET,"")
    