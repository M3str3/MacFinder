#Python 3.7.9
from datetime import datetime
from distutils.command.clean import clean
import os
import argparse
import sys
from time import sleep

macs=[]
vendors={}
vendor_macs=[]

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="inputFile")
parser.add_argument("-o", "--output", help="output")
args = parser.parse_args()
argv = vars(args)
args_inputFile = argv['file']
args_output = argv['output']

def resume():
    print()
    print(f'{datetime.now()} | RESUME')
    print(f'-----------------------------------')
    for vend in vendors:
        print(f'{datetime.now()} | Vendor {vend}')
        for mc in vendors[vend]:
            print(f'{datetime.now()} | \t╚> {mc}')

def format_mac(txt_mac):
    clean = str(''.join(ch for ch in txt_mac if ch.isalnum())).strip()
    ind = 0
    mac = ''
    for i in clean:
        if ind == 2:
            mac+=':'
            ind = 1
        else:
            ind +=1
        mac += str(i)
    return mac
    
def requestVendor(txtmac):
    mc = format_mac(txtmac)
    if len(mc)==17:
        Command = 'curl https://api.macvendors.com/'+mc
        response=os.popen(Command).read()
        return response
    else:
        print(f'{datetime.now()} | {txtmac} is not a valid MAC')
        return None

if args.file:
    inputFile=args_inputFile
    inputFile = open (inputFile, 'r')
    texto = inputFile.read()
    macs=texto.split("\n")
else:
    print()
    print('\t[INFO] You can define a input file with "-f", and, you can define your output with "-o" ')
    print('\t\tEXAMPLE: python MacFinder.py -f maclist.txt -o output.txt \n\n')
    main=True
    while main:
        mac = input(f'{datetime.now()} | Write mac address or "exit" to close \n{datetime.now()} | ')
        if mac.lower() == 'exit':
            if len(vendors)>=1:
                resume()
            sys.exit()
        vendor = requestVendor(mac)
        print(f'{datetime.now()} | {mac} => {vendor}\n')
        if vendor not in vendors:
            vendors[vendor]=[]
        vendors[vendor].append(mac)

# 
if args.output:
    output_file=open(args_output,'w')
else:
    output_file=None

for RAWmac in macs:
    resp = requestVendor(RAWmac)
    sleep(1.1)
    mac = format_mac(RAWmac)
    if resp==None or len(resp)>60:
        continue
    if '{"errors":{"detail":"Not Found"}}' in resp:
        resp='Unknown'
    if output_file is not None:
        output_file.write(f'[{mac}] - {resp} \n')
    if resp not in vendors:
        vendors[resp]=[]
    vendors[resp].append(mac)
    print(f"\n Mac -> {mac} Vendor -> {resp} \n")
resume()
