import numpy as np
import random


options = ['Favourite singer : ','Favourite colour : ','Favourite Actor : ','Favourite Actress : ','Write 1 to 10 : ','Write Your Name 5 Times : ','Write Your Title 5 Times : ']

def Truth():
    print(options[np.random.randint(0,4)])
    a=input('')
    print('Press A to toss again : ')
    x=input('')
    if x == 'A' or x == 'a' :
        Coin()
    else :
        quit()
    
def Dare() :
    print(options[np.random.randint(4,7)])
    a=input('')
    print('Press A to toss again : ')
    x=input('')
    if x == 'A' or x == 'a':
        Coin()
    else :
        quit()


def Head() :
    print('Press A to toss again : ')
    x=input('')
    if x == 'A' or x == 'a' :
        Coin()
    else :
        quit()

def Tail() :
    print('Choose Truth or Dare or Quit : ')
    choice =input('')
    if choice == 'Truth' or choice == 'truth' :
        Truth()

    if choice == 'Dare' or choice == 'dare' :
        Dare()
    if choice == 'Quit' or choice == 'q' :
        quit()

def Coin() :
    np.random.rand()
    coin = np.random.randint(0,2)
    if coin == 0 :
        print('Head')
        Head()
    else :
        print('Tail')
        Tail()



def printline(msg): print(f"\n{msg}\n")

def print_logo(): printline("""
 _________  __  __________ __
/_  __/ _ \/ / / /_  __/ // /
 / / / , _/ /_/ / / / / _  / 
/_/ /_/|_|\____/ /_/ /_//_/  
     / __/___                
     > _/_ _/                
   _|_____/   ___  ____      
  / _ \/ _ | / _ \/ __/      
 / // / __ |/ , _/ _/        
/____/_/ |_/_/|_/___/""")


def main():
    print_logo()
if __name__ == "__main__":
    main()
    
Coin()
