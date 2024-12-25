def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Your code here
    result=[]
    result.append(n*'*')
    for i in range(m-2):
        result.append(n*'*')
    result.append(n*'*')
    
    print(result)
    for j in result:
        print(j)


generate_rectangle(5,4)
        