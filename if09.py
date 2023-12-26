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
    x1=a % 10
    x2=a // 10
    reversed_a=x1 * 10 + x2
    return reversed_a < a
print(main(28))