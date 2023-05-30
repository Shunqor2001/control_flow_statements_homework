def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    tens_digit = a // 10
    ones_digit = a % 10

    new_number = ones_digit * 10 + tens_digit

    if new_number <= a:
        return True
    if new_number >= a:
        return False
print(main())