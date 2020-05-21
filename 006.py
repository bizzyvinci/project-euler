'''
Problem: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

n=100
# Square of Sum
S=(n*(n+1)/2)**2

# Sum of squares
P=n*(n+1)*(2*n+1)/6

print(S-P)