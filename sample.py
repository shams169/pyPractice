"""
This program demonstrate the use of generators in python
"""


#This is the initial implementation of getting the prime numbers
import math

"""
This is an implementation of getting prime numbers using a generator.
A generator function returns a generator iterator which implements the next function
as that of an iterator.

A generator does not return from the function permanently, but save the state of the function
when yield is reached.
When the next is called on the generator again, the function resumes execution from the next line of the yield.

A StopIteration is raised when the last iteration is reached, this signals whoever calling next() that the
generator is exhasuted. So you can use the values from the generator only once.

That is why, when we need an infinite series, we use "while True:" so in this example we will get a prime
number as along as we call next on the generator function.

## We can even pass values to the generators:
>
"""
#/*******************************************************/
# Function: getPrimes(start)
# Desc    : Generator function to generate infinite series
#           of prime numbers greater than start
#/*******************************************************/
def getPrimes(start):
    number = start
    while True:
        if isPrime(number):
            yield number
        number += 1
#End of getPrimes


#/*******************************************************/
# Function: getPrime_Static(input_list)
# Desc    : Function that returns a list of prime numbers
#            from a given input list
#/*******************************************************/
def getPrime_Static(input_list):
    #Result List
    result_list = []

    for element in input_list:
        if isPrime(element):
            result_list.append(element)
    return result_list
#End of getPrime_Static

#/*******************************************************/
# Function: sumOfPrimes(start, end)
# Desc    : Add primes between start and end
#/*******************************************************/
def sumOfPrimes(start, end):
    num = start
    sum = 0
    iter_prime = getPrimes(start)
    while num < end:
        n = next(iter_prime)
        #print("n: "+str(n))
        sum += n
        #print("sum: "+str(sum))
        #print()
        num = n
    return sum

#/*******************************************************/
# Function: isPrime(element)
# Desc    : Function to check if a number is prime or not
#/*******************************************************/
def isPrime(element):
    if element > 1:
        if element == 2:
            return True
        if element%2 == 0:
            return False
        for item in (3, int(math.sqrt(element)+1 ), 2 ):
            if element%item == 0:
                return False
        return True
    return False
#End of isPrime

# Working in testBranch

#/*******************************************************/
# Function: main()
# Desc    : Main Function
#/*******************************************************/
def main():
    #print(getPrime_Static([1,2,3,4,5,6]))

    # num = getPrimes(3)
    # for i in range(5):
    #     print(next(num))

    print(sumOfPrimes(0,50))

#End of main

if __name__ == '__main__':
    main()
