#os module provides dozen of functions for interacting with operating system.
import os
print(os.getcwd())      # Return the current working directory
os.chdir('/windows')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
