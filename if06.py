def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    positive_count = 0
    negative_count = 0

    if a > 0:
        positive_count += 1

    if b > 0:
        positive_count += 1

    if c > 0:
        positive_count += 1

    if a < 0:
        negative_count += 1

    if b < 0:
        negative_count += 1

    if c < 0:
        negative_count += 1

    if positive_count > negative_count:
        return "There are a lot of positive numbers"
    if positive_count < negative_count:
        return "There are a lot of negative numbers"
    if positive_count == negative_count:
        return "There is an equal number of positive and negative numbers