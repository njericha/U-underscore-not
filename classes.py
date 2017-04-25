## Side Project: 

#Random number generator: 
# import random 
# random.randrange(a, b) this outputs an integer between [a, b) 

import random


##----defining classes here----##

class cell:
    '''
    An element containing *two* fields, Energy (float) and Temperature (float).
    Energy can be used for work and some gets converted to Temperature.
    Temperature is thermal energy which radiates to neighbouring cells.
    '''
    def __init__(self,En,Te):
        self.energy=En
        self.temperature=Te
    def __repr__(self):
        first = round(self.energy,dtrt)
        second = round(self.temperature,dtrt)
        if dtrt == 0:
            first = int(first)
            second = int(second)
        first = str(first)
        second = str(second)
            
        if first == "0":
            first = ""
        if second == "0":
            second = ""        
        while len(first) < spacing:
            first = " " + first
        while len(second) < spacing:
            second = " " + second
        
        return "("+first+"|"+second+")"
    
    def copy(self):
        return cell(self.energy,self.temperature)
    

class grid:
    '''
    A "list of lists" of size row by column containing elements from the class
    "cell". Starts out blank (filled with zero cells).
    '''
    def __init__(self,m,n):
        table = []
        for i in range(m):
            rowC = []
            for j in range(n):
                rowC.append(cell(0,0))
            table.append(rowC)
        self.full=table
    
    def __repr__(self):
        to_print=""
        for row in self.full:
            for cell in row:
                to_print += cell.__repr__() + " "
            to_print = to_print[:-1] + "\n"
        return to_print[:-1]
    
    def copy(self):
        '''
        returns a copied verson of the grid
        '''       
        grid_copy = grid(len(self.full),len(self.full[0]))
        for i in range(1,len(self.full)+1):
            for j in range(1,len(self.full[0])+1):
                grid_copy.changeCell(i,j,self.cell(i,j))
        return grid_copy
    
    def changeE(self,i,j,value=0):
        '''
        takes a row (i), column (j), and value (zero by defult if no value is given)
        and changes the grid energy at the point row/column to value
        '''
        edit_row = (i - 1) % len(self.full)
        edit_column = (j - 1) % len(self.full[0])
        self.full[edit_row][edit_column].energy=value
        
    def changeT(self,i,j,value=0):
        '''
        takes a row (i), column (j), and value (zero by defult if no value is given)
        and changes the grid temperature at the point row/column to value
        '''
        edit_row = (i - 1) % len(self.full)
        edit_column = (j - 1) % len(self.full[0])
        self.full[edit_row][edit_column].temperature=value
        
    def changeCell(self,i,j,cell=cell(0,0)):
        '''
        takes a row (i), column (j), and a cell (cell(0,0) by defult if no
        value is given) and mutates grid to a new grid with a copy of that cell
        (this won't alias the cell)
        '''       
        self.changeT(i,j,cell.temperature)
        self.changeE(i,j,cell.energy)
    
    def cell(self,i,j):
        '''
        returns the cell of grid at row i and column j
        '''
        call_row = (i - 1) % len(self.full)
        call_column = (j - 1) % len(self.full[0])        
        return self.full[call_row][call_column]
        
    def nextI(self):
        '''
        mutates the grid to the next generation (and returns it)
        '''
        next_grid = self.copy()
        for i in range(1,len(next_grid.full)+1):
            for j in range(1,len(next_grid.full[0])+1): 
                #rules go in here ## <<-----------           
                cell = self.cell(i,j)
                if not rule42(cell):               
                    new_value = temp_disp(next_grid,i,j,self,cell)
                else:
                    pass
        return next_grid
    
    def store(self,array):
        '''
        Mutates grid to have the array (lists of lists) given. Make sure the 
        lists of lists only contain cell(e,t) for energy 'e' and temperature 't'
        and all lists in array are the length
        '''
        self.full = array


##----rules toggle go here----##

rule_temp_disp = True
rule_threshold = True

##----constents go in here----##

dtrt = 0 #<<-- number of decimals to round the printed values,
         #     0 means int (ex. 81.26 => 81)
         #     1 mean one decimal (ex. 81.26 => 81.3)

spacing = 3 #<<-- number of spaces to display blank cells in grid 
            #     (must be an int >= 0 )

threshold = 42 #<<-- must be an int

defult_U = grid(7,7)
defult_U.changeT(4,4,999)
defult_U.changeE(3,3,42)
defult_U.changeE(4,3,42)
defult_U.changeE(3,4,42)
defult_U.changeE(5,3,42)




##------rules go in here------##

#example of a rule that lowers a value if it is greater than 1
##def rule1(table,row,column,value):
    ##if value > 0:
        ##table[row][column] = value - 1

def temp_disp(new,row,column,old,value):
    """
    radiates an 8th of a cells tempurature (as if by dispersion) to adjacent cells
    (unless it's energy equals threshold) 
    
    """
    if not rule_temp_disp: #<- checks if this rule is turned on
        return value
    new_value = 0
    len_row = len(old.full)
    len_column = len(old.full[0])
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if [i,j] != [0,0]:
                edit_row = row + i
                edit_column = column + j
                neighbour = old.cell(edit_row,edit_column)
                if rule42(neighbour): #<-rule42 check needed here
                    new_value += old.cell(row,column).temperature
                else:
                    new_value += neighbour.temperature                    
    new.changeT(row,column, new_value / 8)
    return new_value / 8

def rule42(cell):
    """
    if a cell has an energy of integer of threshold, it will not radiate
    temperature and ajacent cells will get an 8th of it's energy back
    (i.e. temperature gets "bounced back" or "insulated")
    """   
    if rule_threshold and round(cell.energy) == threshold:
        return True
    else:
        return False


##--helper functions go here---##


def grid_builder():
    """
    Asks user to make a grid of size (row by column) and input spicific values 
    for the grid. Returns the grid.
    """
    #asks for size of grid
    while True: 
        row = input("Enter how many rows: ")
        column = input("Enter how many columns: ")
        U=grid(int(row),int(column))
        print(U)
        okay = input("This okay? ('y' or 'n'): ")
        print("\n")
        if okay == 'y':
            break           
    #asks user for initial values
    while True: 
        okay = input("Would you like to change an initial state? ('y' or 'n'): ")
        if okay == 'n':
            break            
        row = int(input("Enter a row to edit (first row is 1): "))
        column = int(input("Enter a column to edit (first column is 1): "))
        value = int(input("Enter a value: "))
        TE = input("Is this a temperature (t) or energy (e)?: ")
        if TE == "t":
            U.changeT(row,column,value)
        elif TE == "e":
            U.changeE(row,column,value)
        print(U)
    return U


#the main function
def U0():
    U=defult_U
    use_defult= input("Use defult grid? ('y' or 'n'): ")
    
    if use_defult == 'n':
        U = grid_builder()
        
    else:
        print("<loaded defult grid>")
        print(U,"\n")
 
    g = int(input("How many generations would you like?: "))
    n = 0
    while n <= g: #prints all the generations asks
        print("-- Generation {0} --".format(n))
        print(U,"\n")
        U = U.nextI()
        n += 1
    input("End")
    return None

U0()