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
    res = recursion(mylist,key)
    return res.longest_size
    ### TODO
def recursion(mylist,key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0,0,0,False)
    left = recursion(mylist[0 :len(mylist)//2], key)
    right = recursion(mylist[len(mylist)//2: ], key)
    print(left,right)
    print(mylist[ :len(mylist)//2],mylist[len(mylist)//2: ])
    if left.is_entire_range and right.is_entire_range:
        temp = left.right_size + right.left_size
        return Result(temp, temp, temp, True)

    elif left.is_entire_range:
        if right.left_size > 0:
            temp = left.right_size + right.left_size
            return Result(temp,right.right_size,temp,False)
        else:
            return Result(left.left_size,right.right_size,max(left.left_size,right.longest_size),False)

    elif right.is_entire_range:
        if left.right_size > 0:
            temp = left.right_size + right.left_size
            return Result(left.left_size,temp,temp,False)
        else:
            return Result(left.left_size,right.right_size,max(right.right_size,left.longest_size),False)

    else:
        if left.right_size > 0 and right.left_size > 0:
            temp = left.right_size + right.left_size
            return Result(left.left_size,right.right_size,max(left.longest_size,right.longest_size,temp),False)
        elif left.right_size >0:
            return Result(left.left_size,right.right_size,max(left.longest_size,right.longest_size),False)
        elif right.left_size >0:
            return Result(left.left_size,right.right_size,max(left.longest_size,right.longest_size),False)
        elif left.left_size >0:
            return Result(left.left_size,0,max(left.longest_size,right.longest_size),False)
        elif right.right_size>0:
            return Result(0,right.right_size,max(left.longest_size,right.longest_size),False)
        else:
            return Result(0,0,0,False)



## Feel free to add your own tests here.
def test_longest_run():
    return longest_run([2,12,12,8,12,12,12,0,12,1], 999)

print(test_longest_run())
