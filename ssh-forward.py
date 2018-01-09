#!/usr/bin/env python
from fabric.api import *

env.forward_agent = True
env.gateway = 'root@172.16.47.132'
env.hosts = ['root@172.16.47.138']

def function1():
  run('hostname')

def main():
	execute(function1)

if __name__ == '__main__':
	main()