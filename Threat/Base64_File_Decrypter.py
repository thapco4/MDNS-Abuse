# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:54:08 2024

@author: tommy
"""

import re
import base64

#file_in=input("Please enter the complete filepath for the file to be encoded (include double backslashes if running Windows): ")
#file_out=input("Please enter the complete filepath where you wish to save the decoded file including the filename  (include double backslashes if running Windows): ")
file_in="exfiltrated.txt"
file_out="decoded.txt"

#opens file exfiltrated.txt file, that has been cleaned and converted, and
#   joins individual lines to one long single line
with open(file_in,"r") as input_file:
    pkt=input_file.read()
    needed_data=re.findall(r"A abc.(.*?).local",pkt)
#    print(needed_data)
    joined_data="".join(needed_data)
#    print(joined_data)

#writes the joined_data to temp_received_file.txt
with open("temp_received_file.txt","w") as received_data:
    received_data.write(joined_data)

#decrypts data from temp_received_file to decrypted_file
with open("temp_received_file.txt","r") as final_file:
    data_in=final_file.read()
    decrypted_file=base64.b64decode(data_in)
    
    with open(file_out,"wb") as decoded_file:
        decoded_file.write(decrypted_file)
        

    
