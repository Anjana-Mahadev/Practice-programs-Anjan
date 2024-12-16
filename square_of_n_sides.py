def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    result=[]
    for i in range(1,n+1):
        result=result + ['*' * n]
    print(result)
    for i in result:
        print(i)


if __name__=='__main__':
    generate_square(5)
