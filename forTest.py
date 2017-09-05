import os
import time

def MainMenu() :
	"present main menu "
	print("\n --------------------------------------- \n")
	print ("\n1-Make new directory & file for this date \n")
	print ("2-Read a file\n")
	x =input ("Enter the number of your choice please : \n")
	return (x)



def write(file):
	"write in file"
	str=input ("\n enter your memories : \n")
	file.write(str)
	file.close()
	print ("your memories was saved ... \n")



def Make_directory():
	"make new directory for files"
	str=time.asctime()
	namedir=str[4:7]+str[8:10]+str[19:24]
	try: 
		os.mkdir(namedir)
		print ("Directory was created\n")
	except FileExistsError : print("this file was existed ... ")
	Make_file(namedir)
	b=input ("\n If you want to go to main menu enter number -1\n")
	return b
	


def Make_Maindirectory():
	"make main directory"
	try : os.mkdir ("The_Notebook") #make MAIN directory
	except FileExistsError: print("")
	dir=os.getcwd() #Keep location of MAIN directory
	return dir 
  

def Make_file(namedir):
	"make new file"
	os.chdir(namedir)
	x=input("enter 1 for appending & enter 2 for writing \n")
	if (x=='1'):
		file=open(namedir+".txt","a")
		write(file)
	if (x=='2'):
		file=open(namedir+".txt","w")
		write(file)



def read_file(dir):
	"read a file from memories"
	print ("\n ------------------------------ \n")
	print ("\n list of files in The_Notebook: \n",os.listdir(dir+"\The_Notebook"))
	print ("\n ------------------------------ \n")
	x=input ("  enter the name of folder : \n")
	try: 
		os.chdir(x)
	except FileNotFoundError: print("this file dosent exist")
	print ("\n ------------------------------ \n")
	try:
		filecc=open(x+".txt","r")
		print ("\n ------------------------------ \n")
		print(filecc.read(),"\n")
	except IOError:
		print ("Error: can not find file \n")
	b=input ("\n If you want to go to main menu enter number -1\n")
	return b


dir=Make_Maindirectory()
b='-1'
while b=='-1':
	os.chdir(dir+"\The_Notebook")
	x=MainMenu()
	if ( x  == '1' ) : b=Make_directory() #make directory for memories of one date
	if ( x  == '2' ) : b=read_file(dir)


a=input()
