import random
import sys


def solve_for_system(x, y):
  # test solutions for possible results in a tuple data structure
  return (
    x + (2 * y) == 2,
    -x + y == 1
  )

def generate_rand_pair(lower, upper):
  rand_x = 1
  rand_y = -1
  while (rand_x >= rand_y):
    rand_x = random.randint(lower, upper)
    rand_y = random.randint(lower, upper)
  return (rand_x, rand_y)

if __name__ == '__main__':
  # use sys.argv to get list of all inputs ['main.py', x, y]
  lower_bound = float(sys.argv[1]) # for random number generation
  upper_bound = float(sys.argv[2]) # ditto
  rands = generate_rand_pair(lower_bound, upper_bound) # generate random pair of inputs
  x = rands[0]
  y = rands[1]
  print('Solving for...\nx: ' + str(x) + '\ny: ' + str(y) + '\n') # log next problem set
  
  result = solve_for_system(x, y) # get new result tuple
  print('Testing for x: ' + str(result[0]) + ' and y: ' + str(result[0])) # log test variables for info
  while (result[0] != True or result[1] != True): # loop until termination, note: some systems have no solutions... (depends on output of solve_for_system(x, y))
    rands = generate_rand_pair(lower_bound, upper_bound) # get pair of random ints in bounds
    print('Attempting to find solution to system, testing:\n' + 'x: ' + str(x) + '\ny: ' + str(y) + '\n') # log next problem set
    x = rands[0]
    y = rands[1] # assign x and y for simplicity
    result = solve_for_system(x, y) # get new result tuple
  # loop terminated, solution discovered
  print('Solution discovered!\n' + 'x: ' + str(x) + '\ny: ' + str(y) + '\n')
  print('Solution Tuple -> ' + str(result))
  
  print( str(x) + " + " + "(2 * " + str(y) + ") = " + str(x + (2 * y)) )
  
  print(str(-x) + ' + ' + str(y) + ' = ' + str(-x + y))