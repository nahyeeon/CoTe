a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

# 함수 안쓰고 함
a, b = map(int, input().split())

def gcd(a,b):
    i = min(a,b)
    while i>=1:
        if a%i==0 and b%i==0:
            return i
        i -= 1
        
def lcm(a,b):
    return a*b// gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))