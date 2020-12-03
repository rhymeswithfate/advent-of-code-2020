# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:45:38 2020

@author: Chyt
"""
import numpy as np

data = np.genfromtxt("C:\\Users\Chyt\Desktop\Python Projects\input.txt",
                     dtype=int,
                     delimiter="\n")


def part_1(expense_report):
    
    for test_A in expense_report:
        for test_B in expense_report:
            sum_of_expenses = test_A + test_B
            if sum_of_expenses == 2020:
                print(test_A)
                print(test_B)
                quotient = test_A * test_B
                print(quotient)
                return
                

def part_2(expense_report):
    
     for test_A in expense_report:
        for test_B in expense_report:
            sum_of_expenses = test_A + test_B
            if sum_of_expenses < 2020:
                for test_C in expense_report:
                    sum_of_expenses = test_A + test_B + test_C
                    if sum_of_expenses == 2020:
                        print(test_A)
                        print(test_B)
                        print(test_C)
                        quotient = test_A * test_B * test_C
                        print(quotient)
                        return

part_1(data)
part_2(data)