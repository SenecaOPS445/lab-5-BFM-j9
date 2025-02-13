#!/usr/bin/env python3
# Author ID: jowusu9

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
     f = open(file_name, 'r') 
     data = f.read()
     f.close()
     return data


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
      f = open(file_name, 'r')  
      lines = f.readlines()
      f.close
      lines = [line.strip() for line in lines]
      return lines
      
     
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))