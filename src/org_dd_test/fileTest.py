
import os

def make_text_file():
    a=open('test.txt','w')
    a.write("This is how you create a new text file")
    a.close
    print ("Creat Success")

def add_some_text():
    a=open('test.txt',"a")
    a.write("Here add hy love dd")
    a.close
    
def readText():
    a=open('test.txt',"r")
    print(a.read())
    
def lines_lengths():    
    a=open("test.txt","r")
    text=a.readlines()
    for line in text:
     print(line)
     
def deleteFile():   
    a=open("test.txt","r")  
   #  del a
    # a.close
    
if __name__ == '__main__':
     make_text_file()
    #add_some_text()
    #readText()
   # lines_lengths()