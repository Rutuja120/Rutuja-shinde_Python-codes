def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def triangle_area(base, height):
    return 0.5 * base * height

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_first_n_numbers(n):
    return (n * (n + 1)) // 2


print(swap_numbers(3, 5)) 
print(triangle_area(4, 6))  
print(factorial(5))         
print(sum_first_n_numbers(5))  
