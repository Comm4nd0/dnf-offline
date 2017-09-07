#!/usr/bin/python3
import urllib.request
import os

def intro():
    print("""
    Welcome to dnf downloader!
    
    Enter the name of the file you want to install on an offline system
    and this program will download the file and ALL dependencies!""")

def menu():
    print("""
    [1] - Download file and all dependencies
    [2] - Only download individual file
    [99] - Exit
    """)
    choice = int(input("Choice: "))

    if choice == 1:
        get_all()

    elif choice == 99:
        exit()

def get_all():
    file_name = get_file_name()

    #download file
    path = 'ftp://rpmfind.net/linux/fedora/linux/updates/26/x86_64/p/' + file_name + '.rpm'
    urllib.request.urlretrieve(path, os.getcwd() + '/rpm/' + file_name + '.rpm')




def get_file_name():
    file_name = str(input("Enter file name: "))

    return file_name

def main():
    intro()
    while True:
        menu()

if __name__ == '__main__':
    main()