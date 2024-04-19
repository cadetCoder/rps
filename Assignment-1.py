##########
# TASK 1 #
##########

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = "22087552"

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"
#
# Please leave the next line unchanged
task = 'task1'
# ----------------------------------------------------------------------------------------------------------------------------
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of the
# functions below, each of which currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# Do not change the names or parameters of any of these functions
# Make sure you read the function descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a test plan and code to test the functions
# and display the results of the tests
#
# To run the tests type  run_tests()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

##########################
# Function 1: (2 marks)
##########################
# Function name: grade_mark
# Parameter:     mark
# Returns:       grade
# Pre-condition:
#   mark is a whole number
# Post-condition:
#   grade is a string
#   when mark is 0, grade is 'F3'
#   when mark is greater than 0 and less than 20, grade is 'F2'
#   when mark is between 20 and 39 inclusive, grade is 'F1'
#   when mark is between 40 and 49 inclusive, grade is 'P4'
#   when mark is between 50 and 59 inclusive, grade is 'P3'
#   when mark is between 60 and 69 inclusive, grade is 'P2'
#   when mark is between 70 and 79 inclusive, grade is 'P1'
#   when mark is between 80 and 100 inclusive, grade is 'P0'
#   when mark has any other value, grade is 'invalid'

def grade_mark (mark) :
    # Insert function body to replace code stub
        if mark == 0:
          return 'F3'
        elif 0 < mark < 20:
            return 'F2'
        elif 20 <= mark <= 39:
            return 'F1'
        elif 40 <= mark <= 49:
            return 'P4'
        elif 50 <= mark <= 59:
            return 'P3'
        elif 60 <= mark <= 69:
            return 'P2'
        elif 70 <= mark <= 79:
            return 'P1'
        elif 80 <= mark <= 100:
            return 'P0'
        else:
          return 'invalid'



##########################
# Function 2 (2 marks)
##########################
# Function name: stud_marks
# Parameters:    modules, marks
# Returns:       A list of pairs
# Pre-condition:
#  modules is a list of strings, each of which represents
#  the name of a module taken by the student
#  marks is a list of numbers, each of which represents a
#  mark obtained for a module, so that marks[i] is the mark
#  for modules[i], for every natural number, i < len[marks]
# Post-condition:
#  Each pair in the returned list contains the name of a
#  module and the the mark for that module
#  module marks are in the same order as in the lists passed
#  in as parameters
# Example:
#  mods = ['cs101','cs102','mat110']
#  mks = [99,56,54]
#  stud_marks(mods,mks)
#     returns
#   [('cs101',99), ('cs102',56), ('mat110',54)]
#

def stud_marks (modules,marks) :
    # Insert function body to replace code stub
    result = []
    for i in range(len(modules)):
        result.append((modules[i], marks[i]))

    return result    # code stub




##########################
# Function 3 (3 marks)
##########################
# Function name: prime_indexes
# Parameter:     intlist
# Returns:       A pair of lists (P,N)
# Pre-condition:
#   intlist is a list of integers
# Post-condition:
#   P is a list containing the indexes of all the prime
#   numbers in intlist
#   If there are no prime numbers in intlist P is
#   an empty list
#   N is a list containing the indexes of all the non-prime
#   numbers in intlist
#   If there are no non-prime numbers in intlist N is
#   an empty list


# YOU ARE REQUIRED TO USE the function is_prime (defined below)
# to determine whether or not the numbers in intlist are primes
# This function works correctly: DO NOT CHANGE IT
# It is for use in the definition
# of the function prime_indexes
# Parameter: n
# Returns:   A Boolean value, B
# Pre-condition:
#   n is an integer
# Post-condition:
#   B is True if n is a prime number
#   B is False otherwise
def is_prime (n) :
    if n <= 1 :
        return False
    else :
        m = int(n**0.5) + 1
        for i in range(2,m) :
            if n % i == 0 :
                return False
        return True


