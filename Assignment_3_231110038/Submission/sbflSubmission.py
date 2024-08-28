#!/usr/bin/env python3

import argparse
from msilib.schema import Component
import sys
import numpy as np

sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv
from operator import itemgetter

def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite

    # ULYSIS IMPLEMENTATION FOR FITNESS SCORE
    wi = 0 
    for i in range(0,len(activity_mat[0])):

        # If the component is zero vector its wi is 1 
        zero=1
        for k in range(0,len(activity_mat)):
            if(activity_mat[k][i]!=0):
                zero=0
                break

        # Li counts the number of component set with same activity pattern
        Li=0
        for j in range(0,len(activity_mat[0])):
            flag=1
            for k in range(0,len(activity_mat)):
                if(i!=j and activity_mat[k][i]==activity_mat[k][j]):
                    continue
                else:
                    flag=0
                    break
            if(flag==1):
                Li+=1

        # Add 1 to wi if component is a zero vector
        if(zero==1):
            wi += 1
        # Otherwise wi = wi + Li / number_of_components-1
        else:
            wi += Li / (len(activity_mat[0])-1)
        
    W_ulysis = wi/len(activity_mat[0])
    # print(W_ulysis)

    # W_ulysis is the fitness score
    fitness_score = W_ulysis
    return fitness_score


# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """
        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        sus_score = 0
        # ToDo : implement the suspiciousness score function.
        
        #extract the column of component index mentioned from activity mmatrix
        component=[]
        for i in range (0,len(self.activity_mat)):
            component.append(self.activity_mat[i][comp_index])
        
        cf=0
        cp=0
        nf=0

        # Computing the values for cf, cp and nf
        for i in range (0, len(component)):
            if(component[i]==1 and self.errorVec[i]==1):
                cf+=1
            elif(component[i]==1 and self.errorVec[i]==0):
                cp+=1
            elif(component[i]==0 and self.errorVec[i]==1):
                nf+=1

        # using Ochiai metric to calculate suspiciouness score
        # sus_score = ochiai(comp_index) = cf / (((cf+nf)*(cf+cp))**(1/2)))

        temp = (cf+nf)*(cf+cp)
        if(cp!=0 and cf==0 and nf==0):
            sus_score=0
        if(temp!=0):
            sus_score = cf/(temp**(1/2))
       
        # print("SUSP:    =>",sus_score)
        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        """
        rankList = []
        # ToDo : implement rankList
        list_score=[]

        # calling funtion supiciousness(i) for each compnent index of activity matrix
        for i in range(0, len(self.activity_mat[0])):
            list_score.append(['c'+str(i+1),self.suspiciousness(i)])

        # Sort the list in descending order of suspiciousness 
        rankList = sorted(list_score, key=itemgetter(1), reverse=True)
        print("SUSPICIOUSNESS OF EACH COMPONENT:\n ",rankList)
        print("\n")

        # Assign the worst case rank to each component for being suspiciouss
        same_score=1
        k=0
        rank=0
        for i in range(0,len(rankList)):
            if(i!=len(rankList)-1 and rankList[i][1]==rankList[i+1][1]):
                same_score+=1
            else:
                for j in range(k,i+1):
                    rankList[j][1]=same_score+rank
                    k=i+1
                rank=same_score+rank
                same_score=1     
                  
        print("RANK OF COMPONENTS BEING SUSPICIOUS:\n",rankList)
        return rankList


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)
