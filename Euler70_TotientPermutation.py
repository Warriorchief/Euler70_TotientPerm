#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:12:22 2017
@author: christophergreen

Totient permutation
Problem 70
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine
the number of positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n)
produces a minimum.
"""

import math

def is_prime(x):
    if x<1:
        return False;
    for i in range(2,math.ceil(math.sqrt(x))):
        if x%i==0:
            return False
    return True

def get_prime_factorization(x):
    pass
    
def assemble_primes(highest):
    primes=[]; 
    j=2
    while j<=highest:
        if is_prime(j):
            primes.append(j)
        j+=1
    return primes;

def get_factors_effic(x):
    primes=assemble_primes(x);
    facts=[];
    for i in range (2,math.ceil(math.sqrt(x))):
        if x%i==0:
            facts.append(i);
            facts.append(int(x/i));
    facts.sort()
    print("the factors of",x,"are:",facts);
    primefacts=[];
    for j in facts:
        if j in primes:
            primefacts.append(j);
    print (x,"has the prime factors:",primefacts);
    return;   
    

    
    
    
def is_rel_prime(x,y):
    for i in range (2,x+1):
        if x%i==0:
            if y%i==0:
                #print("the prime",i,"goes into both",x,"and",y,"so",x,"is not rel prime to",y);
                return False;
    return True;
    
def count_rel_primes(y):
    count=1; #to account for 1 itself
    for i in range(2,y):
        if is_rel_prime(i,y):
            count+=1;
    return count;
#count_rel_primes(87109) #--> 79180
 
def is_permutation(x,y):
    if len(str(x))!=len(str(y)):
        return False
    chars=[];
    i=0;
    while i<len(str(x)):
        chars.append(str(x)[i]);
        i+=1;
    #print("from",x,"we have made the chars",chars);
    j=0;
    while j<len(str(y)):
        if str(y)[j] in chars:
            del chars[chars.index(str(y)[j])];  #find the first instance of the char in str(x) and deletes it
        else:
            return False;
        j+=1;
    #print("having removed matches one at a time, x still has the chars:",chars);
    if len(chars)==0:
        return True;
    else:
        return False;
          
def find_perm_with_min_phi(start,stop):
    i=start;
    minholder=2
    while i<stop:
        if i%50==0:
            print("passing through i being",i);
        c=count_rel_primes(i);
        if is_permutation(i,c):
            if i/c < minholder:
                print(i,"has",c,"rel primes, making the phi ratio:",i/c,"our new min");
                minholder=i/c;
            else:
                print(i,"had",c,"rel primes","but didn't make a new min phi-value");
        i+=1;
    print("done");
    return;

#find_perm_with_min_phi(10,6000);
#--> 21 has 12 rel primes, making the phi ratio: 1.75 our new min
#--> 291 has 192 rel primes, making the phi ratio: 1.515625 our new min
#--> 4435 has 3544 rel primes, making the phi ratio: 1.2514108352144468 our new min
#--> 5229 had 2952 rel primes but didn't make a new min phi-value
#--> 5367 had 3576 rel primes, but didn't make a new min phi-value
#--> 5637 has 3756 rel primes, but didn't make a new min phi-value

























      
""" THE FUNCTIONS AND DATA BELOW END UP NOT BEING NEEDED  

def assemble_primes(start,stop):
    primes=[];
    i=stop;
    while i>=start:
        if is_prime(i):
            primes.append(i);
        i-=1;
    #print(list(primes));
    #print("above is the",len(primes),"primes from",stop,"down through",start);
    return primes;        
    
def find_min_phi_ratio(primeslist):    
    minholder=5;
    i=100;
    while i<107:
        c=count_rel_primes(primeslist[i]);
        if primeslist[i]/c < minholder: #and is_permutation(i,c):
            print(primeslist[i],"has",c,"relative primes,making the phi ratio:",primeslist[i]/c);
            minholder=primeslist[i]/c;
        i+=1;
    print("done,that was the lowest phi ratio");
    return;
#testlist=assemble_primes(15000,16000);
#find_min_phi_ratio(testlist);
#15913 has 15912 relative primes,making the phi ratio: 1.000062845651081
#15919 has 15918 relative primes,making the phi ratio: 1.000062821962558
#15923 has 15922 relative primes,making the phi ratio: 1.0000628061801282
#15937 has 15936 relative primes,making the phi ratio: 1.000062751004016
#15959 has 15958 relative primes,making the phi ratio: 1.0000626644942976
#15971 has 15970 relative primes,making the phi ratio: 1.0000626174076392
#15973 has 15972 relative primes,making the phi ratio: 1.0000626095667418
#done,that was the lowest phi ratio

def main(stop):
    i=5000000;
    counter=0;
    while i>=stop:
        if is_prime(i):
            if is_permutation(i,i-1):
                print("found it! the prime",i,"and one less than it",i-1,"are permutations!");
                return i;
            else:
                counter+=1;
        if i%100000==0:
            print("passing down through",i,"so another hund thous tried and",counter,"failed");
            counter=0;
        i-=1;
    print("not found");
    return  
#main(1000000); #--> not found

#**********************************************
#IMPORTANT REALIZATION: THE NUMBERS WITH THE LOWEST PHI RATIO ARE THE PRIMES THEMSELVES!
#FOR EXAMPLE, 15973 HAS 15972 RELATIVE PRIMES.
#THIS MEANS WE CAN JUST START WITH THE LARGEST PRIME IN THE RANGE OF THE QUESTION AND WORK 
#DOWNWARDS UNTIL ONE OF THEM HAS A NUMBER OF PRIMES THAT IS A PERMUTATION OF ITSELF.
#SINCE THE NUMBER OF RELATIVE PRIMES OF A PRIME IS ALWAYS JUST 1 LESS THAN THE PRIME ITSELF,
#WE CAN WALK DOWNWARDS FROM THE LARGEST PRIME UNTIL ITSELF AND ONE LESS THAN IT ARE 
PERMUTATIONS!  ...OKAY TRIED THIS AND DIDN't FIND ANY...FAIL
#**********************************************
"""
