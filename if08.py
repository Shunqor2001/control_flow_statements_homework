def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    returnmessage = ""

    if 10 <= abs(a) < 100:
        if a % 2 == 1:
            message = "Two-digit odd number"
        if a % 2 == 0:
            message = "Two-digit even number"
    if 100 <= abs(a) < 1000:
        if a % 2 == 1:
            message = "Three-digit odd number"
        if a % 2 == 0:
            message = "Three-digit even number"

    return message