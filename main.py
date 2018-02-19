import time
from random import randrange
from Selection_Algorithm import *
import matplotlib.pyplot as plt
from Linkedlist import Linkedlist
import math
def draw(t1, t2, t3,  siz, max_input):
    plt.figure(figsize=(13,6))
    plt.gcf().canvas.set_window_title('Comparison')
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Comparison")
    plt.xlabel("size of inputs")
    plt.ylabel("time")
    plt.annotate('T of Linked List with swapping nodes', xy=(max_input, t2[2]), xytext=(math.ceil(max_input + 0.1 * max_input), t2[2] + 0.5), arrowprops=dict(facecolor='blue', shrink=0.05), )
    plt.annotate('T of Linked List with swapping data', xy=(max_input, t3[2]), xytext=(math.ceil(max_input + 0.1 * max_input), t3[2] + 0.5), arrowprops=dict(facecolor='cyan', shrink=0.05), )
    plt.annotate('T of List', xy=(max_input, t1[2]), xytext=(math.ceil(max_input + 0.1 * max_input), t1[2] + 0.5), arrowprops=dict(facecolor='red', shrink=0.05), )
    plt.plot(siz, t1, 'r', siz, t2, 'b', siz, t3, 'c')
    plt.axis([0, 1500, 0, 6])
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.xlabel("size of inputs")
    plt.ylabel("time")
    plt.bar(siz, t2, 50, color = 'b', align = 'center')
    plt.bar(siz, t3, 50, color = 'c', align = 'center')
    plt.bar(siz, t1, 50, color = 'r', align = 'center')
    plt.show()
def automatic():
    t1 = []
    t2 = []
    t3 = []
    siz = []
    arr = []
    max_in = 0
    linked_list =  Linkedlist()
    i = 10
    while i < 10000:
        siz.append(i)
        for j in range(0, i):
            x = randrange(0, 1000000)
            arr.append(x)
            linked_list.add(x)
            max_in = i
        s = time.time()
        Selection_Sort_Array(arr)
        e = time.time()
        t1.append(e - s)
        s = time.time()
        Selection_Sort_Linked_List(linked_list)
        e = time.time()
        t2.append(e - s)
        s = time.time()
        selectionsort_linked(linked_list)
        e = time.time()
        t3.append(e - s)
        i *= 10
    draw(t1, t2, t3, siz, max_in)
def help_manual(linked_list, arr, siz):
    linked_list1 = Linkedlist()
    s = time.time()
    Selection_Sort_Array(arr)
    e = time.time()
    tim = float(e - s)
    s = time.time()
    Selection_Sort_Linked_List(linked_list)
    e = time.time()
    tim1 = float(e - s)
    s = time.time()
    selectionsort_linked(linked_list)
    e = time.time()
    tim2 = float(e - s)
    tim *= 1000000000
    tim1 *= 1000000000
    tim2 *= 1000000000
    print(tim)
    print(tim1)
    print(tim2)
    plt.figure(figsize=(13,6))
    plt.title(s = "Comparison")
    plt.grid(True)
    plt.xlabel("size of inputs")
    plt.ylabel("time in milliseconds")
    plt.axis([0, math.ceil(siz * 1.1), 0, math.ceil(tim1 * 1.1)])
    plt.annotate('T of Linked List with swapping nodes', xy=(siz, tim1), xytext=(math.ceil(siz * 1.1), tim1 + 0.5), arrowprops=dict(facecolor='blue', shrink=0.05), )
    plt.annotate('T of Linked List with swapping data', xy=(siz, tim2), xytext=(math.ceil(siz * 1.1), tim2 + 0.5), arrowprops=dict(facecolor='cyan', shrink=0.05), )
    plt.annotate('T of List', xy=(siz, tim), xytext=(math.ceil(1.1 * siz), tim + 0.5), arrowprops=dict(facecolor='red', shrink=0.05), )
    plt.bar(siz, tim, math.ceil(0.05 * siz), color = 'b', align = 'center')
    plt.bar(siz, tim1, math.ceil(0.05 * siz), color = 'c', align = 'center')
    plt.bar(siz, tim2, math.ceil(0.05 * siz), color = 'r', align = 'center')
    plt.show()




#automatic()



