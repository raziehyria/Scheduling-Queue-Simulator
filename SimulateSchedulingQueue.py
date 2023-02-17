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
*FUNCTIONS USED: time, dictionary, queue, tabulate.
*
* def burst_time(burst) Helper function used to increment and display the given burst time of a process
* borrowed from Stack overflow: \https://stackoverflow.com/a/66940953/17628672
*H'''

import msvcrt
import time

import keyboard
from tabulate import tabulate

'''
***************************************************************
* declaring all the variables and data structures we will use *
***************************************************************
'''

listofprocesses = {  # the entire catalog of processes
    'A': 5,
    'B': 6,
    'C': 2,
    'D': 7,
    'E': 1,
    'F': 10,
    'G': 3,
    'H': 4}

active_queue = {  # supplemented active queue
    'G': 3,
    'F': 10,
    'A': 5}

completed_Tasks = []  # stores completed tasks


'''
***************************
* Various Helper functions *
***************************
'''


def add_to_queue(process):  # function used to store
    active_queue[process] = listofprocesses[process]


def get_next_in_queue(dict):  # a function used to get the next shortest (value) sjf task in the queue
    next_value = min(dict, key=dict.get)  # uses the min function to iterate dict to find min task
    return next_value  # returns the task


def check_status(task):
    if task in completed_Tasks or task not in listofprocesses:
        return False
    else:
        return True


def burst_time(burst):
    for i in range(burst, 0, -1):  # incrementing starting from the burst value
        print(f"{i}", end="\r", flush=True)  # displaying changing burst value live inline w/ output
        time.sleep(1)  # using the sleep function


'''
*************************************
* functions to print various tables *
*************************************
'''


def print_process_table():
    headers = ["Process Name", "Burst Time"]  # store header names
    table = [[key, value] for key, value in
             listofprocesses.items()]  # iterate over dict key/values and store as tuple for table
    print('\nProcesses Catalog:\n', tabulate(table, headers=headers, tablefmt="pretty"), '\n')


def print_queue_table():
    sort_dict = {k: v for k, v in sorted(active_queue.items(), key=lambda item: item[1])}
    headers = ["Order", "Next Processes", "Time Remaining"]
    table = [[key, value] for key, value in sort_dict.items()]
    print('\nCurrent Queue:\n', tabulate(table, showindex=True, headers=headers, tablefmt="pretty"), '\n')


def print_completed_table():
    headers = ["Completed Processes"]
    table = [[item] for item in completed_Tasks]
    print('\n', tabulate(table, headers=headers, tablefmt="pretty"), '\n')


'''
************************************************
* Function to start the SJF Processes Program *
************************************************
'''

def SJF():
    print(" Welcome to the SJF Queue Simulation!")
    print("Press (e) to start executing the queue! The program will until then...")
    keyboard.wait("e")  # waits for the user to enter proper key before starting
    isRunning = True  # start program
    
    while isRunning:
        print("Add items from the process catalog to the queue before all the queue is finished")
        print_process_table()
        print("Press (a) to Add a process in the Ready Queue")
        print_queue_table()

        while len(active_queue) > 0:

            if msvcrt.kbhit(): # if a key was hit
                chrt = msvcrt.getch() #store it
                match chrt: # execute commands depending on the key hit
                    case 'x':
                        print("You pressed: %s. Exiting the Program" % chrt)
                        print_completed_table()
                        isRunning = False
                    case 'a':
                        print("Which process would you like to add?"  )
                        usrinp = input("Enter process from list above")
                        if check_status(usrinp):
                            add_to_queue(usrinp)
                            print_queue_table
                            break
                        else:
                            print("That process is either completed or doesnt eexist!")
                            break
                    case _: # default case
                        break
            #for item in active_queue:
            minval = get_next_in_queue(active_queue) # find next smallest key value
            print("\nCurrent process on CPU: %s, eta: %d \ne "% (minval,active_queue[minval])) # display current task on cpu with burst time
            burst_time(active_queue[minval])
            print("\nProcess %s Completed! Moving to next task...")
            active_queue.pop(minval) #  after burst , pop that min key from dict into completed tasks
            completed_Tasks.append(minval)
            
        print("Queue is complete! Program Exiting")   
        isRunning = False
                      
                


# run the program here
if __name__ == '__main__':
    SJF()
