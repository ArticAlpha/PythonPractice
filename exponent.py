# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

def exponent(base, expo):
    num=expo
    result=1
    while num>0:
        result=result*base
        num=num-1
    print(f"{base} raised to the power of {expo} is: {result}")

exponent(2,3)