#!/usr/bin/env python3

import os, sys
import argparse
import random

# Console colors
W = '\033[1;0m'   # white 
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[1;33m'  # orange
B = '\033[1;34m'  # blue
Y = '\033[1;93m'  # yellow
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GR = '\033[1;37m'  # gray
colors = [G,B,P,W,R,C,O,GR]
argv = {
	'cmd'  : '',
	'verbose'  : '',
	'list1' : '',
	'list2' : '',
	'list3'	 : '',
	'list4' : ''
}
list1 = []


def exe_2list():
	with open(argv['list1'], 'r') as f:
		list1 = f.readlines()

	with open(argv['list2'], 'r') as f:
		list2 = f.readlines()

	cmd = argv['cmd']
	# print(cmd)
	# print(list1)
	color = iter(colors)
	for item1 in list1:
		command = cmd.replace('[1]', item1.strip())
		for item2 in list2:
			command = command.replace('[2]', item2.strip())
			try:
				print(next(color), end='')
				print("[+] Execute command: {}".format(command))
			except:
				color = iter(colors)
			if argv['verbose'] != 'None':
				ques = input("{}[!] Do you want to execute command? [y/n] ".format(next(color)))
				if ques.lower() == 'y' or ques.lower() == 'yes' or ques == '':
					pass
				else:
					continue
			os.system(command)

	for item1 in list1:
			# command = cmd.replace('[1]', item1.strip())
			# for item2 in list2:
				# command = command.replace('[2]', item2.strip())
		try:
			print(next(color), end='')
			print("[*] Exploit done for {}".format(item1))
		except:
			color = iter(colors)
				# os.system(command)



def exec_cmd():
	with open(argv['list1'], 'r') as f:
		list1 = f.readlines()

	cmd = argv['cmd']
	# print(cmd)
	# print(list1)
	color = iter(colors)
	for item in list1:
		command = cmd.replace('[1]', item.strip())
		try:
			print(next(color), end='')
			print("[+] Execute command: {}".format(command))
		except:
			color = iter(colors)
		if argv['verbose'] != 'None':
			try:
				ques = input("{}[!] Do you want to execute command? [y/n] ".format(next(color)))
			except:
				color = iter(colors)
				
			if ques.lower() == 'y' or ques.lower() == 'yes' or ques == '':
				pass
			else:
				continue
		os.system(command)

# def verbose():
# 	ques = input("{}[!] Do you want to execute command? [y/n] ".format(B))
# 	if ques.lower() == 'y' or ques.lower() == 'yes':
# 		pass
# 	else:
# 		break


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-cmd','--command' , action='store', dest='CMD', help='command')
	parser.add_argument('-l1','--list1' , action='store', dest='LIST1', help='Name of input file')
	parser.add_argument('-l2','--list2' , action='store', dest='LIST2', help='Name of input file')
	parser.add_argument('-l3','--list3' , action='store', dest='LIST3', help='Name of input file')
	parser.add_argument('-l4','--list4' , action='store', dest='LIST4', help='Name of input file')
	parser.add_argument('-v','--verbose' , action='store', dest='VERBOSE', help='verbose execute')
	results = parser.parse_args()
	if len(sys.argv) == 1:
			print("""{}Usage: python3 jBash.py -cmd "<command> [1] [2]" -l1 <name of input file> -l2 <name of input file>

Example: 
	$python3 jBash.py -cmd "ping [1] -c 4" -l1 <name of input file>
	$python3 jBash.py -cmd "ping [1] -c 4" -l1 <name of input file> --verbose y
	""".format(G))
			exit(0)


	argv['cmd'] = str(results.CMD)
	argv['list1'] = str(results.LIST1)
	argv['list2'] = str(results.LIST2)
	argv['list3'] = str(results.LIST3)
	argv['list4'] = str(results.LIST4)
	argv['verbose'] = str(results.VERBOSE)
	# print(argv)

	if argv['list2'] != 'None':
		exe_2list()
	else:
		exec_cmd()





if __name__ == '__main__':
	main()