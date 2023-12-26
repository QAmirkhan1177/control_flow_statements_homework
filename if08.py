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
    result=''
    if a>9 and a<100 and a%2 ==1:
        result="two-digit odd number"
    if a>9 and a<100 and a%2 ==0:
        result="two-digit even number"
    if a>99 and a<1000 and a%2 ==1:
        result="three-digit odd number"
    if a>99 and a<1000 and a%2 ==0:
        result="three-digit even number"  
    return result
print(main(127)) 