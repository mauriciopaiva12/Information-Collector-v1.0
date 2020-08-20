#------ IMPORTS OF LIBRARIES ------#

import socket
import sys
import dns.resolver
import time
import requests

#------------#

#------ GLOBAL VARIABLES ------#

port_pattern = [21, 22, 23, 25, 53, 80, 110, 135, 136, 137, 138, 139, 143, 443, 631, 3306, 3389]
all_ports = range(65535)

#------------#

#------ PRESENTATION ------#

print('\n' + '-'*53 + '\n' + '--'*8 + 'Information Collector' + '--'*8 + '\n' + '-'*24 + 'V.1.2' + '-'*24 + '\n')
print(' - For more information about the application, read the attachment "README.md" ')
print('\n' + '-'*59 + '\n')

#------------#

#------ FIRST QUESTION ------#

question1 = input('Save the output?[Y/N]: ')
print('\n' + '-'*59 + '\n')
question2 = input(' Do you want to use the full program or just portscan?[F/P]: ')
print('\n' + '-'*59 + '\n')

#------------#

#------ EXECUTION ------#

if(question1 == 'N' or question1 == 'n'):
    if(question2 == 'P' or question2 == 'p'):
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
    elif(question2 == 'F' or question2 == 'f'):
        print('---'*4 + 'FULL' + '---'*4)
        print('\n' + '-'*59 + '\n')
        target = str(input('Target: '))
        print('\n' + '-'*59 + '\n')
        print('---'*4 + ' Word List ' + '---'*4 + '\n')
        subdo = str(input('(Small/Medium/Big)[S/M/B]: '))
        print('\n' + '-'*59 + '\n')
        type_in = input('[A/AAAA/MX/NS/TXT]: ')
        print('\n' + '-'*59 + '\n')
        dire = str(input('Show Directory Scan? [Y / N]: '))
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
        
        url_http = ('http://www.{}'.format(target))
        url_https = ('https://{}'.format(target))

        print('---'*4 + 'Scan Directory' + '---'*4)
        print('\n' + '-'*59 + '\n')

        if(dire == 'N' or dire == 'n'):
            try:
                arq = open('../lists/Filenames_or_Directories_All.wordlist')
                lines = arq.read().splitlines()
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!')
                print('\n' + '-'*59 + '\n')
                time.sleep(3)
                sys.exit(1)
            for line in lines:
                try:
                    diretory = ('{}/{}'.format(url_https, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code != '404'):
                        if(code != '503'):
                            print(diretory, code)
                            print('\n' + '-'*24 + '\n')
                except:
                    diretory = ('{}/{}'.format(url_http, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code != '404'):
                        if(code != '503'):
                            print(diretory, code)
                            print('\n' + '-'*24 + '\n')
        elif(dire == 'Y' or dire == 'y'):
            try:
                arq = open('../lists/Filenames_or_Directories_All.wordlist')
                lines = arq.read().splitlines()
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!')
                print('\n' + '-'*59 + '\n')
                time.sleep(3)
                sys.exit(1)
            for line in lines:
                try:
                    diretory = ('{}/{}'.format(url_https, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code == '200'):
                        print(diretory, '\033[32m' + code + '\033[0;0m')
                        print('\n' + '-'*24 + '\n')
                    else:
                        print(diretory, code)
                        print('\n' + '-'*24 + '\n')
                except:
                    diretory = ('{}/{}'.format(url_http, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code == '200'):
                        print(diretory, '\033[32m' + code + '\033[0;0m')
                        print('\n' + '-'*24 + '\n')
                    else:
                        print(diretory, code)
                        print('\n' + '-'*24 + '\n')

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
elif(question1 == 'Y' or question1 == 'y'):
    out = open('OUTPUT_FULL.txt', 'w')
    if(question2 == 'P' or question2 == 'p'):
        print('---'*4 + 'PORTSCAN' + '---'*4, file=out)
        print('\n' + '-'*59 + '\n', file=out)
        ip_ps = str(input(' Target: '))
        print('Target: ' + ip_ps, file=out)
        print('\n' + '-'*59 + '\n')
        print('\n' + '-'*59 + '\n', file=out)
        port_sc = str(input(' Port (Pattern/All)[P/A]: '))
        print('\n' + '-'*59 + '\n')
        if(port_sc == 'P' or port_sc == 'p'):
            print('SCANNING...', file=out)
            print('\n' + '-'*59 + '\n', file=out)
            for port in port_pattern:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.05)
                code = client.connect_ex((ip_ps, port))
                code_transfer = str(code)
                if(code_transfer == '0'):
                    print('Port: {} <----> '.format(port) + '\033[32m' + 'OPEN' + '\033[0;0m', file=out)
                    print('\n' + '-'*24 + '\n', file=out)
                else:
                    print('Port: {} <----> '.format(port) + '\033[31m' + 'CLOSE' + '\033[0;0m', file=out)
                    print('\n' + '-'*24 + '\n', file=out)
            print('SCANNING COMPLETED', file=out)
            print('\n' + '-'*59 + '\n', file=out)
        elif(port_sc == 'A' or port_sc == 'a'):
            print('The full scan can take a while!', file=out)
            print('\n' + '-'*59 + '\n', file=out)
            print('SCANNING...', file=out)
            print('\n' + '-'*59 + '\n', file=out)
            for port in all_ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.05)
                code = client.connect_ex((ip_ps, port))
                code_transfer = str(code)
                if(code_transfer == '0'):
                    print('Port: {} <----> '.format(port) + '\033[32m' + 'OPEN' + '\033[0;0m', file=out)
                    print('\n' + '-'*24 + '\n', file=out)
                print('SCANNING COMPLETED', file=out)
                print('\n' + '-'*59 + '\n', file=out)
        else:
            print('\033[31m' + 'SCANNING FAILED' + '\033[0;0m', file=out)
            print('\n' + '-'*59 + '\n', file=out)
        out.close()
        print('---'*4 + 'End' + '---'*4)
    elif(question2 == 'F' or question2 == 'f'):
        print('---'*4 + 'FULL' + '---'*4)
        print('\n' + '-'*59 + '\n')
        target = str(input('Target: '))
        print('Target: ' + target, file=out)
        print('\n' + '-'*59 + '\n')
        print('\n' + '-'*59 + '\n', file=out)
        print('---'*4 + ' Word List ' + '---'*4 + '\n')
        print('---'*4 + ' Word List ' + '---'*4 + '\n', file=out)
        subdo = str(input('(Small/Medium/Big)[S/M/B]: '))
        print('\n' + '-'*59 + '\n')
        type_in = input('[A/AAAA/MX/NS/TXT]: ')
        print('\n' + '-'*59 + '\n')
        dire = str(input('Show Directory Scan? [Y / N]: '))
        print('\n' + '-'*59 + '\n')
        if(subdo == 'S' or subdo == 's'):
            try:
                arq = open('../lists/Filenames_or_Directories_Common.wordlist')
                subs = arq.read().splitlines()
                print('---'*4 + 'DNS BRUTE FORCE' + '---'*4, file=out)
                print('\n' + '-'*59 + '\n', file=out)
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!', file=out)
                print('\n' + '-'*59 + '\n', file=out)
                time.sleep(3)
                sys.exit(1)
            for sub in subs:
                try:
                    host = ('{}.{}'.format(sub, target))
                    results = dns.resolver.resolve(host, type_in)
                    for result in results:
                        print('\033[32m' +'TARGET: ' '\033[0;0m' + '{} <----> IP: {} <----> {}'.format(host, result, type_in), file=out)
                        print('\n' + '-'*24 + '\n', file=out)
                except:
                    a = 1
        elif(subdo == 'M' or subdo == 'm'):
            try:
                arq = open('../lists/Filenames_or_Directories_Extra.wordlist')
                subs = arq.read().splitlines()
                print('---'*4 + 'DNS BRUTE FORCE' + '---'*4, file=out)
                print('\n' + '-'*59 + '\n', file=out)
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!' + '\033[0;0', file=out)
                print('\n' + '-'*59 + '\n', file=out)
                time.sleep(3)
                sys.exit(1)
            for sub in subs:
                try:
                    host = ('{}.{}'.format(sub, target))
                    results = dns.resolver.resolve(host, type_in)
                    for result in results:
                        print('\033[32m' +'TARGET: ' '\033[0;0m' + '{} <----> IP: {} <----> {}'.format(host, result, type_in), file=out)
                        print('\n' + '-'*24 + '\n', file=out)
                except:
                    a = 1
        elif(subdo == 'B' or subdo == 'b'):
            try:
                arq = open('../lists/Filenames_or_Directories_All.wordlist')
                subs = arq.read().splitlines()
                print('---'*4 + 'DNS BRUTE FORCE' + '---'*4, file=out)
                print('\n' + '-'*59 + '\n', file=out)
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!' + '\033[0;0m', file=out)
                print('\n' + '-'*59 + '\n', file=out)
                time.sleep(3)
                sys.exit(1)
            for sub in subs:
                try:
                    host = ('{}.{}'.format(sub, target))
                    results = dns.resolver.resolve(host, type_in)
                    for result in results:
                        print('\033[32m' +'TARGET: ' '\033[0;0m' + '{} <----> IP: {} <----> {}'.format(host, result, type_in), file=out)
                        print('\n' + '-'*24 + '\n', file=out)
                except:
                    a = 1
        else:
            print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m', file=out)
            print('\n' + '-'*59 + '\n', file=out)
            time.sleep(4)
            sys.exit(1)
        
        url_http = ('http://www.{}'.format(target))
        url_https = ('https://{}'.format(target))

        print('---'*4 + 'Scan Directory' + '---'*4, file=out)
        print('\n' + '-'*59 + '\n', file=out)

        if(dire == 'N' or dire == 'n'):
            try:
                arq = open('../lists/Filenames_or_Directories_All.wordlist')
                lines = arq.read().splitlines()
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!' + '\033[0;0m', file=out)
                print('\n' + '-'*59 + '\n', file=out)
                time.sleep(3)
                sys.exit(1)
            for line in lines:
                try:
                    diretory = ('{}/{}'.format(url_https, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code != '404'):
                        if(code != '503'):
                            print(diretory, code, file=out)
                            print('\n' + '-'*24 + '\n', file=out)
                except:
                    diretory = ('{}/{}'.format(url_http, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code != '404'):
                        if(code != '503'):
                            print(diretory, code, file=out)
                            print('\n' + '-'*24 + '\n', file=out)
        elif(dire == 'Y' or dire == 'y'):
            try:
                arq = open('../lists/Filenames_or_Directories_All.wordlist')
                lines = arq.read().splitlines()
            except:
                print('\033[31m' + 'For some reason a necessary file was not found! So the program will end!' + '\033[0;0m', file=out)
                print('\n' + '-'*59 + '\n', file=out)
                time.sleep(3)
                sys.exit(1)
            for line in lines:
                try:
                    diretory = ('{}/{}'.format(url_https, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code == '200'):
                        print(diretory, '\033[32m' + code + '\033[0;0m', file=out)
                        print('\n' + '-'*24 + '\n', file=out)
                    else:
                        print(diretory, code, file=out)
                        print('\n' + '-'*24 + '\n', file=out)
                except:
                    diretory = ('{}/{}'.format(url_http, line))
                    request = requests.get(diretory)
                    code = str(request.status_code)
                    if(code == '200'):
                        print(diretory, '\033[32m' + code + '\033[0;0m', file=out)
                        print('\n' + '-'*24 + '\n', file=out)
                    else:
                        print(diretory, code, file=out)
                        print('\n' + '-'*24 + '\n', file=out)

        else:
            print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m', file=out)
            print('\n' + '-'*59 + '\n', file=out)
            time.sleep(4)
            sys.exit(1)

        try:
            print('---'*4 + 'PORTSCAN' + '---'*4, file=out)
            print('\n' + '-'*59 + '\n', file=out)
            print('SCANNING...', file=out)
            print('\n' + '-'*59 + '\n', file=out)
            for port in port_pattern:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.1)
                code = client.connect_ex((target, port))
                code_transfer = str(code)
                if(code_transfer == '0'):
                    print('PORT: {} <----> '.format(port) + '\033[32m' + 'OPEN' + '\033[0;0m', file=out)
                    print('\n' + '-'*24 + '\n', file=out)
                else:
                    print('PORT: {} <----> '.format(port) + '\033[31m' + 'CLOSE' + '\033[0;0m', file=out)
                    print('\n' + '-'*24 + '\n', file=out)
            print('SCANNING COMPLETED', file=out)
            print('\n' + '-'*59 + '\n', file=out)
        except:
            print('\033[31m' + 'SCANNING FAILED' + '\033[0;0m', file=out)
            print('\n' + '-'*59 + '\n', file=out)
        out.close()
        print('---'*4 + 'End' + '---'*4)

    else:
        print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m', file=out)
        print('\n' + '-'*59 + '\n', file=out)
        out.close()
        print('---'*4 + 'End' + '---'*4)
        time.sleep(4)
        sys.exit(1)

    #------------#
else:
    print('\033[33m' + 'Command not identified. Going out!' + '\033[0;0m', file=out)
    print('\n' + '-'*59 + '\n', file=out)
    out.close()
    print('---'*4 + 'End' + '---'*4)
    time.sleep(4)
    sys.exit(1)