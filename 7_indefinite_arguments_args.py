def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, 'ordered a', tea_type, 'tea')
    for arg in args:
        print('  -Add:', arg)
    for key, value in kwargs.item():
        print('  -Add',key, ':', value)

    # print('args contains:', args)

tea_order('alice', 'chamomile')
tea_order('bob', 'black', milk='oat')
tea_order('Tony', 'black', 'oat', sweetner='honey')


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    total = 0
    for num in args:
        total += num ** 2
    return total
print(sum_squares(1,2,3))
print(sum_squares(4,5,6))

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0
    for num in args:
        total += abs(num)
    return total
print(absolute_sum(-1,-2,-3))
print(absolute_sum(-10,-20,-30))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(*args):
    name = args(0)
    sum_numbers = sum(args(1,1))
    return f'{name} "the sum of your numbers is" {sum_numbers}'
print(personal_numbers(alice, 1,2,3))
# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"