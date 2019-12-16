def demo_filter():

    num_list = list( range(1, 11) )

    ## Example_#1:
    # pick even number
    result = list( filter( lambda x:x%2==0, num_list) )

    # [2, 4, 6, 8, 10]
    print( result )



    ## Example_#2:
    # pick odd number
    result = list( filter( lambda x:x%2==1, num_list) )

    # [1, 3, 5, 7, 9]
    print( result )



    ## Example_#3:
    # pick mutliplier of 3
    result = list( filter( lambda x:x%3==0, num_list) )

    # [3, 6, 9]
    print( result )



    str_list = ["Apple", "Banana", "cat", "dog", "elephant"]

    ## Example_#4:
    # pick word with word length is 3
    result = list( filter( lambda s: len(s)==3, str_list) )

    # ['cat', 'dog']
    print( result )



    ## Example_#4:
    # pick word with all character in lower case
    result = list( filter( lambda s: s.islower(), str_list) )

    # ['cat', 'dog', 'elephant']
    print( result )



if __name__ == '__main__':

    demo_filter()

