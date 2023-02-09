'''*H
* AUTHOR :   Razie Hyria        START DATE :    FEB 8th 2023
* FILENAME :        Simulate Process Scheduling          
* COURSE NAME:      CMPSC 472 Section 001: Operating Systems
* SEMESTER:         SPRING 2023
*
* DESCRIPTION :
*      Write a program to simulate one of two Process Scheduling algorithms
       Simulate either Shortest Job First (SJF) or Priority Scheduling.
*
* 
*FUNCTIONS USED:
*
*H'''
from tabulate import tabulate

ready_queue = [] # stores the processes and
listofprocess = ['a','b','c'] 
performed_Tasks = [] # add dequed tasks here after removing from queu
time = 0

print("Current queue", ready_queue)
print("current process: , Time till completion", listofprocess, time)
print("List of processes: ")

'''list all the process to the user, supplement some into the queue, and tll the user
to process x to begin
the queue will execute the processes based on the smalles affiliated burst time
for process in list of queue, chose the next smallest burst time to execute, and alert user
control the burst time with wait/sleep and wait for it to get to 0 before moving to next process

while the queue isnt done exectuting all the processes, the user may add another process from the list
if queue runs out, the list of processes is exaushted or user hits x, exit the program.

display like:
[list of process | time]  [list completed processes]
[current queue]
currently executing :[process | timex1]
[next: process | timex2]
[third: process | timex3]


'''

# burst cycle associated 


# catching user inputs
print("(E) to execute the next Process in the Ready Queue.")
print("(A) to Add a process in the Ready Queue")
print("(X) to Exit the program")
userinput = input("Please enter your choice\n")
print(userinput)


#printing tables

table = tabulate([["value1", "value2"], ["value3", "value4"]], ["column 1", "column 2"], tablefmt="grid")
print(table)



