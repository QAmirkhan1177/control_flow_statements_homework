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
    p ,n=0 ,0
    if a>0:
        p+=1
    if a<0:
        n+=1
    
    if b>0:
        p+=1
    if b<0:
        n+=1
    
    if c>0:
        p+=1
    if c<0:
        n+=1
    result="there are a lot of positive numbers"
    if p<n: 
        result="there are a lot of negative numbers"   
    print (main(1,-3,9))
   