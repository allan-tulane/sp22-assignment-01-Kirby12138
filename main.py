"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

# The foo function calculates the x-th Fibonacci sequence.
# It consists of the base case and recursive steps.
# The base cases are when x <= 1, then return the value of x
# What the recursive step does is simply add (x-1)-th Fibonacci sequence and (x-2)th Fibonacci Sequence
def foo(x):
    if x <= 1:
        return x
    return foo(x-1) + foo(x-2)


def longest_run(mylist, key):
    longest = -float("inf")
    cnt = 0
    for i in range(len(mylist)):
        if i == 0 and mylist[i] == key:
            cnt = 1
        if mylist[i] == mylist[i-1] and mylist[i] == key:
            cnt += 1
        elif mylist[i] == key:
            cnt = 1
        longest = max(cnt,longest)

    return longest
# work = O(n)
# span = O(n)
        


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    if len(mylist) == 1 and mylist[0] == key:
        return Result(1, 1, 1, True)
    else:
        return Result(0,0,0,False)
    left = longest_run_recursive(mylist[ :len(mylist)//2], key)
    right = longest_run_recursive(mylist[len(mylist)//2: ], key)
    return 
    
        

## Feel free to add your own tests here.
def test_longest_run():
    return longest_run([2,12,12,8,12,12,12,0,12,1,1], 12)

print(foo(10))
print(test_longest_run())

