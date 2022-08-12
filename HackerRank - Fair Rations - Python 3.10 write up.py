##    https://www.hackerrank.com/challenges/fair-rations/problem
##
##    You are the benevolent ruler of Rankhacker Castle, and today you're
##    distributing bread. Your subjects are in a line, and some of them
##    already have some loaves. Times are hard and your castle's food stocks
##    are dwindling, so you must distribute as few loaves as possible
##    according to the following rules:
##
##        1. Every time you give a loaf of bread to some person, you must
##        also give a loaf of bread to the person immediately in front of or
##        behind them in the line.
##        2. After all the bread is distributed, each person must have an even
##        number of loaves.
##
##    Given the number of loaves already held by each citizen, find and
##    print the minimum number of loaves you must distribute to satisfy
##    the two rules above. If this is not possible, print NO.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in B

#   Idea:
#       We simply check each person in line one at a time.  If they have
#       an even amount of bread then we do nothing, if they have an odd
#       amount of bread then we give them a single piece and the person
#       behind them in line a single piece.  If we get to the last person
#       in line and they have an odd amount of bread then we know it is not
#       possible, because the person in front of them already has an even
#       amount of bread and there is no person behind them.  If we get to
#       the last person in line and they have an even amount of bread then
#       we simply return the total amount of bread handed out.

#   Algo:
#       1. Initiate a variable to store the total number of loaves given out => O(1)
#       2. Iterate through the provided list B => O(|B|)
#           A. Check if current value is odd => O(1)
#               If True:
#                   Increment current value => O(1)
#                   Increment next value => O(1)
#                   Increment loaves given => O(1)
#       3. Check parity of last value of B => O(1)
#           If odd:
#               return 'NO' => O(1)
#           else:
#               return loaves given as a string => O(1)

def fairRations(B):
    
    loaves_given = 0
    
    for index in range(len(B) - 1):
        
        if B[index] % 2 == 1:
            
            B[index] += 1
            B[index + 1] += 1
            loaves_given += 2
            
    if B[-1] % 2 == 1:
        
        return 'NO'
    
    else:
        
        return str(loaves_given)
