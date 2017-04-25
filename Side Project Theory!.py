## Theory/Postulates:
# U_0 is a universe with 2 spatial Dimensions and one temporal Dimension. 
# The net energy is 0! Local positives and negatives can and will occur! 
# The initial state (U @ t = 0) is a random distribution of positive and 
# negative energy! 


# Every generation each cell distributes a portion of its current energy via 
# an energy distribution function E(t).

# Every generation some portion of a cells energy is converted to temperature 
# via the energy conversion function C(t). 


# Rule 42: 
# if a cell has energy value = to thresh hold value then it does not absorb
# nor distribute energy. (we can use this to make closed shapes, and tunnels)

# There exists two types of objects: 
# these objects exist as additional functions which only appear on certain cells
# these functions are distributed by the user when setting the initial state
#    "Absorber": This cell has a function A(t) which randomly chooses an 
#       adjacent cell and reduces its energy value, that energy is transfered
#       and classified in the original cell under Stored energy. This cell has
#       a finite lifetime i.e, the function will be deleted after n generations
#    "Transporter": This cell has a function B(t) which selects an adjacent cell 
#       and in the next generation the function is shifted to that cell. It has 
#       a finite number of "free steps". If the transporter encounters an 
#       absorber it will "latch" onto it. Then both cells will be transported
#       togethers. It will steal energy from the stored energy of the absorber
#       for every time they are transported together. The transporter will "die"
#       if it runs out of "free steps" and does not have an absorber to steal
#       from.

# ^^ Seems complicated but it provides a way for the simulation to be more
# dynamic and allow for energy to be moved in a different form other then 
# simply distributed. Also I am gonna start coming up with these mathematical 
# functions. Do you guys have any idea on how we can incorporate reproduction
# and random sub cell mutation [i.e the baby cells have a different A(t), B(t)]
