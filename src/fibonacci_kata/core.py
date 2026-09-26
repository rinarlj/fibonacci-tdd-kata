def fibonacci(n: int) -> int:
    """
        Returns the n-th Fibonacci number 
        Contract:
        - if n = 0: 0
        - if n = 1: 1
        - otherwise: fibonacci(n-1) + fibonacci(n-2)

    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("fibonacci expects a positive integer")
    
    prev = 0
    cur = 1
    
    for k in range(n):
        cur, prev = cur + prev, cur


    return prev