def prime_indexes (intlist) :
    # See specifiction above
    # Insert function body to replace code stub

    primes = []
    non_primes = []
    for i in range(len(intlist)):
        if is_prime(intlist[i]):
            primes.append(i)
        else:
            non_primes.append(i)

    return primes, non_primes



##########################
# Function 4 (3 marks)
##########################
# A function that mimics the encoding of bit-strings for transmission
# via a data link
##########################
# Function name: send
# Parameter:     bit_str
# Returns:       A character string, signal_str
# Pre-condition:
#   bit_str is a character string
#   bit_str contains a sequence of '0' and '1' characters each of
#   which represents a single bit in a bit-string.
#   For example
#   The character string '0010111' represents the bit-string 0010111
# Post-condition:
#   signal_str contains a sequence of '*' (star) and '_' (underscore)
#   characters to represent the sequence of high and low voltages that
#   will be used to send bit_str over the data link 
#   signal_str is derived from bit_str as follows
#     Each signal_str must start with the sequence '**' (two stars)      
#     and end with the sequence '__' (two underscores)
#     In between the start and end indicators the sequence of bits from
#     bit_string are encoded in signal_str as follows
#       every '0' from bit_str is encoded as '*_*'
#       every '1' from bit_str is encoded as '_*_'
#  
# For example
# send ('')    returns '**__'
# send ('0')   returns '***_*__'
# send ('1')   returns '**_*___'
# send ('00')  returns '***_**_*__'
# send ('001') returns '***_**_*_*___'
# send ('100') returns '**_*_*_**_*__'
# send ('110') returns '**_*__*_*_*__'
# and so on, so that
# send ('0010111') returns '***_**_*_*_*_*_*__*__*___'

def send (bit_str) :
    # Insert function body to replace code stub
    signal_str = '**'
    for b in bit_str:
        if b == '0':
            signal_str += '*_*'
        elif b == '1':
            signal_str += '_*_'
    signal_str += '__'

    return signal_str




##########################
# Function 5 (4 marks)
##########################
# A function that extracts a bit-string from a sequence of signals
# received over a data link
# The function is effectively the inverse of send (see function 4)
# so that after executing the following sequence of instructions
#   inbitstring  = '0010'
#   signalseq    = send(inbitstring)
#   outbitstring = receive(signalseq)
# signalseq is  '***_**_*_*_*_*__'  and outbitstring is  '0010'
#
# If the sequence of signals received could not have been generated
# by a correctly implemented send function, the receive function
# should return "error", to indicate a data transmission error
#
##########################
# Function name: receive
# Parameter:     signal_str
# Returns:       A character string, bit_str
# Pre-condition:
#   signal_str contains a sequence of '*' (star) and '_' (underscore)
#   characters to represent the sequence of high and low voltages that
#   were received over the data link 
#   Any sequence of high and low voltages may be received, so the
#   function must return a meaningful result for any sequence of '*'
#   and '_' characters
#
# Post-condition:
#   bit_str is a character string
#
#   If signal_str represents a valid sequence of signals
#      bit_str contains a sequence of '0' and '1' characters each of
#      which represents a single bit in a bit-string
#   Otherwise
#      the function returns "error"
#
#   To be valid a signal_str must start with the sequence '**' (two stars)
#   and end with the sequence '__' (two underscores)
#   In between the start and end indicators a valid signal_str must
#   contain a series of three-character segments
#      the sequence '*_*' is decoded as a '0'
#      the sequence '_*_' is decoded as a '1'
#  
# For example
# receive ('**__')          returns ''
# receive ('*_*')           returns 'error'
# receive ('***_*__')       returns '0'
# receive ('__*_***')       returns 'error'
# receive ('**_*___')       returns '1'
# receive ('***_*___')      returns 'error'
# receive ('***_**_*__')    returns '00'
# receive ('***_**_*_*___') returns '001'
# receive ('**_*_*_**_*__') returns '100'
# receive ('**_*__*_*_*__') returns '110'
# and so on, so that
# receive ('***_**_*_*_*_*_*__*__*___') returns '0010111'

