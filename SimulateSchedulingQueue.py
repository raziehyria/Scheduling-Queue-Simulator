'''*H
* AUTHOR :   Razie Hyria        START DATE :    FEB 8th 2023
* FILENAME :        Simulate SJF Process Scheduling          
* COURSE NAME:      CMPSC 472 Section 001: Operating Systems
* SEMESTER:         SPRING 2023
*
* DESCRIPTION :
*      Write a program to simulate one of two Process Scheduling algorithms
       Simulate either Shortest Job First (SJF) or Priority Scheduling.
* 
*FUNCTIONS USED: time, dictionarys, queue, tabulate.
* 
* def burst_time(burst) Helper function used to deincriment and display the given burst time of a process
* borrowed from Stack overflow: \https://stackoverflow.com/a/66940953/17628672
*H'''

from tabulate import tabulate
import time
import sys

'''
***************************************************************
* declaring all the variables and data structures we will use *
***************************************************************
'''


listofprocesses = { # the entire catalog of processes
       'A' : 5,
       'B' : 6,
       'C' : 2,
       'D' : 7,
       'E' : 1,
       'F' : 10,
       'G' : 3 } 

active_queue = { # supplemented active queue
       'G' : 3,
       'F' : 10,
       'A' : 5} 

completed_Tasks = [] # stores completed tasks

#userinput = input("Please enter your choice\n")


'''
***************************
* Varius Helper functions *
***************************
'''

def add_to_queue(process): # function used to store 
       active_queue[process] = listofprocesses[process]

def get_next_in_queue(dict): # a functin used to get the next shortest (value) sjf task in the queue
       next_value = min(d, key=d.get) # uses the min function to iterate dict to find and store the next value min task
       return next_value # returns the task

def check_status(task):
       if task in completed_Tasks or task not in listofprocesses:
              return False
       else:
              return True

def burst_time(burst):
       for i in range(burst,0,-1): # deincrimenting starting from the burst value
              print(f"{i}", end="\r", flush=True) # displaying changing burst value live inline w/ output
              time.sleep(1) # using the sleep function

'''
*************************************
* functions to print various tables *
*************************************
'''

def print_process_table():
       headers = ["Process Name", "Burst Time"] # store header names
       table = [[key, value] for key, value in listofprocesses.items()] # iterate over dict key/values and store as tuple for table
       print('\nProcesses Catalog:\n',tabulate(table, headers=headers, tablefmt="pretty"),'\n')

def print_queue_table():
       sort_dict = {k: v for k, v in sorted(active_queue.items(), key=lambda item: item[1])}
       headers = ["Order","Next Processes", "Time Remaining"]
       table = [[key, value] for key, value in sort_dict.items()]
       print('\nQueue:\n',tabulate(table, showindex=True, headers=headers, tablefmt="pretty"),'\n')

def print_completed_table():
       headers = ["Completed Processes"]
       table = [[item] for item in completed_Tasks]
       print('\n',tabulate(table, headers=headers, tablefmt="pretty"),'\n')

'''
************************************************
* Function to start the SJF Processes Program *
************************************************
'''
print("(A) to Add a process in the Ready Queue")

def SJF():
       isRunning = True
       print(" Welcome to the SJF Queue Simulation!")

       while isRunning:
              print("(E) to start executing the queue, or X to exit.")

             userInput = input() 
              
       


       pass



#run the program here
if __name__ == '__main__' :
       print_process_table()
       add_to_queue('b')
       print_queue_table()
       print_completed_table()
       #print("Current process executing: ",burst_time(7))

       




