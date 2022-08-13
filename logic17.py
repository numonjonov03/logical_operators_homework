def main(b):
    a=b
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a%10<=a//10%10 and a//10%10<=a//10//10%10 and a//10//10%10<=a//10//10//10%10 and a//10//10//10%10<=a//10//10//10//10%10
print(main(87654))