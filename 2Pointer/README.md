                                    Two Pointer Technique
## Two Pointers 

Optimization on some bruteforce approaches in certain condition.

Generalize approach:

Example:
Given a sorted array A ( sorted in ascending order ),
Find if there exists 2 integers A[i] and A[j] such that A[i] + A[j] = 0, i != j 
Now the naive solution would be,

        for (int i = 0; i < A.size(); i++) 
            for (int j = 0; j < A.size(); j++) {
                if (i != j && A[i] + A[j] == 0) return true; // solution found. 
                if (A[i] + A[j] > 0) break; // Clearly A[i] + A[j] would increase as j increases
            }
This solution is O(n^2).

However, let us now analyze how ‘i’ and ‘j’ move with iterations.
Clearly, ‘i’ moves forward with every iteration.
Now let us analyze the ‘j’ loop.
As i is increasing, A[i] is also increasing.
That means the point where the loop breaks is decreasing.
Let us rewrite the 2 loops slightly differently.

        for (int i = 0; i < A.size(); i++) 
            for (int j = A.size() - 1; j >= 0; j--) {
                if (i != j && A[i] + A[j] == 0) return true; // solution found. 
                if (A[i] + A[j] < 0) break; // Clearly A[i] + A[j] would decrease as j decreases.
            }
Still O(n^2).

Now, with the same analysis, as ‘i’ increases, A[i] also increases.
And the number of iterations after which ‘j’ breaks also increases.
But note what changes when ‘i’ moves to i + 1:

1. If A[i] + A[J] > 0,
2. Then A[i + 1] + A[J] is also greater than 0, as A[i + 1] > A[i].
This means if we have tried J for ‘i’, then when moving to i + 1, we should only try values of j < J.
This concludes that our ‘j’ should be monotonically decreasing and we could re-write the above solution as :

        int j = A.size() - 1;    
        for (int i = 0; i < A.size(); i++) 
            for (; j > i; j--) {
                if (i != j && A[i] + A[j] == 0) return true; // solution found. 
                if (A[i] + A[j] < 0) break; // Clearly A[i] + A[j] would decrease as j decreases.
            }

Let us analyze the time complexity of the above solution.
Let us say A.size() = n.

‘i’ moves in total of n steps.
‘j’ also moves in total of n steps
( j– is executed atmost n times. Note that we are never increasing the value of j. Neither are we resetting it ).
That means we take in total of n + n steps = O(n).

Two pointer approach work as optimization of Brute force 

#Summary
It is used in two Scenarios:
#### Scenario I:
a. Iterate the array from two ends to the middle.One pointer starts from the beginning while the other pointer starts from the end.<br />
b. This technique is often used for sorted array
#### Scenario II:
a. Two pointers with different steps. one is still used for the iteration while the second one always points at the position for next addition.<br />
b. One slow-runner and one fast-runner at the same time.<br />
c. It is used to solve the problem, which determine the movement strategy for both pointers.<br />
d. Sometimes need to sort the array before using the two-pointer technique. Also,need a greedy way to determine your movement strategy.