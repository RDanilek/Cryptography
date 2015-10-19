"""
cryptography.py
Author: Roger Danilek
Credit: Nils

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
la = 1000*associations
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
        esum = [x + y for x, y in combined_list]
        for x in esum:
            print(la[x], end='')
        print("")

    elif a=="d":
        decrypting = input("What do you want to decrypt? ")
        jumbler = input("What should the key be? ")
        d_list = []
        j_list= []
        for x in decrypting:
            d_list.append(associations.find(x))
        for x in jumbler:
            j_list.append(associations.find(x))
        if len(d_list) > len(j_list):
            combined_list = list(zip(d_list, cycle(j_list)))
        else:
            combined_list = list(zip(cycle(d_list), j_list))
        dsum = [x - y for x, y in combined_list]
        for x in dsum:
            print(la[x], end='')
        print("")
    elif a =="q":
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")

#associations.find(char)
#associations[index]