def receive (signal_str) :
    # Insert function body to replace code stub
    bit_str = signal_str[2:-2]
    if len(bit_str) % 3 != 0:
        return 'error'
    for i in range(0, len(bit_str), 3):
        if bit_str[i:i+3] not in ['*_*', '_*_']:
            return 'error'
    return bit_str.replace('*_*', '0').replace('_*_', '1')




##########################
# Function 6 (3 marks)
##########################
# A function that determines whether or not all elements in a list
# are valid assignment marks

# Function name: valid_marks
# Parameters:    thelist,min_mark,max_mark
# Returns:       A truth value
# Pre-condition:
#   thelist is a list
#   min_mark and max_mark are both non-negative integers
#   and max_mark > min_mark
# Post-condition:
#   Returns True when all elements of thelist are integers
#   between min_mark and max_mark inclusive
#   Returns False when an element of thelist is not an
#   integer or is not in the range min_mark..max_mark
#
# NOTE that the function isinstance can be used to check whether
# a data item is an integer.
#   isinstance(i,int)
# returns True if i is an integer and False if it is not

def valid_marks (thelist,min_mark,max_mark) :
    # Insert function body to replace code stub
    for mark in thelist:
        if not isinstance(mark, int) or not min_mark <= mark <= max_mark:
            return False
            
    return True     # code stub



##########################
# Function 7 (3 marks)    USE RECURSION
##########################
# A function that determines whether or not a list of students is
# arranged in ascending order by total mark

# You are required to USE RECURSION when implementing this function

# Parameter:  stud_list
# Returns:    a truth value
# Pre-condition:
#   Each element in stud_list is a triple, (name,total,average) representing
#   a student's name, total mark and average mark
# Post-condition:
#   returns True when the elements in stud_list are in ascending order
#   of total mark
#   returns False when they are not
# NOTE: A stud_list with less than two entries is in order

def in_order (stud_list) :
    # Insert function body to replace code stub
    for i in range(len(stud_list) - 1):
        if stud_list[i][1] > stud_list[i+1][1]:
            return False

    return True



# ----------------------------------------------------------------------------------------------------------------------------
# Do not change any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------

###########################################################################

#                           TEST PLAN

############################################################################

test_plan = dict ()


fn = "grade_mark"
test_plan [fn] = dict()
test_plan [fn] [1] = [[0],'F3']
test_plan [fn] [2] = [[-9],'invalid']
test_plan [fn] [3] = [[93],'P0']
test_plan [fn] [4] = [[40],'P4']
test_plan [fn] [5] = [[59],'P3']
test_plan [fn] [6] = [[38],'F1']


fn = "stud_marks"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[],[]],[]]
test_plan [fn] [2] = [[['com101'],[8]],[('com101',8)]]
test_plan [fn] [3] = [[['com101','com125'],[100,86]],[('com101',100),('com125',86)]]
test_plan [fn] [4] = [[['com102','bus101','mat110'],[52,73,35]],[('com102',52),('bus101',73),('mat110',35)]]
test_plan [fn] [5] = [[['bus120','com202','mat110','com127','psy100'],[33,78,43,65,23]],[('bus120',33),('com202',78),('mat110',43),('com127',65),('psy100',23)]]


fn = "prime_indexes"
test_plan [fn] = dict()
test_plan [fn] [1] = [[list()],([],[])]
test_plan [fn] [2] = [[[1,3,5,6,8]],([1,2],[0,3,4])]
test_plan [fn] [3] = [[[4,6,8]],([],[0,1,2])]
test_plan [fn] [4] = [[[5,7,11,13]],([0,1,2,3],[])]


fn = "send"
test_plan [fn] = dict()
test_plan [fn] [1] = [[''],'**__']
test_plan [fn] [2] = [['1'],'**_*___']
test_plan [fn] [3] = [['01'],'***_*_*___']
test_plan [fn] [4] = [['0011'],'***_**_*_*__*___']
test_plan [fn] [5] = [['11100110'],'**_*__*__*_*_**_*_*__*_*_*__']


