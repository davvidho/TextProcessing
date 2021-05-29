# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:37:38 2021

@author: dh361
"""
import numpy as np
import os

directory = 'C:/Users/dh361/Desktop/optreports'
files_list=[]
for file in os.listdir(directory):
    files_list.append(file)

params_list =[]
for k in enumerate(files_list):
    text = open(directory +'/'+ files_list[k[0]])
    for lines in text:
        if lines.startswith('PARAMETERS'):
            words = lines.split()
    params_list.append(words)

new_params_list = []
for m in enumerate(params_list):
    new_params_list.append(params_list[m[0]][2:len(params_list[m[0]])])       
    
for a in range(len(new_params_list)):
    for b in range(len(new_params_list[a])):
        new_params_list[a][b] = new_params_list[a][b].replace('[', '')
        new_params_list[a][b] = new_params_list[a][b].replace(']', '')
        new_params_list[a][b] = new_params_list[a][b].replace(',', '')
        new_params_list[a][b]=float(new_params_list[a][b])
    new_params_list[a] = np.asarray(new_params_list[a])        

random_changes = []
for i in range(len(new_params_list)):
    arr = np.copy(new_params_list[i])
    for j in range(int(len(new_params_list[0])/2)):
        arr[2*j]=arr[2*j]+3e-7
        arr[2*j+1]=arr[2*j+1]+3e-7
        random_changes.append(arr)
        print(arr)
        arr = np.copy(new_params_list[i])
                
matrix_random_changes = np.zeros((len(random_changes),10))
for j in range(len(random_changes)):
    matrix_random_changes[j] = random_changes[j]
        
    
        
        
# params = np.array([2.55548549e-07, 2.47268575e-07, 4.93578500e-07, 4.88792798e-07, 6.96553250e-07, 8.00000000e-07, 7.27019713e-07, 7.37678512e-07, 7.08860421e-07, 5.91896566e-07])
# list2= []

# for j in range(int(len(params)/2)):
#     list2.append(np.zeros(len(params)))

# for i, arr in enumerate(list2):
#     arr = np.copy(params)
#     arr[2*i]=arr[2*i]+3e-7
#     arr[2*i+1]=arr[2*i+1]+3e-7
#     list[i]=arr
#     arr=np.copy(params)
#     print(list[i])
    
    
    