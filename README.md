# Zappos Coding Competition March 2016

My solution accomplishes absolutely nothing that was asked for in the competition, but here it is. (See the rules <a href='https://challenge.zappos.biz/problems/number-chain/index.html'>here</a>.)

I spent 3 hours.

Here's my reasoning:
* If the first number in the pair is larger than the second, only the third operation (adjacent bit-swapping) will reduce the first number and bring it closer to the second. If bit-swapping can't bring the first lower than the second, then no solution exists.
* Once the first number has been reduced to a value lower than the second, find the difference between the two numbers (diff). Then, if diff appears as a digit in the first number, add it to the first number. This approach does not account for the possibility that subsequences longer than one digit can also be added to the first number.
* If diff does not appear as a subsequence of the first number, then the second operation (split the number into two pieces and multiply them) would be used. I didn't get this far. 
* Of course, all of the above steps only account for the case when the first number is larger than the second (and it doesn't do a complete job of that). If the first is smaller, then... I'm going to bed.
