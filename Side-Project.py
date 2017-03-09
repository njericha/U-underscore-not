## Side Project: 

#Random number generator: 
# import random 
# random.randrange(a, b) this outputs an integer between [a, b) 

import random 

##----rules toggle go here----##

rule_energy = True
rule_threshold = True

##----constents go in here----##

t3x3=[[0,0,0],\
      [0,0,0],\
      [0,0,0]]

defult_table=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],\
              [0.0, 8.0, 0.0, 0.0, 0.0, 0.0],\
              [0.0, 0.0, 336, 0.0, 0.0, 0.0],\
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],\
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],\
              [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
              
dtrt = 2 #<<-- number of decimals to round the printed values

threshold = 42 #<<-- must be an int


##------rules go in here------##

#example of a rule that lowers a value if it is greater than 1
##def rule1(table,row,column,value):
    ##if value > 0:
        ##table[row][column] = value - 1

def energy_rule(new,row,column,old,value):
    """
    radiates an 8th of a cells energy to adjacent cells
    (unless it equals threshold) 
    
    """
    if not rule_energy: #<- checks if this rule is turned on
        return value
    new_value=0
    len_row = len(old)
    len_column = len(old[0])
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if [i,j] != [0,0]:
                edit_row = (row + i) % len_row
                edit_column = (column + j) % len_column
                if rule42(old[edit_row][edit_column]): #<-rule42 check needed here
                    new_value += old[row][column]
                else:
                    temp = old[edit_row][edit_column]
                    new_value += old[edit_row][edit_column]                    
    new[row][column] = new_value / 8
    return new_value / 8

def rule42(value):
    """
    if a cell has an integer of threshold, it will not radiate energy and 
    ajacent cells will get an 8th of it's energy back
    (i.e. energy gets bounced back)
    """   
    if rule_threshold and round(value) == threshold:
        return True
    else:
        return False


##--helper functions go here---##


def next_generation(table):
    """
    takes a table and itterates the next generation
    """
    next_table = table_copy(table)
    for i in range(0,len(table)):
        for j in range(0,len(table[0])): 
            #rules go in here ## <<-----------           
            value = table[i][j]
            if not rule42(value):               
                new_value = energy_rule(next_table,i,j,table,value)
            else:
                pass
    return next_table

def generate_table(x,y):
    """
    takes x and y and outputs a blank table with x rows and y columns
    """    
    table = []
    row = []
    while y>0: 
        row.append(0)
        y += -1
    while x>0:
        table.append(row)
        x += -1
    return table

def print_table(table):
    """
    takes a table and prints it formated to the screen
    """
    for row in table:
        print(list(map(lambda x: round(x,dtrt),row)))
    return None

def change_table(table,row,column,value):
    """
    use this if you don't want to use table[i][j]
    """
    table[row-1][column-1]=value
    return

def table_copy(table):
    """
    Outputs a coppied version of table.
    DON'T USE "table.copy()" TO COPY A TABLE!!
    """
    copy = []
    for row in table:
        copy.append(row.copy())
    return copy

def table_builder():
    """
    Asks user to make a table of size (row by column) and input spicific values 
    for the table. Returns the table.
    """
    table=[]
    #asks for size of table
    while True: 
        row = input("Enter how many rows: ")
        column = input("Enter how many columns: ")
        table=generate_table(int(row),int(column))
        print_table(table)
        okay = input("This okay? ('y' or 'n'): ")
        if okay == 'y':
            break           
    #asks user for initial values
    while True: 
        okay = input("Would you like to change an initial state? ('y' or 'n'): ")
        if okay == 'n':
            break            
        row = int(input("Enter a row to edit: ")) - 1
        column = int(input("Enter a column to edit: ")) - 1
        value = int(input("Enter a value: "))
        tablecopy = table_copy(table)
        change_table(tablecopy,row,column,value)
        table = tablecopy
        print_table(table)
    return table


#the main function
def U0():
    table=defult_table
    use_defult= input("Use defult table? ('y' or 'n'): ")
    
    if use_defult == 'n':
        table = table_builder()
 
    g = int(input("How many generations would you like?: "))
    n = 0
    while n <= g: #prints all the generations asks
        print("-- Generation {0} --".format(n))
        print_table(table)
        print()
        table = next_generation(table)
        n += 1
    input("End")
    return None



U0()