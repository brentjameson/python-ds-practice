def weekday_name(day_of_week_num):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    day_of_week_pairs = {1 : 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7:'Saturday'}

    print(day_of_week_num)

    return day_of_week_pairs.get(day_of_week_num, None)