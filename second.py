import io
import time
import subprocess
import sys
import threading

                                   
                                                                                                                              
def runcommand(cmd="", file_log = "console.log"):
	
	print cmd
	with io.open(file_log, 'wb') as writer, io.open(file_log, 'rb', 1) as reader:
		process = subprocess.Popen(cmd, stdout=writer)
		while process.poll() is None:
			sys.stdout.write(reader.read())
			time.sleep(0.5)
		# Read the remaining
		sys.stdout.write(reader.read())	
#threading.Thread(target=runcommand).start()
cmd = [r'COMMAND1',
       r'COMMAND2']
for no,i in enumerate(cmd):
    threading.Thread(target=runcommand,kwargs={"cmd":i,"file_log":"console"+str(no)}).start()
