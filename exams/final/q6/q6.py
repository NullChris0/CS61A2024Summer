email = 'example_key'

def compress(lst1, lst2):
    """
    Write a function compress that takes in two lists of positive integers,
        lst1 and lst2, and determines if lst1 can be compressed into lst2.

    A compression is when two adjacent elements in the list are either addded or
        subtracted from each other to form one single new element.

    For example, for the list [1,2,1] the first compression could result in either

        [3, 1] (adding)
        [-1, 1] (subtraction)

    >>>> compress([1,1,1], [3])
    True
    >>>> compress([1,1,1], [2])
    False
    >>>> compress([1,1,1], [1])
    True
    >>>> compress([1,2,3], [1,5])
    True
    >>>> compress([1,2,3], [2])
    True
    >>>> compress([], [1,2,3])
    False
    >>>> compress([1,2,3], [])
    False
    >>>> compress([], [])
    True
    >>>> compress([1,4,2,8,3,9,4], [31])
    True
    >>>> compress([1,4,2,8,3,9,4], [3,5,5])
    True
    """
    if ______ == ______:
        return ______
    elif ______ or ______:
        return ______
    compress_add = ______
    compress_sub = ______
    compress_eq = ______ and ______
    return ______

# ORIGINAL SKELETON FOLLOWS

# def compress(lst1, lst2):
#     """
#     Write a function compress that takes in two lists of positive integers,
#         lst1 and lst2, and determines if lst1 can be compressed into lst2.

#     A compression is when two adjacent elements in the list are either addded or
#         subtracted from each other to form one single new element.

#     For example, for the list [1,2,1] the first compression could result in either

#         [3, 1] (adding)
#         [-1, 1] (subtraction)

#     >>>> compress([1,1,1], [3])
#     True
#     >>>> compress([1,1,1], [2])
#     False
#     >>>> compress([1,1,1], [1])
#     True
#     >>>> compress([1,2,3], [1,5])
#     True
#     >>>> compress([1,2,3], [2])
#     True
#     >>>> compress([], [1,2,3])
#     False
#     >>>> compress([1,2,3], [])
#     False
#     >>>> compress([], [])
#     True
#     >>>> compress([1,4,2,8,3,9,4], [31])
#     True
#     >>>> compress([1,4,2,8,3,9,4], [3,5,5])
#     True
#     """
#     if ______ == ______:
#         return ______
#     elif ______ or ______:
#         return ______
#     compress_add = ______
#     compress_sub = ______
#     compress_eq = ______ and ______
#     return ______
