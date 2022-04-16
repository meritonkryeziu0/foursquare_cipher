#!/usr/bin/env python3
import re

table = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 

def mangle(topRight, bottomLeft, digraphs):

    a = position(table, digraphs[0])        #kthen poziten e karakterit te pare te digrafit bazuar ne tabelen e alfabetit
    b = position(table, digraphs[1])
    return topRight[a[0]][b[1]] + bottomLeft[b[0]][a[1]]    #kthen karakteret ne baze te renditjes se matricave


if __name__ == '__main__':
    plaintext = 'Dite e mire'
    key = ['siguri', 'python']

    ciphertext = encrypt(key, plaintext)
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Plain teksti: {0}        len: {1}\n".format(plaintext,len(plaintext)))
    print("Cipher teksti: {0}         len: {1}".format(ciphertext, len(ciphertext)))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++\n")