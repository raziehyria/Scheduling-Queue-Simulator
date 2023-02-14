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
*FUNCTIONS USED: time, dictionarys.
*H'''
# notes from class
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
[third: process | timex3]'''

from tabulate import tabulate
import time
import sys

'''gettingkeyss = lxTerm()
gettingkeyss.getch() '''

active_queue = [
       
] # stores the processes and affiliated burst time
listofprocesses = {
       'a' : 5,
       'b' : 6,
       'c' : 2,
       'd' : 7,
       'e' : 1,
       'f' : 10,
       'g' : 8
       } 

performed_Tasks = [] # add dequed tasks here after removing from queu
burst = listofprocesses.values()

print("Current queue", active_queue)
print("current process: , Time till completion", listofprocesses.values(), time)
print("List of processes: ")


# catching user inputs
print("(E) to start executing the queue.")
print("(A) to Add a process in the Ready Queue")
print("(X) to Exit the program")
userinput = input("Please enter your choice\n")
print("Your choice was: %s" % userinput)

#functions to print various tables
def print_process_table():
       headers = ["Index", "Process", "Burst Time"]
       table = [[key.upper(), value] for key, value in listofprocesses.items()]
       print('\n',tabulate(table, showindex=True, headers=headers, tablefmt="pretty"))

def print_queue_table():
       headers = ["Index","Current Process", "Time Remaining"]
       table = [[key, value] for key, value in listofprocesses.items()]
       print('\n',tabulate(table, showindex=True headers=headers, tablefmt="pretty"))

def print_completed_table():
       headers = ["Completed Process"]
       table = [[key.upper()] for key in listofprocesses.items()]
       print('\n',tabulate(table, headers=headers, tablefmt="pretty"))


#run the program here
if __name__ == '__main__' :
       print_process_table()


