import os

def get_targets(path):
    '''
    Purpose: get_targets is used to search through a nested directory structure and return a list of all of 
    the .txt files in it that contain at least one line with exactly 2 lower case e's in it. Find the target .txt files 
    by calling the two_es function. When the inside of top level directory is more directories, go deeper using recursion
    until you reach .txt files for every possible path.
    Parameter(s): path - (string) the name of a directory. it is the top level directory to search through for subdirectories
    and .txt files. 
    Return Value: empty - it's a list containing strings that are the paths from the top level directory to the .txt files
    that meet the target requirement of the two_es function. There may be subdirectories in between the top level directory
    (path), and the .txt file targets.
    '''
    empty = []
    for file in os.listdir(path): 
        if os.path.isfile(path+'/'+file):
            if file.endswith('.txt'):
               fp = open(path+'/'+file)
               lines = fp.readlines()
              #  print('lines are', lines)
               fp.close()
               output = two_es(lines)
               if output == True:
                  empty.append(path+'/'+file)
               
               # print(output)
        else:
            empty += get_targets(path+'/'+file)
            


              #Go into a subdirectory
    return empty


def collatz(n):
    '''
    Purpose: Take in a positive integer n and returns the sum of numbers in the collatz sequence from n to 1, inclusive.
    if n is an even number divide it by 2 and if n is odd multiply n by 3 and add 1. Keep repeating the collatz sequence
    using the result of n = 3n+1 and n = n/2 until n = 1 when the recursion ends. 
    Parameter(s): n - an initial positive integer. Function keeps updating n through each recursion of collatz
    until n reaches 1. 
    Return Value: An integer - has no name. it's just the recursive sum of all n's used in the collatz equation. each n
    produced a new n until n = 1. When n = 1 return integer 1 to end the recursion.
    '''
   
    if n == 1:
      #funciton returns something (this is base case)
       return 1
    
    else:
       if n%2 == 0:
          div = n/2 
        #   count += 1
          return int(collatz(div)) + int((div * 2))
       else:
          prd = 3 * n + 1 
        #   count += 1 
          return int(collatz(prd)) + int(((prd -1 )/3))


def two_es(lines):
    '''
    Purpose: Function takes in a list of strings representing each line of a document and returns True if at least one of
    the strings in the list has exactly two lowercase e's
    Parameter(s): lines(a list) - a list of strings representing each line of document 
    Return Value: True- a boolean. Returns true if at least one line in the lines has exactly 2 e's. 
    False - returns boolean False if no line in the list has exactly 2 e's after running through each line.
    two_es(lines[1:]) - a recursive call to the two_es function, that slices off the first character to approach
    the empty list base case each time.
    '''
    if lines == []:
       
       return False 
    
    elif lines[0].count('e') == 2:
        return True
    # elif lines == []:
    #    return False   
    else:
       
       return two_es(lines[1:]) 
    





