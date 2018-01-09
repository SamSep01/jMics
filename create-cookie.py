#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time
import sys
import argparse
import glob
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
colors = [G,R,B,P,C,O,GR]

current_path = os.path.dirname(os.path.realpath(__file__))

# def create_dir(dir_name):
# 	if not os.path.exists(dir_name):
# 		os.makedirs(dir_name)

# create_dir('output')
def cowsay():
	print ("""{1}
	  -----------------------------
	< You didn't say the {2}MAGIC WORD{1} >
	  ----------------------------- 
	         \   ^__^
	          \  (oo)\_______
	             (__)\       )\/
	             	\||----w |
	                 ||     ||
	""".format(C, G, P))

	# "expirationDate": 1576344852,
cookie_template = '''
{
	"domain": "[domain]",
	"hostOnly": false,
	"httpOnly": false,
	"name": "[name]",
	"path": "/",
	"sameSite": "no_restriction",
	"secure": fals	e,
	"session": false,
	"storeId": "1",
	"value": "[value]",
	"id": [id]
}'''

argv = {
	'intput' : '',
	'text' : '',
	'output' : ''
}

def create_cookie():

	input_file = argv['input']
	text = argv['text']
	domain = argv['domain'].strip()
	output = argv['output']
	final = []
	cookies = []
	out_file = []

	if input_file != 'None':
		with open(input_file, 'r') as i:
			data = i.read()
	elif text != 'None':
		data = text

	cookie_data = data.split(';')
	for c in cookie_data:
		print("{0}[*] Handling cookie: {1}".format(G, c))
		item = c.split('=')
		cookie = cookie_template.replace('[domain]',domain)
		cookie = cookie.replace('[name]',item[0])
		cookie = cookie.replace('[value]',item[1])
		cookies.append(cookie)

	# final.append('[')
	for i in range(len(cookies)):
		final.append(cookies[i].replace('[id]', str(i + 1)))
	# final.append(']')

	final_cookie = '[' + ','.join(final) + ']'
	print(final_cookie)
	# all_file = glob.glob(folder + '*')

	# for f in all_file:
	# 	with open(f, 'r') as i:
	# 		content = i.read()
	# 	if text in content:
	# 		ip = f.split('_')[2].strip()
	# 		with open(f, 'r') as i:
	# 			data = i.readlines()
	# 		for line in data:
	# 			if match in line:
	# 				print('{0}====[ {1} ]===='.format(B, ip))
	# 				print(G + line)
	# 				print('{0}====[ ##### ]===='.format(B))

	# 		final.append(ip)
	# 		out_file.append(f)

	# print("{0}[*] List ip match the text: ".format(G))
	# print('{}'.format(P)+ '=' * 40)

	# print(G,end='')
	# for i in final:
	# 	print(i)

	# # print(G)
	# # print(final)
	# if output != 'None':
	with open(output, 'w') as o:
		o.write(final_cookie)
	# 		for i in out_file:
	# 			o.write(i + '\n')

	print('{}'.format(P)+ '=' * 40)
	print("{1}[*] Check your output in: {0}".format(output, G))
	print('{}'.format(P)+ '=' * 40)
	print(W)
	

def main():
	cowsay()
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input' , action='store', dest='INPUT', help='Name of input file')
	parser.add_argument('-d','--domain' , action='store', dest='DOMAIN', help='Name of input file')
	parser.add_argument('-s','--string' , action='store', dest='STRING', help='Text to search')
	parser.add_argument('-o','--output' , action='store', dest='OUTPUT', help='Name of output file')
	results = parser.parse_args()

	if len(sys.argv) == 1:
		print("""{}
Usage: python3 create-cookie.py [-h] [-i INPUT] [-o OUTPUT]

Example: 
	$python3 create-cookie.py -i <input>  -s <text> -o <output>

		  """.format(G))
		exit(0)

	argv['input'] = str(results.INPUT)
	argv['domain'] = str(results.DOMAIN)
	argv['text'] = str(results.STRING)
	argv['output'] = str(results.OUTPUT)

	create_cookie()


if __name__ == '__main__':
	main()




