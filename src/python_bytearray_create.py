#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

In Python, How to create a bytearray object?

En Python, ¿Cómo crear un objeto bytearray?
'''

#create a bytearray from a bytes object
ba = bytearray(b'hello world')
print(ba)

#create a bytearray from a string defining the standard of coding
ba = bytearray('Python is easy', 'utf8')
print(ba)

#create a bytearray from a list of integers in the range 0 through 255
ba = bytearray([104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100])
print(ba)
