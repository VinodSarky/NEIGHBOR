#!/usr/bin/env python
# coding: utf-8

# Copyright 2022 by Vinod Sarky, Indian Institute of Technology Madras.
# All rights reserved.

import math
import numpy as np
import pandas as pd

print("Hi!. This code had been generated to find out the neighbors of an atom in a binary supercell.")
print()

#1.0 Function Section:

#The function is defined where the sphere is created with respective given center and all the points are taken in the sphere which is below the cut-off radius.
def check(a, b, c, x, y, z):

    x1 = math.pow((x-a), 2)
    y1 = math.pow((y-b), 2)
    z1 = math.pow((z-c), 2)
    return (x1 + y1 + z1)



#2.0 Input Section:

#2.1 The elements and the cut-off radius had been introduced:

print("Please enter the Element name exactly as in your input file. Eg. (Cu, Nb, Ta, etc.)")
print("Atom A and Atom B are two elements in a binary supercell.")
print("Note: There might be an error, if the input element name differs from that of in the input excel file.")
print()
A = input("Please enter the element name of Atom A:" )

B = input("Please enter the element name of Atom B:" )


#Input the desired cut-off radius, in which you want your detected neighbors to be.
print()
r = eval(input("Enter the cut-off radius in angstorms with-in which you want the neighbors to be defined:" ))
print()


#2.2 The input filename and the sheetname had to be introduced:

print("Note: Be careful while entering the input filenames and sheetnames. Slight deviations can cause error.")
print("Note: Don't forget to mention the extension while entering filename. Eg. Input.xlsx")

print()
print("Please enter the excel filename containing coordinates of center atoms of Supercell. Eg. Input.xlsx.")

df=pd.read_excel(input(), sheet_name=input("Enter the sheetname in your input excel file. Eg. Sheet1:" ))
print()
print("Please enter the excel filename containing neighbouring atomic positions of Supercell. Eg. Input.xlsx.")

dg=pd.read_excel(input(), sheet_name=input("Enter the sheetname in your input excel file. Eg. Sheet2:" ))
print()


#3.0 Code Section:

np_list = df.to_numpy()
np_list = dg.to_numpy()

m=df.values
n=dg.values

print("Enter 1, if you need neighboring atoms count only, without coordinates as an output.")
print("Enter 2, if you need neighboring atoms count along with the respective coordinates as an output.")

what = eval(input("Enter 1 or 2:" ))
print()

#3.1 If only neighbor atoms count is only needed.

if what == 1:

    final=[]
    for center_atom in m:
        dist=[]
        out=[]
        for atoms in n:
            ans = check(center_atom[0], center_atom[1], center_atom[2], atoms[0], atoms[1], atoms[2])
            if ans<(r**2) or ans==(r**2):
                out.append(atoms[3])
                dist.append(math.sqrt(ans))
        AtomA = out.count(A)
        AtomB = out.count(B)
        final.append(list(center_atom))
        final.append(AtomA)
        final.append(AtomB)
        final.append(dist)
    
    
#Converting to excel

    do = pd.DataFrame()

    do['Centeres'] = final[0::4]
    do[A] = final[1::4]
    do[B] = final[2::4]
    do['Distance'] = final[3::4]

 
    final_output = input("Enter the name of the output file. Note: Don't forget to mention the extension. Eg. Output.xlsx:" )
    do.to_excel(final_output, index = False)
    print("Your {} file is successfully created".format(final_output))
    
    
#3.2 If neighbor atoms count along with coordinates are needed.
    
elif what == 2:
     
    final=[]
    for center_atom in m:
        dist=[]
        out=[]
        for atoms in n:
            ans = check(center_atom[0], center_atom[1], center_atom[2], atoms[0], atoms[1], atoms[2])
            if ans<(r**2) or ans==(r**2):
                out.append(list(atoms))
                dist.append(ans**0.5)
            AtomA = 0
            AtomB = 0
            for point in out:
                if point[3] == A:
                    AtomA = AtomA + 1
                elif point[3] == B:
                    AtomB = AtomB + 1
                    
        final.append(list(center_atom))
        final.append(AtomA)
        final.append(AtomB)
        final.append(out)
        final.append(dist)
    
#Converting to excel

    do = pd.DataFrame()

    do['Centeres'] = final[0::5]
    do[A] = final[1::5]
    do[B] = final[2::5]
    do['Coordinates'] = final[3::5]
    do['Distance'] = final[4::5]
    
    
    final_output = input("Enter the name of the output file. Note: Don't forget to mention the extension. Eg. Output.xlsx:" )
    do.to_excel(final_output, index = False)
    print("Your {} file is successfully created".format(final_output))
    
else:
    print("You have entered an output other then 1 or 2. Re-run the code with proper input being either 1 or 2 as per your requirement.")

    
#Code_End.

