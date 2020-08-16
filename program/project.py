#------ IMPORTS OF LIBRARIES ------#

import socket
import sys
import dns.resolver
import time

#------------#

#------ GLOBAL VARIABLES ------#

port_pattern = [21, 22, 23, 25, 53, 80, 110, 135, 136, 137, 138, 139, 143, 631, 3306, 3389]
all_ports = range(65535)

#------------#

#------ PRESENTATION ------#

print('\n' + '-'*53 + '\n' + '--'*8 + 'Information Collector' + '--'*8 + '\n' + '-'*24 + 'V.1.2' + '-'*24 + '\n')
print(' - For more information about the application, read the attachment "README.md" ')
print('\n' + '-'*59 + '\n')

#------------#

#------ FIRST QUESTION ------#

question = input(' Do you want to use the full program or just portscan?[F/P]: ')
print('\n' + '-'*59 + '\n')

#------------#

#------ EXECUTION ------#

if(question == 'P' or question == 'p'):
    print('---'*4 + 'PORTSCAN' + '---'*4)
    print('\n' + '-'*59 + '\n')
    ip_ps = str(input(' Target: '))
    print('\n' + '-'*59 + '\n')
    port_sc = str(input(' Port (Pattern/All)[P/A]: '))
    print('\n' + '-'*59 + '\n')
    if(port_sc == 'P' or port_sc == 'p'):
        print('SCANNING...')
        print('\n' + '-'*59 + '\n')
        for port in port_pattern:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            code = client.connect_ex((ip_ps, port))
            code_transfer = str(code)
            if(code_transfer == '0'):
                print('Port: {} <----> '.format(port) + '\033[32m' + 'OPEN' + '\033[0;0m')
                print('\n' + '-'*24 + '\n')
            else:
                print('Port: {} <----> '.format(port) + '\033[31m' + 'CLOSE' + '\033[0;0m')
                print('\n' + '-'*24 + '\n')
        print('SCANNING COMPLETED')
        print('\n' + '-'*59 + '\n')
    elif(port_sc == 'A' or port_sc == 'a'):
        print('The full scan can take a while!')
        print('\n' + '-'*59 + '\n')
        print('SCANNING...')
        print('\n' + '-'*59 + '\n')
        for port in all_ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            code = client.connect_ex((ip_ps, port))
            code_transfer = str(code)
            if(code_transfer == '0'):
                print('Port: {} <----> '.format(port) + '\033[32m' + 'OPEN' + '\033[0;0m')
                print('\n' + '-'*24 + '\n')
        print('SCANNING COMPLETED')
        print('\n' + '-'*59 + '\n')
    else:
        print('\033[31m' + 'SCANNING FAILED' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
elif(question == 'F' or question == 'f'):
    print('---'*4 + 'FULL' + '---'*4)
    print('\n' + '-'*59 + '\n')
    target = str(input('Target: '))
    print('\n' + '-'*59 + '\n')
    print('---'*4 + ' Word List ' + '---'*4 + '\n')
    subdo = str(input('(Small/Medium/Big)[S/M/B]: '))
    print('\n' + '-'*59 + '\n')
    type_in = input('[A/AAAA/MX/NS/TXT]: ')
    print('\n' + '-'*59 + '\n')
    if(subdo == 'S' or subdo == 's'):
        try:
            arq = open('../lists/Filenames_or_Directories_Common.wordlist')
            subs = arq.read().splitlines()
            print('---'*4 + 'DNS BRUTE FORCE' + '---'*4)
            print('\n' + '-'*59 + '\n')
        except:
            print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!')
            print('\n' + '-'*59 + '\n')
            time.sleep(3)
            sys.exit(1)
        for sub in subs:
            try:
                host = ('{}.{}'.format(sub, target))
                results = dns.resolver.resolve(host, type_in)
                for result in results:
                    print('\033[32m' +'TARGET: ' '\033[0;0m' + '{} <----> IP: {} <----> {}'.format(host, result, type_in))
                    print('\n' + '-'*24 + '\n')
            except:
                a = 1
    elif(subdo == 'M' or subdo == 'm'):
        try:
            arq = open('../lists/Filenames_or_Directories_Extra.wordlist')
            subs = arq.read().splitlines()
            print('---'*4 + 'DNS BRUTE FORCE' + '---'*4)
            print('\n' + '-'*59 + '\n')
        except:
            print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!')
            print('\n' + '-'*59 + '\n')
            time.sleep(3)
            sys.exit(1)
        for sub in subs:
            try:
                host = ('{}.{}'.format(sub, target))
                results = dns.resolver.resolve(host, type_in)
                for result in results:
                    print('\033[32m' +'TARGET: ' '\033[0;0m' + '{} <----> IP: {} <----> {}'.format(host, result, type_in))
                    print('\n' + '-'*24 + '\n')
            except:
                a = 1
    elif(subdo == 'B' or subdo == 'b'):
        try:
            arq = open('../lists/Filenames_or_Directories_All.wordlist')
            subs = arq.read().splitlines()
            print('---'*4 + 'DNS BRUTE FORCE' + '---'*4)
            print('\n' + '-'*59 + '\n')
        except:
            print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!')
            print('\n' + '-'*59 + '\n')
            time.sleep(3)
            sys.exit(1)
        for sub in subs:
            try:
                host = ('{}.{}'.format(sub, target))
                results = dns.resolver.resolve(host, type_in)
                for result in results:
                    print('\033[32m' +'TARGET: ' '\033[0;0m' + '{} <----> IP: {} <----> {}'.format(host, result, type_in))
                    print('\n' + '-'*24 + '\n')
            except:
                a = 1
    else:
        print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
        time.sleep(4)
        sys.exit(1)
    
    try:
        print('---'*4 + 'PORTSCAN' + '---'*4)
        print('\n' + '-'*59 + '\n')
        print('SCANNING...')
        print('\n' + '-'*59 + '\n')
        for port in port_pattern:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.1)
            code = client.connect_ex((target, port))
            code_transfer = str(code)
            if(code_transfer == '0'):
                print('PORT: {} <----> '.format(port) + '\033[32m' + 'OPEN' + '\033[0;0m')
                print('\n' + '-'*24 + '\n')
            else:
                print('PORT: {} <----> '.format(port) + '\033[31m' + 'CLOSE' + '\033[0;0m')
                print('\n' + '-'*24 + '\n')
        print('SCANNING COMPLETED')
        print('\n' + '-'*59 + '\n')
    except:
        print('\033[31m' + 'SCANNING FAILED' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')

else:
        print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
        time.sleep(4)
        sys.exit(1)

#------------#
