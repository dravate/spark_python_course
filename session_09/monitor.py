
import subprocess
def disk (partition="/"):
     print ("The Partition is: ", partition)
     info = subprocess.call(["df", partition]) 

if __name__ == '__main__':
     disk()