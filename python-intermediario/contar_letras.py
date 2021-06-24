#!/bin/env python3

def contar_letras(palavra):
    split_text = tuple(palavra)
    letter_count_dict = {}
    #your code goes here
    
    for letter in split_text:
        if (not letter in letter_count_dict):
            letter_count_dict[letter] = 1
        else:
            letter_count_dict[letter] += 1
    
    return letter_count_dict

