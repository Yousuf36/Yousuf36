"""Functions to calculate lasagna prep and bake times."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Args:
        elapsed_bake_time (int): Baking time already elapsed in minutes.

    Returns:
        int: Remaining bake time in minutes derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Args:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: Total time spent preparing the lasagna layers.
    """
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time (prep time + bake time).

    Args:
        number_of_layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has spent
            baking in the oven.

    Returns:
        int: The total minutes spent preparing and baking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


