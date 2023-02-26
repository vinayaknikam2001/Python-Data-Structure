''' This is program to find gcd of 2 numbers using euclidian theorem.
    Calculating gcd by loop'''
def gcd_byloop(a,b):
    while(b):
        temp = a%b
        a = b
        b = temp
    return a


def gcd_byrecurssive(a,b):
    if(b == 0):
        return a
    else:
        gcd = gcd_byrecurssive(b,a%b)
    return gcd



if(__name__ == '__main__'):
    a = int(input('Enter 1st number : \n'))
    b = int(input('Enter 2nd number : \n'))
    c = int(input('Enter your choice for calculating gcd 1 by looping and 0 by recurssive function call : \n'))
    if(b>a):
        a,b = b,a
    if(c):
        gcd = gcd_byloop(a,b)
    else:
        gcd = gcd_byrecurssive(a,b)

    print(f'\n GCD or HCF of {a} and {b} is {gcd}. ')
    
    
            


