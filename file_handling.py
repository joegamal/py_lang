# read mood 
file = open("./file_handling.txt", "r")

file.read() # this return a string with all the file content
file.readlines()# this reads a file as an array each line



#append mood modifies the content of the file without overriding the data and writes a new one
file = open("./file_handling.txt", "a")



#write mood wippes the old data and writes a new one
file = open("./file_handling.txt", "w")


#dont forget to close the file
file.close()

