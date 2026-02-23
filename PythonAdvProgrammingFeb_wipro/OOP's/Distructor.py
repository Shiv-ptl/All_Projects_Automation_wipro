#Destructor - When we want to destroy the object
#post condition - closing of the browser , db connection closing , releasing of certain resources
#clean up operations
#for proper memory usages destructors should be used
#When db connection hs to be closed
# Destructors - when we want to destroy the object
# post conditions - cloisng of the browser , db coonectinon closing , reasing of certian resources
# clean up operations
# for  proper memory usage destcrutors should  be used
#  when db connection has to be closed -
# free the memory (garbage collection) which is automatically called
# Destructor runs when program ends or object is garbage-collected.

#

class Desct:
    def __init__(self):
        print("constructor clled-> Object Created")

    def __del__(self):
        print("Destructor called->closing the db connection........")
        print("db connection closed.")

a = Desct()

print("End of the program.")
del a


class FileHandling:
    def __init__(self,filename):
        self.file = open(filename,"w")
        print("File Opened")

    def write_data(self,data):
        self.file.write(data)
        print("Data writtento the File.")

    def readfile(self,filename):
        print("Reading the file")

    def __del__(self):
        self.file.close()
        print("File closed using destructor.")

f1 = FileHandling("intro.txt")
f1.write_data("Hello, this is wipro python class.")
f1.readfile("intro.txt")
del f1


