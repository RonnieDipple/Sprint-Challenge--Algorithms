#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) is my answer as the initial input is 0 but n is unknown. 
As I am not sure I must assume O(n) 


b) Again n is unknown. As we aren’t certain then we must assume O(n) 


c)my answer is O(1) as the moment the calculation is used we know the exact amount of bunny ears

## Exercise II
So there are two possible outcomes/base cases here, either the egg breaks or it does not
so we need an algorithm to determine the best scenario
what we know:
the amount of floors is n
the egg get's broken if thrown off floor f so we have an upper bound
so if the egg is thrown off of every floor below f it would survive
we have plenty of eggs
we need to divide the building into sections so that it takes 
the same number of throws to find the optimal height
recursion might be a good idea here:

we start on the 14 floor then move up every 14 floors minus 1 until an egg breaks
then we repeat the process minus 1
n + (n-1) + (-n2) + (-n3) etc

Complexity: O(n^2)








