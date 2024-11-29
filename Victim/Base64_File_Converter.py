# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:38:40 2024

@author: tanderson
"""

import base64

#file_in=input("Please enter the complete filepath for the file to be encoded (include double backslashes if running Windows): ")
#file_out=input("Please enter the complete filepath where you wish to save the encoded file including the filename  (include double backslashes if running Windows): ")
file_in="c:\\temp\\sherlockholmes.txt"
file_out="c:\\temp\\sampleb64.txt"

with open(file_in,'rb') as inputfile:
    data_in=inputfile.read()
    encodedfile=base64.b64encode(data_in)
    print(encodedfile.decode('utf-8'))
    
    with open(file_out,'wb') as outfile:
        outfile.write(encodedfile)