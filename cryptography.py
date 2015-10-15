"""
cryptography.py
Author: Roger Danilek
Credit: Nils

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
from itertools import cycle 
a = ""
while a != "q":
    a = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if a=="e":
        encrypting = input("What do you want to encrypt? ")
        jumbler = input("What should the key be? ")
        e_list = []
        j_list= []
        for x in encrypting:
            e_list.append(associations.find(x))
        for x in jumbler:
            j_list.append(associations.find(x))
        if len(e_list) > len(j_list):
            combined_list = list(zip(e_list, cycle(j_list)))
        else:
            combined_list = list(zip(cycle(e_list), j_list))
        list1, list2 = zip(*combined_list)
        wot = [list1, list2]
        [(sum a for a in (*wot))] 
        
    elif a=="d":
        print("d")
    elif a =="q":
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")

#associations.find(char)
#associations[index]