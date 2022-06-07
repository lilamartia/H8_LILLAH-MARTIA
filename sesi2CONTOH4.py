# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:48:05 2022

@author: Lenovo
"""

buku = 2000
jumlahbeli = 3
totalbelanja = 6000
uang = 10000

if uang > totalbelanja:
    print("mangkuk")
elif uang < totalbelanja:
    print("tidak beli buku")
else:
    print("tidak jadi beli buku")
    
    if uang > totalbelanja:
        print("beli buku dapat mangkuk")
    elif uang < totalbelanja:
        print("tidak beli buku")
    else:
        print("tidak jadi beli buku")
        
        buku = 2000
        jumlahbeli = 3
        totalbelanja = 6000
        uang = 10000

        if uang > totalbelanja:
            print("beli buku dapat mangkuk")
        elif uang < totalbelanja:
            print("tidak beli buku")
        else:
            print("tidak jadi beli buku")