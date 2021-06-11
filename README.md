# Collatz
A fun little program to play around with the Collatz conjecture from mathematics.

In short, the Collatz conjecture is an idea in mathematics which suggests that any natural number, when applied two rules, will eventually reach 1. Those two rules are as follows:
1) if the number is even, then divide by two.
2) If the number is odd, then multiply by three, and add one.

Rinse and repeat. To learn more about the details of the conjecture, visit the following link: https://en.wikipedia.org/wiki/Collatz_conjecture .

Although the function could be implemented with similar efficiency via a while loop, the function is mathematically recursive in nature, and because of that, I thought it was appropriate to implement it with that in mind.

As this was my first program of the summer, all I intended to do was use recursion to implement it, and leave it there. After doing so though, I realized that there were potentially some interesting observations to be derived from continuing it a bit further, and so I did.

Throughout the project, I refer to something called the "collatz number". This is not a standard term, but rather one which I came up with that refers to the number of cycles it takes for any x in a range to reach 1, via the aforementioned conditions of the Collatz conjecture. The idea of the collatz number is at the core of the insights which followed the initial implementation of the recursive algorithm.

## Insights
There are two interesting insights which came as a result of this project. 
The first pertains to the general increase in collatz numbers through an indexed range. I expected the collatz numbers to increase either exponentially or quadratically in some way, but if you look at the first screenshot, you can see that it actually resembles more of a logarithmic curve. This means that as index increases through the range, the difference between average collatz numbers decreases. This is best exemplified at a large range, such as with what is shown in the screenshot (1 - 15 000).

The second interesting outcome of the project came as I was looking through the collatz numbers, and realized that there would often be consecutive integers which shared the same collatz number. For example, the integers 49, 50, and 51 all share a collatz number of 25. As a result of this realization, I saw an opportunity to continue the project a step further, and see if there was a pattern in these consecutive collatz numbers that might emerge over a large range of integers.

Much to my surprise, there was! Unlike with primes, where the distance between prime numbers increases throughout the natural numbers, the difference between collections of consecutive collatz numbers actually remains almost constant throughout the the ranges that I computed. The second screenshot shows a graph with two subplots, one of which being a rate of increase across average integers in collections of collatz numbers, and the other being the difference between those average integers.
What the first subplot confirms from the constant difference between collections of consecutive collatz numbers is that the rate of increase for these collections is actually linear!
This means that the occurrence of a cluster of integers with consecutive collatz numbers will almost always be somewhere between 2-8 numbers away from another cluster. While this is obviously a fluctuation, it is an extremely controlled one, and so on a large range, it is approximately linear.

I hope you found this as cool as I have.

## Goals
Although I am happy with the functionality of the program in its current form, there are 4 major issues:
1) The function which processes and groups consecutive collatz numbers is quite slow. There are too many loops, some of which being nested, and aside from the fact that it detracts from the program's readability, it ultimately makes the program quite slow, especially when working with ranges in larger than 1 - 10000.
2) The program lacks a GUI at the moment, but I intend to create a simple UI using pygame or tkinter in the near future.
3) There is a lack of error-handling upon unexpected user input. It simply reiterates the loop. I intend add some try blocks to correct that.
4) The information relayed by the graphs provided through matplotlib is limited by the labelling at the moment.
