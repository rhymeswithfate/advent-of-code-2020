# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:39:45 2020

@author: Chyt
"""
filename = r"C:\\Users\Chyt\Desktop\Python Projects\tree.txt"

def part_1(data):

    answer = 0
    count = 0

    with open(filename) as f:
        for line in f:
            stripped = line.strip()
            length = len(stripped)
            if line[count % length] == '#':
                answer = answer + 1
            count = count + 3
                    
    print(answer)
    
def part_2(data):

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    with open(filename) as f:
        count = 0
        for line in f:
            stripped = line.strip()
            length = len(stripped)
            if line[count % length] == '#':
                one = one + 1
            count = count + 3

        print(one)
       
    with open(filename) as f:
        count = 0
        for line in f:
            stripped = line.strip()
            length = len(stripped)
            if line[count % length] == '#':
                two = two + 1
            count = count + 1
        print(two)
        
        
    with open(filename) as f:
        count = 0
        for line in f:
            stripped = line.strip()
            length = len(stripped)
            if line[count % length] == '#':
                three = three + 1
            count = count + 5
        print(three)
        
        
    with open(filename) as f:
        count = 0
        for line in f:
            stripped = line.strip()
            length = len(stripped)
            if line[count % length] == '#':
                four = four + 1
            count = count + 7
        print(four)
    
    
    with open(filename) as f:
        count = 0
        second_line = 0
        for line in f:
            stripped = line.strip()
            length = len(stripped)
            if second_line > 0:
                second_line = 0
            else:
                if line[count % length] == '#':
                    five = five + 1
                count = count + 1
                second_line = 1
                
        print(five)
                        
    print(one*two*three*four*five)

part_1(filename)
print("\n")
part_2(filename)