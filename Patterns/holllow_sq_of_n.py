def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    result=[]
    if n==1:
        return ['*']
    else:
        result.append(n*'*')
        for i in range(0,n-2):
            result.append('*' + (n-2)*' ' + '*')
        result.append(n*'*')
        return result

square=generate_hollow_square(5)
print(square)