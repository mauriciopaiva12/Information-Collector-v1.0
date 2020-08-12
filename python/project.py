#------ IMPORTS OF LIBRARIES ------#

import socket
import sys
import dns.resolver
import time

#------------#

#------ GLOBAL VARIABLES ------#

port_pattern = [21, 22, 23, 25, 53, 80, 110, 135, 136, 137, 138, 139, 143, 631, 3306, 3389]
all_ports = range(65535)

a = 0

#------------#

#------ PRESENTATION ------#

print('\n' + '-'*59 + '\n' + '---'*4 + 'Information Collector' + '---'*4 + '\n' + '-'*24 + 'V.1.0' + '-'*24 + '\n')
print(' - For more information about the application, read the attachment "INFO.txt" ')
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
            client.settimeout(0.1)
            code = client.connect_ex((ip_ps, port))
            code_transfer = str(code)
            if(code_transfer == '0'):
                print('Port: {} <----> OPEN'.format(str(port)))
                print('\n' + '-'*24 + '\n')
            else:
                print('Port: {} <----> CLOSE'.format(str(port)))
                print('\n' + '-'*24 + '\n')
        print('SCANNING COMPLETED')
        print('\n' + '-'*59 + '\n')
    elif(port_sc == 'A' or port_sc == 'a'):
        print('SCANNING...')
        print('\n' + '-'*59 + '\n')
        for port in all_ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            code = client.connect_ex((ip_ps, port))
            code_transfer = str(code)
            if(code_transfer == '0'):
                print('Port: {} <----> OPEN'.format(port))
                print('\n' + '-'*24 + '\n')
            else:
                a = a + 1
    else:
        print('\033[31m' + 'SCANNING FAILED' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
elif(question == 'F' or question == 'f'):
    print('---'*4 + 'COMPLETE PROGRAM' + '---'*4)
    print('\n' + '-'*59 + '\n')
    target = str(input('Target: '))
    print('\n' + '-'*59 + '\n')
    subdo = str(input('Which type of world list do you want to use? (Small / Medium / Large)[S/M/L]: '))
    print('\n' + '-'*59 + '\n')
    if(subdo == 'S' or subdo == 's'):
        type_inp = str(input('[A/AAAA/MX/TXT/NS]: '))
        print('\n' + '-'*59 + '\n')
        try:
            arq = open('smal.txt')
            line = arq.read().splitlines()
        except:
            print('\033[33m' + 'For some reason, the required file could not be found. Therefore, the program will end' + '\033[0;0m')
            print('\n' + '-'*59 + '\n')
            time.sleep(10)
            sys.exit(1)
        for sub in line:
            host = ('{}.{}'.format(sub, target))
            results = dns.resolver.resolve(host, type_inp)
            for result in results:
                print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <====> IP: {} <====> {}'.format(host, result, type_inp))
                print('\n' + '-'*59 + '\n')
        print('SCANNING...')
        print('\n' + '-'*59 + '\n')
    elif(subdo == 'M' or subdo == 'm'):
        print('\033[33m' + 'Unfortunately there is still no other world list, but I am working on it. I apologize for the inconvenience.' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
        time.sleep(10)
        sys.exit(1)
#        type_inp = input('[A/AAAA/MX/TXT/NS]: ')
#        print('\n' + '-'*59 + '\n')
#        try:
#            arq = open('../word_lists/medium.txt')
#            line = arq.read().splitlines()
#        except:
#            print('\033[33m' + 'For some reason, the required file could not be found. Therefore, the program will end' + '\033[0;0m')
#            print('\n' + '-'*59 + '\n')
#            time.sleep(10)
#            sys.exit(1)
#        for sub in line:
#            host = ('{}.{}'.format(sub, target))
#            results = dns.resolver.resolve(host, type_inp)
#            for result in results:
#                print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <====> IP: {} <====> {}'.format(host, result, type_inp))
#                print('\n' + '-'*59 + '\n')
    elif(subdo == 'B' or subdo == 'b'):
        print('\033[33m' + 'Unfortunately there is still no other world list, but I am working on it. I apologize for the inconvenience.' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
        time.sleep(10)
        sys.exit(1)
#        type_inp = input('[A/AAAA/MX/TXT/NS]: ')
#        print('\n' + '-'*59 + '\n')
#        try:
#            arq = open('../word_lists/big.txt')
#            line = arq.read().splitlines()
#        except:
#            print('\033[33m' + 'For some reason, the required file could not be found. Therefore, the program will end' + '\033[0;#0m')
#            print('\n' + '-'*59 + '\n')
#            time.sleep(10)
#            sys.exit(1)
#        for sub in line:
#            host = ('{}.{}'.format(sub, target))
#            results = dns.resolver.resolve(host, type_inp)
#            for result in results:
#                print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <====> IP: {} <====> {}'.format(host, result, type_inp))
#                print('\n' + '-'*59 + '\n')
    else:
        print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
        time.sleep(10)
        sys.exit(1)
    
    try:
        print('Scanning...')
        print('\n' + '-'*59 + '\n')
        for port in port_pattern:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            code = client.connect_ex((target, port))
            code_transfer = str(code)
            if(code_transfer == '0'):
                print('Port: {} <----> OPEN'.format(str(port)))
                print('\n' + '-'*24 + '\n')
            else:
                print('Port: {} <----> CLOSE'.format(str(port)))
                print('\n' + '-'*24 + '\n')
        print('Scanning completed')
        print('\n' + '-'*59 + '\n')
    except:
        print('\033m[31m' + 'Scanning failed' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
    pass
    print('PROGRAMMING COMPLETED')
    print('\n' + '-'*59 + '\n')

else:
        print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m')
        print('\n' + '-'*59 + '\n')
        time.sleep(10)
        sys.exit(1)

#------------#