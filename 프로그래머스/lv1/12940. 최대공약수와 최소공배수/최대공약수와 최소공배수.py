import math

def get_gcd(n, m):
    gcd = 0
    
    if n % m == 0: gcd = m
    elif m % n == 0: gcd = n
    else:   
        for i in range(1, min(n, m) + 1):
            if n % i == 0 and m % i == 0: 
                gcd = i
            
    return gcd

def get_lcm(n, m, gcd):
    lcm = 0
    
    if gcd == 1: lcm = n * m
    else: lcm = n * m / gcd
    
    return lcm

def solution(n, m):
    gcd = get_gcd(n, m)
    lcm = get_lcm(n, m, gcd)
    
    return [gcd, lcm]