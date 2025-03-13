# Objective:
# Understand and implement different types of recursion.
# Analyze the complexity of recursive functions.
# Design optimal recursive solutions.


#exercise 1(direct recursion:)

def minCoins(n,coins):
    if n == 0:
        return 0#  Base case: No more coins needed for zero amount
    coins = sorted(coins, reverse=True)
    for coin in coins:
        if coin <=n:
            return 1 + minCoins(n-coin,coins)
            
result = minCoins(47, [1, 5, 10, 25])
print(result)
#Time complexity: O(2^N)
#Space complexity: O(N)
#optimized solution using memoization
def minCoins(n, coins, memo):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    coins = sorted(coins, reverse=True)
    min_coins = float('inf')
    for coin in coins:
        if coin <= n:
            min_coins = min(min_coins, 1 + minCoins(n - coin, coins, memo))
    memo[n] = min_coins
    return min_coins
#Time complexity: O(N * M)where N is the amount and M is the number of coins
#Space complexity: O(N)

#exercise 2(h)

def virusSpread(N, P):
    if N == 0:
        return P
    return 2 * virusSpread(N - 1, P) + P
#Explanation:
# if n = 0 return P because no time has passed
#recursive case : at eaach hour every infected computer infects 2 more computers and the original P computers are still infected

#Time complexity: O(2^N)

print(virusSpread(3, 1))  
 # iterative approach   
def virusSpreadIterative(N, P):
    infected = P
    for _ in range(N):
        infected = 2 * infected + P

        
    return infected


print(virusSpreadIterative(3, 1))  

#time complexity: O(N)
# the iterative approach is more efficient than the recursive approach

#exercise 3(Tail Recursion)

#Non-Tail-Recursive Factorial
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  

#Tail-Recursive Factorial
def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

print(factorial_tail_recursive(5))

#time complexity: O(N) for both recursive and tail recursive functions

# exercice 4(nested recursion)
def pascal(n, k):
    if k == 0 or k == n:
        return 1  # Base case
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

# Print Pascal's Triangle up to n = 5
for n in range(6):
    for k in range(n + 1):
        print(pascal(n, k), end=" ")
    print()
#timecomplexity: O(2^N) 
#space complexity: O(N)

#exercice6* 6(indirect recursion)
def callerNo(n):
    if n == 0:
        return
    print(f"Caller: {n} sentences")
    receiverNo(n - 1)

def receiverNo(n):
    if n == 0:
        return
    print(f"Receiver: {n} sentences")
    callerNo(n - 1)

# Test the function with n = 3
callerNo(3)
#time complexity: O(N) because the functions are called N times
#bonus exercice
#
def hanoi(N, A, B, C):
    if N == 1:
        print(f"Move disk 1 from {A} to {C}")
        return
    hanoi(N - 1, A, C, B)  # Move N-1 disks from A to B
    print(f"Move disk {N} from {A} to {C}")
    hanoi(N - 1, B, A, C)  # Move N-1 disks from B to C

# Test the Towers of Hanoi function
hanoi(3, 'A', 'B', 'C')
#time complexity: O(2^N)





             
                
                