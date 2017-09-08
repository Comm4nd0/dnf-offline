#!/usr/bin/python3
import urllib.request
import os
from subprocess import check_output

RPM_TO_DL = []

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
        download()

    elif choice == 99:
        exit()

def get_all():
    file_name = get_file_name()

    RPM_TO_DL.append(file_name)
    # enter dnf command to find dependencies

    for item in RPM_TO_DL:
        stdout = check_output(['dnf', 'repoquery', '--deplist', item])
        stdout = stdout.decode('utf-8')
        #print(type(stdout))
        stdout = stdout.split('\n')
        #print(stdout)

        for line in stdout:
            if 'provider: ' in line:
                package_name = line[line.index('provider: ') + 10:]
                if package_name not in RPM_TO_DL:
                    RPM_TO_DL.append(package_name)

def download():
    # download file
    for file_name in RPM_TO_DL:
        file_copy = file_name
        front = 0
        while True:
            name_split = file_copy.index('-')
            try:
                int(file_copy[name_split + 1:name_split + 2])
                file_name = file_name[:name_split+front]
                print(file_name)
                break
            except ValueError:
                print('split!')
                front += len(file_copy[:name_split])
                file_copy = file_copy[name_split+1:]
            except Exception as err:
                print(err)
                break

        fp = urllib.request.urlopen('http://rpmfind.net/linux/rpm2html/search.php?query=' + file_name)
        mybytes = fp.read()
        mystr = mybytes.decode('utf8')
        fp.close()
        try:
            trim = mystr[mystr.index('Fedora 26 for x86_64'):]
            link_start = trim.index('ftp://')
            link_end = trim.index('.rpm')
            path = trim[link_start:link_end+4]

            urllib.request.urlretrieve(path, os.getcwd() + '/rpm/' + file_name + '.rpm')
        except Exception as err:
            print(Err)
            print(path)

def get_file_name():
    file_name = str(input("Enter file name: "))

    return file_name

def main():
    intro()
    while True:
        menu()

if __name__ == '__main__':
    main()