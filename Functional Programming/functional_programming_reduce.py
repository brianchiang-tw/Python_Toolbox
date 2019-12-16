from functools import reduce

# remember to import reduce from functools
def demo_reduce():

    num_list = list( range(1, 11) )

    ## Example_#1:
    # compute summation over list
    result = reduce( lambda x, s: x+s, num_list) 

    # 55
    print( result )



    ## Example_#2:
    # compute product over list
    result = reduce( lambda x, p: x*p, num_list)

    # 3628800
    print( result )



    str_list = ["Apple", "Banana", "cat", "dog", "elephant"]

    ## Example_#3:
    # concatenate each word, separated by one dash
    result = reduce( lambda s, r: s + "-" + r, str_list)

    # Apple-Banana-cat-dog-elephant
    print( result )



if __name__ == '__main__':
    
    demo_reduce()