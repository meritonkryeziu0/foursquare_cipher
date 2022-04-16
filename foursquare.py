#!/usr/bin/env python3
import re

table = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 
def generate_table(key = ''):	
    # Algoritmi punon sipas nje matrice 5x5 (= 25 elemente), alfabeti i gjuhes angleze ka gjithsej 26 shkronja,	
    # karakteri i cili perdoret me se paku eshte 'Q' prandaj e heqim nga alfabeti	
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'	
    table = [[0] * 5 for row in range(5)] # krijo nje tabele 5x5 me elementet fillestare 0	
    	
    # Largon te gjitha karakteret jasht rangut {a-z, A-Z, 0-9} dhe kthen qelsin ne uppercase

def mangle(topRight, bottomLeft, digraphs):

    a = position(table, digraphs[0])        #kthen poziten e karakterit te pare te digrafit bazuar ne tabelen e alfabetit
    b = position(table, digraphs[1])
    return topRight[a[0]][b[1]] + bottomLeft[b[0]][a[1]]    #kthen karakteret ne baze te renditjes se matricave
  '''	
                topRight	
     table         	
    a b c d e   S I G U R	
    f g h i j   A B C D E	
    k l m n o   F H J K L	
    p r s t u   M N O P T	
    v w x y z   V W X Y Z	
    	
    P Y T H O   a b c d e	
    N A B C D   f g h i j	
    E F G I J   k l m n o	
    K L M R S   p r s t u	
    U V W X Z   v w x y z
    	
    bottomLeft	
    '''
         		
def decrypt(keys, plaintext):	
    ciphertext = ''	
    plaintext = re.sub(r'[\W]', '', plaintext).upper().replace('Q', '')	
    topRight, bottomLeft = generate_table(key[0]), generate_table(key[1])
         # todo	
def position(table, ch):	
    for row in range(5):	
        for col in range(5):	
            if table[row][col] == ch:	
                return (row, col)       #kthen poziten e karakterit ne tabel	
    return (None, None)


if __name__ == '__main__':
    plaintext = 'Dite e mire'
    key = ['siguri', 'python']

    ciphertext = encrypt(key, plaintext)
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Plain teksti: {0}        len: {1}\n".format(plaintext,len(plaintext)))
    print("Cipher teksti: {0}         len: {1}".format(ciphertext, len(ciphertext)))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++\n")
