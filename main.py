"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)
    pass

def longest_run(mylist, key):
    ### TODO
    counter = 0
    longest_run = 0
    for i in mylist:
        if i == key:
            counter += 1
        else:
            if longest_run < counter:
                longest_run = counter
                counter = 0
        if longest_run < counter:
                longest_run = counter
                
    return longest_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' % (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def longest_run_recursive(mylist, key):
    return final_object(mylist, key).longest_size

def final_object(mylist, key):
    ### TODO
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    left_result = final_object(mylist[:len(mylist)//2], key)
    right_result = final_object(mylist[len(mylist)//2:], key)

    return combine_function(left_result, right_result)

def combine_function(left_result, right_result):
    adjacent_size = left_result.right_size + right_result.left_size
    if (left_result.is_entire_range and right_result.is_entire_range):

        new_left_size = left_result.longest_size + right_result.longest_size
        new_right_size = left_result.longest_size + right_result.longest_size
        new_longest_size = left_result.longest_size + right_result.longest_size
        new_is_entire_range = True

        return Result(new_left_size, new_right_size, new_longest_size, new_is_entire_range)

    elif (adjacent_size > left_result.longest_size or adjacent_size > right_result.longest_size):

        if (left_result.is_entire_range):
            new_left_size = left_result.longest_size + right_result.left_size
            new_right_size = right_result.right_size
        elif (right_result.is_entire_range):
            new_left_size = left_result.left_size
            new_right_size = right_result.longest_size + left_result.right_size
        else:
            new_left_size = left_result.left_size
            new_right_size = right_result.right_size

        new_longest_size = adjacent_size
        new_is_entire_range = False

        return Result(new_left_size, new_right_size, new_longest_size, new_is_entire_range)

    else:
        if right_result.longest_size > left_result.longest_size:

            new_left_size = left_result.left_size
            new_right_size = right_result.right_size
            new_longest_size = right_result.longest_size
            new_is_entire_range = False

        else:

            new_left_size = left_result.left_size
            new_right_size = right_result.right_size
            new_longest_size = left_result.longest_size
            new_is_entire_range = False

        return Result(new_left_size, new_right_size, new_longest_size, new_is_entire_range)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run_recursive([2,12,12,8,12,12,12,12], 12) == 3

print(longest_run_recursive([0], 12))
