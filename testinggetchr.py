import sys
import time

lx = lxTerm()

def main():
    global lx
    print("Press any key to restart the game.")
    lx.getch(True) # Standar getch, no manual needed.

    lx.start() # This will need new term
    while True:
        if lx.kbhit():
            c = lx.getch()
            c_ord = ord(c)
            print(c)
            if c_ord == 27: # ESC
                break
    lx.reset() # Reset to old term

if __name__ == "__main__":
    main()