# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:35:03 2020

@author: Chyt
"""
filename = "C:\\Users\Chyt\Desktop\Python Projects\passwords.txt"

def part_1(data):
    
    answer = 0
    
    with open(data) as f:
        for line in f:
            (pw, string) = line.strip().split(': ')
            nums, substring = pw.split()
            lst_int = [int(x) for x in nums.split("-")]
            count = string.count(substring)
            bottom = lst_int[0]
            top = lst_int[1]
            
            if bottom <= count <= top:
                answer = answer + 1
            
    print(answer)
    
def part_2(data):
    
    answer = 0
    
    with open(data) as f:
        for line in f:
            (pw, string) = line.strip().split(': ')
            nums, substring = pw.split()
            lst_int = [int(x) for x in nums.split("-")]
            bottom = lst_int[0] - 1
            top = lst_int[1] - 1
            if string[bottom] == substring and not string[top] == substring or string[top] == substring and not string[bottom] == substring:
                answer = answer + 1
            
    print(answer)

part_1(filename)
part_2(filename)



 

