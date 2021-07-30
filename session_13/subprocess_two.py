import subprocess

try: 
	completed = subprocess.run(['false', '-l'], check=True )
#except Exception as e: 
except subprocess.CalledProcessError as e:
   print ("Error: ", e)

#print (completed)

