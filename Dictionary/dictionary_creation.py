from collections import Counter

def demo_dictionary_creation():

    # Create empty dictionary

    # Method_#1 : using braces
    dict_domain = {}

    # expected output:
    # {}
    print( dict_domain )
    dict_domain.clear()



    # Method_#2 : using dict() constructor
    dict_domain = dict()

    # expected output:
    # {}
    print( dict_domain )
    dict_domain.clear()

    


    # Create dictionary with given keys and default value

    # Method_#1 : using a list of given keys
    country = ["Japan", "France", "United Kingdom"]
    dict_domain = dict().fromkeys( country, "TBD")

    # expected output
    # {'Japan': 'TBD', 'France': 'TBD', 'United Kingdom': 'TBD'}
    print( dict_domain )
    dict_domain.clear()



    # Create dictionary with given key-value 

    # Method_#1 : Initialization with literals
    dict_domain = { "Japan":".jp", "France":".fr", "United Kingdom" : ".uk" }

    # expected output
    # {'Japan': '.jp', 'France': '.fr', 'United Kingdom': '.uk'}
    print( dict_domain )
    dict_domain.clear()
    

    
    # Method_#2 : Initialization with key-value pairs
    dict_domain = dict( Japan = ".jp", France = ".fr", United_Kingdom = ".uk" )
    
    # expected output:
    # {'Japan': '.jp', 'France': '.fr', 'United Kingdom': '.uk'}
    print( dict_domain )
    dict_domain.clear()



    # Method_#3 : Initialization with a list of tuples
    country_domain = [("Japan",".jp"), ("France", ".fr"), ("United Kingdon", ".uk") ]
    dict_domain = dict( country_domain )

    # expected output:
    # {'Japan': '.jp', 'France': '.fr', 'United Kingdom': '.uk'}
    print( dict_domain )
    dict_domain.clear()



    # Method_#4 : Initialization by two list and zip
    country = ["Japan", "France", "United Kingdom"]
    domain = [".jp", ".fr", ".uk"]
    dict_domain = dict( zip(country, domain) )

    # expected output:
    # {'Japan': '.jp', 'France': '.fr', 'United_Kingdom': '.uk'}
    print( dict_domain )



if __name__ == '__main__':

    demo_dictionary_creation()