fn = "receive"
test_plan [fn] = dict()
test_plan [fn] [1] = [['**__'],'']
test_plan [fn] [2] = [['**_*___'],'1']
test_plan [fn] [3] = [['***_*_*___'],'01']
test_plan [fn] [4] = [['***_**_*_*__*___'],'0011']
test_plan [fn] [5] = [['**_*__*__*_*_**_*_*__*_*_*__'],'11100110']
test_plan [fn] [6] = [[''],'error']
test_plan [fn] [7] = [['*_**_*'],'error']


fn = "valid_marks"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[],0,100],True]
test_plan [fn] [2] = [[[1,'a'],0,100],False]
test_plan [fn] [3] = [[['0',2],0,50],False]
test_plan [fn] [4] = [[[14,36.5],10,25],False]
test_plan [fn] [5] = [[[12,1,15],0,40],True]
test_plan [fn] [6] = [[[1,2,3,4,5,6,7,8,9,10,9,8,7],0,10],True]


fn = "in_order"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[]],True]
test_plan [fn] [2] = [[[('fred',80,20.0)]],True]
test_plan [fn] [3] = [[[('fred',100,25.0),('bill',86,86.0)]],False]
test_plan [fn] [4] = [[[('bill',45,45.0),('fred',86,43.0)]],True]
test_plan [fn] [5] = [[[('joe',99,33.0),('fred',78,39.0),('rose',43,21.5),('misty',66,11.0),('bill',23,23.0)]],False]
test_plan [fn] [6] = [[[('buster',33,33.0),('freda',43,21.5),('janet',65,13.0),('pete',72,12.0),('sam',200,50.0)]],True]
test_plan [fn] [7] = [[[('pete', 72, 12.0), ('janet', 65, 13.0), ('freda', 43, 21.5), ('buster', 33, 33.0), ('sam', 200, 50.0)]],False]



###########################################################################

#                           TEST DRIVER

############################################################################

def tester (ms) :
    results = dict()
    totalmark = 0
    for funcname in ms :
        results[funcname] = dict()
        totalfunc = 0
        tests = ms[funcname].copy()
        for case in tests :
            test      = tests [case]
            args      = test[0]
            arg0      = args[0]
            if isinstance (arg0,str) :
                arg0 = "'" + arg0 + "'"
            else :
                arg0 = str(args[0])
            strargs = "(" + arg0
            for arg in args[1:] :
                if isinstance (arg,str) :
                    arg = "'" + arg + "'"
                else :
                    arg = str(arg)
                strargs = strargs + "," + arg
            strargs   = strargs + ")"
            target    = test[1]
            if isinstance (target,str) :
                strtarget = "'" + target + "'"
            else :
                strtarget = str(target)
            try :
                call = funcname + strargs
                actual = eval(call)
                if isinstance (actual,str) :
                    stractual = "'" + actual + "'"
                else :
                    stractual = str(actual)

            except NameError :
                result = "Name error"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except RecursionError :
                result = "Recursion error (too many recursive calls)"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except :
                result = funcname + " crashed"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue

            if type(actual) != type(target) :
                result = "wrong type returned"
                
            else :
                if target == actual :
                    result = "PASS"
                else :
                    result = "FAIL"

            results[funcname][case] = [strargs,strtarget,stractual,result]

    return results



def DisplayTestResults (results) :    
    display = "Test results\n"
    display += "Each function listed in the order tested\n\n"
    
    for fn in results :
        display += "\nTesting " + fn + "\n=========================="
        testres = results[fn]
        for test in testres :
            t = testres[test]
            #display += "\nTest " + str(test)
            display += "\nParameters:    " + t[0]
            display += "\nShould return: " + t[1]
            display += "\nActual return: " + t[2]
            display += "\nTest result:   " + t[3]
            display += "\n"
        display += "\n"
    return display




def run_tests () :
    global test_plan
    
    results = tester(test_plan)
    message = DisplayTestResults (results)
    print (message)


if input ("Run tests (y/n)? ") in ['y','Y'] :
    run_tests()
