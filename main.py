"""
Collatz Conjecture Modeller: V1

Primary goal for this iteration is to use the following rules, via recursion, to arrive at 1:
    - If the n is odd, then compute 3n + 1
    - If the n is even, compute n/2
Following that, I used the newly generated objects to generate some insights about the phenomena 
surrounding the conjecture, and to visualize some of my findings graphically.
"""
import matplotlib.pyplot as plt

from Collatz import Collatz
from typing import List, Tuple
import matplotlib.pyplot as p
import numpy


def plot_points_fixed(x_data: List[int], y_data: List[int]) -> None:
    p.plot(x_data, y_data)
    p.xlabel('Integers Plotted')
    p.ylabel('Collatz Number')
    p.show()


def consecutive_cycles(x_data: List[int], y_data: List[int]) -> None: # the runtime efficiency of this function needs to be improved.
    consecutive_list = []
    for j in range(len(x_data)):
        if j < len(x_data) - 1 and (y_data[j] == y_data[j + 1] or y_data[j] == y_data[j - 1]):
            consecutive_list.append((x_data[j], y_data[j]))

    consecutive_groups = []
    for k in consecutive_list: # reduce the number of for loops.
        if consecutive_groups:
            for l in range(len(consecutive_groups)):
                if consecutive_groups[l][0][1] == k[1] and k not in consecutive_groups[l]\
                        and k[0] - consecutive_groups[l][-1][0] == 1:

                    consecutive_groups[l].append(k)
            k_count = 0
            for s in range(len(consecutive_groups)):
                if k in consecutive_groups[s]:
                    k_count += 1

            if k_count == 0:
                consecutive_groups.append([k])

        else:
            consecutive_groups.append([k])

    x_list_2 = []
    y_list_1 = []
    y_list_2 = []
    for r in range(len(consecutive_groups)):
        x_list_2.append(r + 1)
        if len(consecutive_groups[r]) % 2 != 0:
            r_len = int(len(consecutive_groups[r]) - 1 / 2)
            y_list_2.append(consecutive_groups[r][r_len][0])
        else:
            r2_len = round(len(consecutive_groups[r]) / 2)
            y_list_2.append(consecutive_groups[r][r2_len][0])

    for q in range(len(y_list_2)):
        if q < len(y_list_2) - 1:
            diff_q = y_list_2[q + 1] - y_list_2[q]
            y_list_1.append(diff_q)
    x_list_1 = x_list_2[:-1]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('A plot of consecutive collatz numbers and the distance from one '
                 'group to another')
    ax1.plot(x_list_2, y_list_2)
    ax2.plot(x_list_1, y_list_1, )
    p.show()


if __name__ == "__main__":
    x_list = []
    y_list = []

    highest_pair = (0, 0)
    for i in range(int(input("Choose first num: ")), int(input("Choose second num: ")) + 1):
        i_collatz = Collatz(i)
        i_collatz.run()
        pair = i_collatz.make_tuple()
        if highest_pair == (0, 0):
            highest_pair = pair
        else:
            if pair[1] < highest_pair[1]:
                highest_pair = pair
        x_list.append(pair[0])
        y_list.append(pair[1])
    keep_going = True
    while keep_going is not False:
        question = input("Do you want to look at an interesting plot of the Collatz numbers? (Y/N) ")
        if question == "Y" or question == "y" or question == "Yes":
            q2 = input("Graph 1 or Graph 2? ")
            if q2 == "Graph 1" or q2 == "graph 1" or q2 == "1":
                plot_points_fixed(x_list, y_list)
            elif q2 == "Graph 2" or q2 == "graph 2" or q2 == "2":
                consecutive_cycles(x_list, y_list)
        else:
            keep_going = False
