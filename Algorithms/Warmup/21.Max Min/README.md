Max Min
===================

###Problem Statement###

Given a list of N integers, your task is to select K integers from the list such that its _unfairness_ is minimized.

if (x{1},x{2},x{3},…,x{k}) are K numbers selected from the list N, the _unfairness_ is defined as

max(x{1},x{2},…,x{k})−min(x{1},x{2},…,x{k})

where max denotes the largest integer among the elements of K, and min denotes the smallest integer among the elements of K.

###Input Format###

The first line contains an integer N.  
The second line contains an integer K.  
N lines follow. Each line contains an integer that belongs to the list N.

**Note:** Integers in the list N may not be unique.

###Constraints###

```
2 ≤ N ≤ 10^5 
2 ≤ K ≤ N 
0 ≤ integer in N ≤ 10^9
```

###Output Format###

An integer that denotes the minimum possible value of unfairness.

###Sample Input #00###

```
7
3
10
100
300
200
1000
20
30
```

###Sample Output #00###

```
20
```

###Explanation #00###
Here K=3; selecting the 3 integers such that K = 10,20,30, unfairness equals

```
max(10,20,30) - min(10,20,30) = 30 - 10 = 20
```

###Sample Input #01###

```
10
4
1
2
3
4
10
20
30
40
100
200
```

###Sample Output #01###

```
3
```

###Explanation #01###

Here K=4; selecting the 4 integers 1,2,3,4, unfairness equals

```
max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
```

###Sample Input #02###

```
6
3
10
20
30
100
101
102
```

###Sample Output #02###

```
2
```

###Explanation #02###

Here K=3; the 3 integers so that the difference between the maximum and the minimum is the smallest are 100,101,102, which means unfairness equals

```
max(100, 101, 102) - min(100, 101, 102) = 102 - 100 = 2
```