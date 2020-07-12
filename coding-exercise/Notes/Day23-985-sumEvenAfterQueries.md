For beginners like me, here are some more explanations.
"When acting on an array element A[index], the rest of the values of A remain the same."

When we add things from query to A[index], the rest of A is not changed. Thus, we do not need to
calculate the sum of the whole array A every time after we perform the addition.
This saves lots of time, since we are not traversing the whole array A for query.length times.
Instead, we only traverse the array A only once.
"Let's remove A[index] from S if it is even, then add A[index] + val back (if it is even.)"

If we don't perform Sum(A) every time after addition, what do we do?
1. We find the sum of the even numbers in A first. We will perform modifications on this "sum"
instead of traverse A to find a new sum every time after addition.
2. Now let's look at the elements at A that is going to change.
if A[index] is an even number, we remove it from sum. Why?
    We already added it to our "sum". If after the addition, this number becomes odd, we won't want it anymore.
    if A[index] is an odd number, we don't touch it. We didn't add it to our "sum".
3. Then we check the result after the addition.
    if A[index]+val is even:
        we add the whole "A[index]+val" to our sum, since it's even.
        recall that , we subtracted A[index] in our previous step. we want to add everything back.
    if A[index]+val is odd:
        we don't do anything.
    since it's odd, we don't want it in our sum.
    we already subtracted A[index] from sum if it was even.
    we didn't add A[index] to our sum if it was odd.
    therefore, we don't need any extra steps here.
4. Now look again at the examples. I hope this helped.
5. The principle is, try to not recalculate the whole thing again and again. Avoid wasting resources at all costs.
6. Another way can be, and might be easier to understand, but takes extra steps:
we check the A[index]+val first. then check A[index]