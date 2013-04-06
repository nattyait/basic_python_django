#!/usr/bin/env python
#-*-coding: utf-8 -*-

import requests
from BeautifulSoup import BeautifulSoup
import sys

def echo(message):
    print message

def main():
	response = requests.get('http://en.wikipedia.org/wiki/Python')
	soup = BeautifulSoup(response.content)
	echo(soup.findAll('p')[0].getText(separator=u' '))
	
if __name__ == '__main__':
    main()