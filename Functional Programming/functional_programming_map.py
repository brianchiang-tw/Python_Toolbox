def demo_map():

    num_list = list( range(1, 6) )

    ## Example_#1:
    # compute x^2 for each element
    result = list( map( lambda x:x**2, num_list) )

    # [1, 4, 9, 16, 25]
    print( result )



    ## Example_#2:
    # compute 3x + 1 for each element
    result = list( map( lambda x:3*x+1, num_list) )

    # [4, 7, 10, 13, 16]
    print( result )



    ## Example_#3:
    # compute sqrt(x) for each element
    result = list( map( lambda x:x**(0.5), num_list) )

    # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]
    print( result )



    str_list = ["apple", "banana", "cat", "dog", "elephant"]

    ## Example_#4:
    # Capitalize each word
    result = list( map( lambda x:x.capitalize(), str_list) )

    # ['Apple', 'Banana', 'Cat', 'Dog', 'Elephant']
    print( result )



    ## Example_#5:
    # Transfer each word into uppercase
    result = list( map( lambda x:x.upper(), str_list) )

    # ['APPLE', 'BANANA', 'CAT', 'DOG', 'ELEPHANT']
    print( result )



def demo_input_with_map():

    with open("input.txt", 'r') as f:

        input_content = f.readline()
        print("\ninput_content is:\n{}".format(input_content) )

        # read one line, separator is white space set
        # convert each token to integer and save in list
        num_list = list( map(int, input_content.split() ) )

        # [1, 2, 3, 4, 5]
        print( num_list )



        input_content = f.readline()
        print("\ninput_content is:\n{}".format(input_content) )

        # read one line, separator is ','
        # convert each token to integer and save in list
        num_list = list( map(int, input_content.split(sep = ',') ) )

        # [1, 2, 3, 4, 5]
        print( num_list )



        input_content = f.readline()
        print("\ninput_content is:\n{}".format(input_content) )

        # read one line, separator is white space 
        # convert each token to integer and save in list
        str_list = list( map(str, input_content.split(sep = ' ') ) )

        # ['apple', 'banana', 'cat', 'dog', 'elephant']
        print( str_list )




if __name__ == '__main__':

    demo_map()

    demo_input_with_map()

