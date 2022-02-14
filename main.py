"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
        return x
    else:
        return foo(x-1) +foo(x-2)

def longest_run(mylist, key):
    count = 0
    max = 0
    for i in mylist:
        if i == key:
            count = count + 1
            if count >= max:
                max = count
        else:
            count = 0
    return max


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
    
    
def longest_run_recursive(mylist,key):
    if len(mylist) == 1:
        if mylist[0] == key:
            result = Result(0, 0, 1, True)
            return result
        result = Result(0, 0, 0, False)
        return result

    mid = len(mylist)//2
    left = longest_run_recursive(mylist[0:mid],key)
    right = longest_run_recursive(mylist[mid:],key)
  
    leftleft = left.left_size
    rightright = right.right_size
    longest = 0

    if left.is_entire_range:
        leftleft = mid
    if right.is_entire_range:
        rightright = len(mylist)-mid

    if left.is_entire_range and right.is_entire_range:
        result = Result(leftleft, rightright, len(mylist), True)
        return result

    if right.left_size > 0 and left.right_size > 0 or right.is_entire_range and left.right_size >0 or left.is_entire_range and right.left_size >0:
        longest = left.longest_size + right.longest_size
    else:
        longest = max(right.longest_size, left.longest_size)
  
    result = Result(leftleft, rightright, longest, False)
    return result

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

print(longest_run_recursive([0,2,4,2,2,2,2,0,2,2], 2))

