<h1>Recursive Algorithms and Optimization</h1>


This project explores various recursive algorithms and optimization techniques. It includes a set of exercises designed to implement and analyze different types of recursion in Python, such as direct recursion, head recursion, tail recursion, nested recursion, tree recursion, and indirect recursion. The exercises also cover optimizations such as memoization and iterative approaches for better performance.
<h1>Table of Contents</h1>
Introduction
Exercises
Exercise 1: The Recursive Cashier (Direct Recursion)
Exercise 2: Virus Spread (Head Recursion)
Exercise 3: The Tail-Recursive Factorial (Tail Recursion)
Exercise 4: Pascal’s Triangle (Nested Recursion)
Exercise 5: File System Depth (Tree Recursion)
Exercise 6: Two-Way Communication (Indirect Recursion)
Bonus Challenge: The Towers of Hanoi (Optimization & Complexity)
Complexity Analysis
<h1>Introduction</h1>
This repository presents a set of recursive algorithms aimed at demonstrating different recursion types and optimizing their performance. Each exercise focuses on implementing a recursive solution for a problem, followed by analysis of the time and space complexities. In some cases, optimizations like memoization or switching to iterative solutions are explored to enhance efficiency.
The main goals of this project are to:
Understand and implement various types of recursion.
Analyze the time complexity of recursive functions.
Design optimal recursive solutions using memoization, iteration, or other strategies.
<h1>Exercises</h1>
1. Exercise: The Recursive Cashier (Direct Recursion)
A cashier needs to give change using the fewest number of coins. The minCoins function calculates the minimum number of coins needed for a given amount using direct recursion. An optimization is implemented using memoization to avoid recalculating previously solved subproblems.
2. Exercise: Virus Spread (Head Recursion)
A computer virus spreads exponentially every hour. The virusSpread function uses head recursion to determine how many computers will be infected after a given number of hours. An iterative solution is provided to compare performance and efficiency.
3. Exercise: The Tail-Recursive Factorial (Tail Recursion)
The factorial of a number is calculated using both a non-tail-recursive and a tail-recursive function. The tail-recursive version is more memory-efficient as it avoids stack overflow by reusing the stack frame for each recursive call.
4. Exercise: Pascal’s Triangle (Nested Recursion)
Pascal's Triangle is computed using nested recursion. The pascal function calculates values at the nnn-th row and kkk-th column of the triangle. This solution is inefficient for large values of nnn, and an iterative approach is suggested as a more optimal solution.
5. Exercise: File System Depth (Tree Recursion)
A file system can be represented as a tree, where each folder can contain files or subfolders. The maxDepth function computes the maximum depth of the file system. An iterative BFS solution is also discussed for better performance in large file systems.
6. Exercise: Two-Way Communication (Indirect Recursion)
A conversation alternates between the caller and receiver. The callerNo and receiverNo functions use indirect recursion to simulate the conversation, where each party alternates speaking. The recursion continues until both reach the base case.
Bonus Challenge: The Towers of Hanoi (Optimization & Complexity)
The Towers of Hanoi problem is a classic recursive puzzle. The hanoi function solves the problem by moving disks from one peg to another, following the rules. The minimum number of moves is shown to be O(2N−1)O(2^N - 1)O(2N−1). A solution with memoization is also explored to optimize the number of recursive calls.
Complexity Analysis
Here is a summary of the time and space complexities for each of the recursive solutions:
Exercise 1: The Recursive Cashier


Time Complexity (Direct Recursion): O(2N)O(2^N)O(2N) due to overlapping subproblems.
Time Complexity (Memoization): O(N×C)O(N \times C)O(N×C), where NNN is the amount and CCC is the number of coin denominations.
Space Complexity: O(N)O(N)O(N) for memoization.
Exercise 2: Virus Spread


Time Complexity (Head Recursion): O(N)O(N)O(N) due to NNN recursive calls.
Space Complexity (Head Recursion): O(N)O(N)O(N) for the recursion stack.
Time Complexity (Iterative): O(1)O(1)O(1).
Space Complexity (Iterative): O(1)O(1)O(1).
Exercise 3: The Tail-Recursive Factorial


Time Complexity: O(N)O(N)O(N) for both tail-recursive and non-tail-recursive versions.
Space Complexity (Tail Recursion): O(1)O(1)O(1) due to stack frame reuse.
Space Complexity (Non-Tail Recursion): O(N)O(N)O(N) due to recursive calls.
Exercise 4: Pascal’s Triangle


Time Complexity (Recursive): O(2N)O(2^N)O(2N) due to overlapping subproblems.
Space Complexity (Recursive): O(N)O(N)O(N) for the recursion stack.
Exercise 5: File System Depth


Time Complexity: O(N)O(N)O(N), where NNN is the number of files and folders in the file system.
Space Complexity: O(N)O(N)O(N) for the recursion stack.
Exercise 6: Two-Way Communication


Time Complexity: O(N)O(N)O(N) for alternating calls.
Space Complexity: O(N)O(N)O(N) for the recursion stack.
Bonus Challenge: The Towers of Hanoi


Time Complexity: O(2N−1)O(2^N - 1)O(2N−1), the minimum number of moves required.
Space Complexity: O(N)O(N)O(N) due to recursion stack.
Conclusion
This project provides a comprehensive set of exercises that cover a wide range of recursion techniques. By analyzing the complexity of each solution, we've also explored various optimizations, such as memoization and iteration, to improve efficiency. Recursion is a powerful tool, but it requires careful consideration of time and space complexity for optimal performance.
Feel free to explore each exercise, test different input values, and experiment with optimizations!

