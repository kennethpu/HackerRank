Is Fibo
===================

###Problem Statement###

You are given an integer, N. Write a program to determine if N is an element of the Fibonacci sequence.

The first few elements of the Fibonacci sequence are 0,1,1,2,3,5,8,13,⋯. A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are 0 and 1.

Formally: 
fib{0} = 0
fib{1} = 1
⋮
fib{n} = fib{n−1} + fib{n−2} ∀n > 1

###Input Format###

The first line contains T, number of test cases. 
T lines follow. Each line contains an integer N.

###Constraints###

```
1 ≤ T ≤ 10^5 
1 ≤ N ≤ 10^10
```

###Output Format###

Display `IsFibo` if N is a Fibonacci number and `IsNotFibo` if it is not. The output for each test case should be displayed in a new line.

###Sample Input###

```
3
5
7
8
```

###Sample Output###

```
IsFibo
IsNotFibo
IsFibo
```

###Explanation###

5 is a Fibonacci number given by fib{5} = 3+2  
7 is not a Fibonacci number  
8 is a Fibonacci number given by fib{6} = 5+3