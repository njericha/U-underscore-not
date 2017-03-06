## Side Project: 

#Random number generator: 
# import random 
# random.randrange(a, b) this outputs an integer between [a, b) 

import random 

t3x3=[[0,0,0],[0,0,0],[0,0,0]]

###rules in here

#example of a rule that lowers a value if it is greater than 1
def rule1(table,row,column,value):
    if value > 0:
        table[row][column] = value - 1

def energy_rule(new,row,column,value,old):
    new_value=0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if [i,j] != [0,0]:
                #if column + j >= len(old[0]):
                    #j = len(old[0]) - 1 - column
                #if row + i < 0:
                    #i = len(old) - 1
                    #new_value += old[i][column+j] / 8
                #elif row + i >= len(old):
                    #i = 0
                    #new_value += old[i][column+j] / 8
                #else:
                    #new_value += old[row+i][column+j] / 8
                edit_row = (row + i) % len()
                
    new[row][column]=new_value
    return

###---

def generate_table(x,y): #takes x and y and outputs a table with x rows and y columns
    table = []
    row = []
    while y>0: 
        row.append(0)
        y += -1
    while x>0:
        table.append(row)
        x += -1
    return table

def print_table(table): #takes a table and prints it formated to the screen
    for row in table:
        print(row)
    return None

def next_generation(table): #takes a table and produces the next generation
    next_table = table
    for row in range(0,len(table)):
        for column in range(0,len(table[0])): #rules go in here
            value = table[row][column]
            energy_rule(next_table,row,column,value,table)
    return next_table

def change_table(table,row,column,value):
    table[row][column]=value
    return

def U0(): #the main function
    table=[]
    while True: # asks user to make the board/table of size rowXcolumn
        row = input("Enter how many rows: ")
        column = input("Enter how many columns: ")
        table=generate_table(int(row),int(column))
        print_table(table)
        okay = input("This okay? ('Y' or 'N'): ")
        if okay == 'Y':
            break    
    okay = 'Y'
    while okay == 'Y': #asks user for unitial values
        #okay = input("Would you like to change an initial state?: ")
        #if okay != 'Y':
        #    break
        row = int(input("Enter a row to edit: "))
        column = int(input("Enter a column to edit: "))
        value = int(input("Enter a value: "))
        change_table(table,row,column,value)
        print_table(table)
        okay = input("Would you like to change an initial state?: ")
    
    n = int(input("How many generations would you like?: "))
    while n > 0: #prints all the generations asks
        next_table = next_generation(table)
        print_table(next_table)
        print("-")
        table = next_table
        n += -1
    
    return None