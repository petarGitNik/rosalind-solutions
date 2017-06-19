# Input: Two integers 'a' and 'b' each less than 1000
# Output: The integer corresponding to the square of the hypotenuse of the right
#         triangle whose legs have lengths 'a' and 'b'

# Check if the input number is integer
def is_integer(num):
    try:
        int(num)
    except ValueError:
        return False
    else:
        return True

# Alternative to above function
#def is_integer(num):
#    try:
#        int(s)
#        return True
#    except ValueError:
#        return False

# Calculate the square of the hypotenuse
def square_of_hypotenuse(a, b):
    return a ** 2 + b ** 2

# =================
# Start the program
# =================

print "Sides 'a' and 'b' should be less than 1000."
a = raw_input('Please enter side "a"> ')
b = raw_input('Please enter side "b"> ')

if is_integer(a) and is_integer(b):
    a = int(a)
    b = int(b)
    if a > 1000 or b > 1000:
        print "Sides of the triangle should not be greater than 1000"
    else:
        print "The square of the hypotenuse is equal to %d" % square_of_hypotenuse(a, b)
else:
    print "You should enter integer values!"
