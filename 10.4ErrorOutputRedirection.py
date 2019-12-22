#sys module also has attributes for stdin, stdout and stderr
import sys
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.exit() #to terminate a script