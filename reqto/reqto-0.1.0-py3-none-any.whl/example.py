# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 02:43:08 2022

@author: EUROCOM
"""
import reqto
import math

package="docrawl"
  
#reqto=Reqto() 


#response=reqto.get(url+"/api/v1/nodes")

def function1(par1,kw="test"):
    print(par1,kw)
    


response = reqto.get(f'https://pypi.org/pypi/{package}/json',timeout=5,timeout_function=function1,timeout_args=10)
#response = requests.get('https://pypi.org/pypi/doclick/json')

print(response)
#print(response.content)
#print(response.ok)



#response = reqto.get("https://pypi.org/pypi/doclick/json",timeout=5)
#response = reqto(requests.get(f'https://pypi.org/pypi/{package}/json'),5)

    
