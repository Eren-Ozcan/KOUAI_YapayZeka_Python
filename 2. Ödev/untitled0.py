# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:54:27 2021

@author: ereno
"""

def myFunction(liste,sentence):
    controls=liste
    sentence=sentence
    newSentence=""
    for i in range(len(controls)):
        ayrac=controls[i]
        newSentence=""
        tempSentence=sentence.split(ayrac) 
        for j in range(len(tempSentence)):
            newSentence+=tempSentence[j]
        sentence=newSentence
    with open('output.txt', 'a') as f1:
        f1.write(sentence)
    return sentence

file1 = open('odev.txt', 'r')
Lines = file1.readlines()
liste=["+",".",",","-","_","?","=","(",")","{","}","[","]","/","&","%","#","!","<",">","|","*",":",";","0","1","2","3","4","5","6","7","8","9",]
for i in range(len(Lines)):
    print(myFunction(liste,Lines[i]))