#Python 3.7.9
try:
    from art import *
    from termcolor import colored
    tprint('MacFinder', font="sub-zero")
    print(colored('Created by Mestre',"green"))
except:
    print('')

from email import header
import os
import argparse
from time import sleep

macs=[]

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="fichero")
parser.add_argument("-o", "--output", help="output")
args = parser.parse_args()
argv = vars(args)
args_fichero = argv['file']
args_output = argv['output']

if args.file:
    fichero=args_fichero
else:
    print('[*]ERROR - Pls define a file with "-f", u can define your output with "-o" ')
    print('EXAMPLE: python MacFinder.py -f maclist.txt -o output.txt')
    quit()

fichero = open (fichero, 'r')
texto = fichero.read()
macs=texto.split("\n")

if args.output:
    output_file=open(args_output,'w')
else:
    output_file=open('output.txt','w')

for mac in macs:
    comando = 'curl https://api.macvendors.com/'+mac
    x=os.popen(comando).read()
    output_file.write(mac+" ; "+(x)+"\n")
    print("\n Mac -> "+str(mac)+" Fabricante -> "+str(x)+" \n")
    sleep(1.1)

    