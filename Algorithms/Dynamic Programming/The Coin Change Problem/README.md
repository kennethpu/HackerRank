The Coin Change Problem
===================

###Problem Statement###

How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer.

###The problem can be formally stated:###

Write a program that, given

- An amount N and types of infinite available coins M
- A list of M coins - C = {C<sub>1</sub>,C<sub>2</sub>,C<sub>3</sub>,..,C<sub>M</sub>}

Prints out how many different ways you can make change from the coins to `STDOUT`.

###Solving the overlapping subproblems using dynamic programming###

You can solve this problem recursively, but not all the tests will passs unless you optimise your solution to eliminate the overlapping subproblems using a dynamic programming solution

Or more specifically;

If you can think of a way to store the checked solutions, then this store can be used to avoid checking the same solution again and again.


###Input Format###

First line will contain 2 integer N and M respectively.  
Second line contain M integer that represent list of distinct coins that are available in infinite amount.

###Constraints###

<pre>
1 ≤ C<sub>i</sub> ≤ 50
1 ≤ N ≤ 250
1 ≤ M ≤ 50
</pre>

The list of coins will contain distinct integers.

###Output Format###

One integer which is the number of ways in which we can get a sum of N from the given infinite supply of M types of coins.

###Sample Input #01###

```
4 3
1 2 3 
```

###Sample Output #01###

```
4
```

###Sample Input #02###

```
10 4
2 5 3 6
```

###Sample Output #02###

```
5
```

###Explanation###

- Example 1: For N=4 and C={1,2,3} there are four solutions: {1,1,1,1}, {1,1,2}, {2,2}, {1,3}
- Example 2: For N=10 and C={2,5,3,6} there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}, {5,5}.

###Hints###

- Think about the degenerate cases:
  - How many ways can you give change for 0 cents?
  - How many ways can you give change for >0 cents, if you have no coins?
- If you are having trouble defining your solutions store, then think about it in terms of the base case (n=0)