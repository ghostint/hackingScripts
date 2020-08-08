import ftplib
import socket
import time
import sys
import os
import argparse

def help():

    print '''\n

        How to use:  ftpconnector.py ip port



    '''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', '--ipaddress', type=str)
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-u', '--url', type=str)
    args = parser.parse_args()
    
    if args.ipaddress:
        ip = args.ipaddress
    else:
        ip = str(socket.gethostbyname(args.url))

    try:
        ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp.connect((ip, args.port))
        try:
            print ftp.recv(2048)
            while True:
                comd  = raw_input('#> ')
                ftp.send(comd+' \r\n')
                print ftp.recv(4096)
        except:
            print ftp.recv(1024)
            ftp.send('agdadg\r\n')
            print ftp.recv(2048)
    except:
        pass
    ftp.close()

main()

