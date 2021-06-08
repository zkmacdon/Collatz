# Collatz
A fun little program to play around with the Collatz conjecture from mathematics.

In short, the Collatz conjecture is an idea in mathematics which suggests that any natural number, when applied two rules, will eventually reach 1. Those two rules are as follows:
1) if the number is even, then divide by two.
2) If the number is odd, then multiply by three, and add one.

Rinse and repeat. To learn more about the details of the conjecture, visit the following link: https://en.wikipedia.org/wiki/Collatz_conjecture .

Although the function could be implemented with similar efficiency via a while loop, the function is mathematically recursive in nature, and because of that, I thought it was appropriate to implement it with that in mind.

As this was my first program of the summer, all I intended to do was use recursion to implement it, and leave it there. After doing so though, I realized that there were potentially some interesting observations to be derived from continuing it a bit further, and so I did.

## Insights
Coming soon.

## Goals
Although I am happy with the functionality of the program in its current form, there are 3 major issues:
1) The function which processes and groups consecutive collatz numbers is quite slow. There are too many loops, some of which being nested, and aside from the fact that it detracts from the program's readability, it ultimately makes the program quite slow, especially when working with ranges in larger than 1 - 10000.
2) The program lacks a GUI at the moment, but I intend to create a simple UI using pygame or tkinter in the near future.
3) There is a lack of error-handling upon unexpected user input. It simply reiterates the loop. I intend add some try blocks to correct that.
