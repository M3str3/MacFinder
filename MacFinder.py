#Python 3.7.9
from datetime import datetime
import os
import argparse
import sys
from time import sleep

###########################################################################

macs=[]
vendors={}
vendor_macs=[]

###########################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="inputFile")
parser.add_argument("-o", "--output", help="output")
args = parser.parse_args()
argv = vars(args)
args_inputFile = argv['file']
args_output = argv['output']

def requestVendor(mc):
    mc = str(mc).reaplce('-','').replace(':','').strip()
    if len(mc)=12
        Command = 'curl https://api.macvendors.com/'+mc
        response=os.popen(Command).read()
        return response
    else:
        print(f'{datetime.now()} | {mc} is not a valid MAC')

if args.file:
    inputFile=args_inputFile
    inputFile = open (inputFile, 'r')
    texto = inputFile.read()
    macs=texto.split("\n")
else:
    print('\t[INFO] You can define a input file with "-f", and, you can define your output with "-o" ')
    print('\tEXAMPLE: python MacFinder.py -f maclist.txt -o output.txt \n\n')
    main=True
    while main:
        mac = input(f'{datetime.now()} | Write mac address or "exit" to close \n{datetime.now()} | ')
        if mac.lower() == 'exit':
            sys.exit()
        print(f'{datetime.now()} | {mac} => {requestVendor(mac)}\n')

if args.output:
    output_file=open(args_output,'w')
else:
    output_file=None

for mac in macs:
    resp = requestVendor(mac)
    sleep(1.1)
    if len(resp)>60:
        continue
    if '{"errors":{"detail":"Not Found"}}' in resp:
        resp='Unknown'
    if output_file is not None:
        output_file.write(f'[{mac}] - {resp} \n')
    if resp not in vendors:
        vendors[resp]=[]
    vendors[resp].append(mac)
    print(f"\n Mac -> {mac} Vendor -> {resp} \n")
    
print(f'{datetime.now()} | RESUME')
print(f'-----------------------------------')
for vend in vendors:
    print(f'{datetime.now()} | Vendor {vend}')
    for mc in vendors[vend]:
        print(f'{datetime.now()} | \t╚{mc}')

    
