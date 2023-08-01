"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining():
    def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    remaining_bake_time = EXPECTED_BAKE_TIME - elasped_bake_time 
    return remaining_bake_time
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time
        
    
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the total preparation time based on the number of layers.
    
    :param number_of_layers: int - number of layers added to the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME'.
    """
    prep_time = PREPARATION_TIME * number_of_layers
    return prep_time


# TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
"""
    Calculate the total elapsed time, which is the sum of the preparation time and elapsed bake time.
    
    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    total_time = prep_time + elapsed_bake_time
    return total_time
