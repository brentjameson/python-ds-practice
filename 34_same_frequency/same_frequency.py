def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_list = [list(str(num1)), list(str(num2))]
    
    return sorted(num1_list[0], key = int) == sorted(num1_list[1], key = int)