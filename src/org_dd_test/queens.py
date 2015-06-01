'''
@author: LENOVO
'''
import random
import os

def conflict(state,nextX):
  nextY=len(state)
  for i in range(nextY):
      if abs(state[i]-nextX) in (0,nextY-i):
          return True
      return False
  
def queens(num,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield(pos,)
            else: 
                for result in queens(num,state+(pos,)):  
                    yield(pos,)+result
                    
def prettyprint(solution):
     def line(pos, length=len(solution)):
         return '. '*(pos)+'X'+'.'*(length-pos-1)
     for pos in solution:
         print line(pos)
         

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
    
     #make_text_file()
    #add_some_text()
    #readText()
   # lines_lengths()
        prettyprint(random.choice(list(queens(8))))