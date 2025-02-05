def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 0 and a % 2 == 1:
        return "Positive odd number"
    if a > 0 and a % 2 == 0:
        return "Positive even number"
    if a < 0 and a % 2 == 1:
        return "Negative odd number"
    if a < 0 and a % 2 == 0:
        return "Negative even number"
    if a == 0:
        return "The number is zero"
print(main(8))