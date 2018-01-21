# Developed By : NIRANJAN KUMAR G S 
# From : INDIA
# Email : niranjan4@outlook.in
# Updated date : 12/Dec/2017


from multiprocessing import Process
import os ,time, threading,sys
from datetime import datetime

    
def first():
    
    for i in range(10):
        #time.sleep(1)
        print('first', datetime.now(),name)

   
def second():
           
    for i in range(10):   
        print('second', datetime.now(),name)


def three():
           
    for i in range(10):   
        print('three', datetime.now(),name)


def four():
           
    for i in range(10):   
        print('four', datetime.now())
def naming():
    global name
    name='niranjan'
    print name

                
if __name__ == '__main__':
    naming()
    #time.sleep(2)
    if 'one' in sys.argv and len(sys.argv) == 2:

        threading.Thread(target=first).start()

    elif 'one' and 'two' in sys.argv and len(sys.argv) == 3:

        threading.Thread(target=first).start()
        threading.Thread(target=second).start()

    elif 'one' and 'two' and 'three' in sys.argv and len(sys.argv) == 4:

        threading.Thread(target=first).start()
	threading.Thread(target=second).start()        
	threading.Thread(target=three).start()
	
    elif 'one' and 'two' and 'three' and 'four' in sys.argv and len(sys.argv) == 5:

        threading.Thread(target=first).start()
        threading.Thread(target=second).start()
	threading.Thread(target=three).start()
	threading.Thread(target=four).start()
    else:

        print"no arguments passed"
