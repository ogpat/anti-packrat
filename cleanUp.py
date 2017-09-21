import os
import glob
from datetime import date
import shutil

#naming convention for directory
def generate_dir_name(dirName):
    #better way to do this is to use the os.join
    tdate = date.today()
    tdate = tdate.strftime('%m%d%y')
    new_folder = "/Users/MrHughes/Documents/"+ dirName+tdate
    global global_path_1 
    global_path_1 = new_folder
    global global_dir_name 
    global_dir_name = dirName
    os.makedirs(new_folder)

#the listdir() function doesn't seem to be working 
def show_folder():
    dst = '/Users/MrHughes/Documents/python-code'
    os.chdir(dst)
    #go to the folder and show the contents of the folder
    show = input("Would you like to see the contents of the folder? [Y/N]")
    if show.upper() == 'Y':
        print('Here are your files in the {} directory : '.format(dst))
        os.listdir()
    if show.upper() == 'N':
        print('Exiting ...')
    

def clean_up_ppt():
    
    global global_path_1
    for file in glob.glob('*.pptx'):
        #get the path of each file
        fromPath = os.path.abspath(file)
        #change the location of file
        shutil.move(fromPath, global_path_1)
    print('All PowerPoint files are cleaned up! Does someone smell lemon citrus?')

def clean_up_word():
    
    global global_path_1
    for file in glob.glob('*.docx'):
        #get the path of each file
        fromPath = os.path.abspath(file)
        #change the location of file
        shutil.move(fromPath, global_path_1)
    print('All Word files are cleaned up! Does someone smell Lysol?') 
    
       
'''
def func_dm():
    global global_path_1
    for file in glob.glob('*.docx'):
        fromPath = os.path.abspath(file)
        shutil.move(fromPath, global_path_1)
        
def dirDescription(pathCheck):
    """ Gives the description recursively of the folders and files with in each folder. shows the tree basically. """
    for dirpath, dirnames, filenames in os.walk(path)
    print 
    
'''


global_path_1 = ''
global_path_2 = None
global_dir_name = ''


#file path to search
print(os.getcwd())
documentsFolder = '/Users/MrHughes/Documents'
os.chdir(documentsFolder)
print(os.getcwd())
userDirName = input("Enter the name of the directory to store you semester files: ")
generate_dir_name(userDirName)
#Confirm message
print('Folder {} was created at this location : {}'.format(global_dir_name, global_path_1))
print("You are currently in: " + os.getcwd())
clean_up_ppt()

