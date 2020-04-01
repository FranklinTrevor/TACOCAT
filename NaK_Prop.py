# Lane Carasik and Tyler Hughes
# Last Modified: 11/17/2015
# Calculate fluid properties for NaK 
# Reference: Thermophysical Properties of Materials for Nuclear
# Note: 
# 1. In the reference the equations are mislisted as j/kg-k were they are
# actually kJ/kg-k
# Engineering: A Tutorial and Collection of Data
#function [rho,Cp,k,nu,Pr] = NaKProps(T) - does this need to be in code?

import numpy as np 
import matplotlib as mpl 


def rhoNa(T):
	rhoNa = (1/(10**-3))*(0.89660679 + 0.5161343*((T+273.15)*10**-3) - 1.8297218*((T+273.15)*10**-3)**2 + 2.2016247*((T+273.15)*10**-3)**3 - 1.3975634*((T+273.15)*10**-3)**4 + 0.4486694*((T+273.15)*10**-3)**5 - 0.057963628*(T*10**-3)**6) #kg/m^3
	return rhoNa

def rhoK(T):
	rhoK = (1/(10**-3))*(0.90281376 - 0.16990711*((T+273.15)*10**-3) - 0.26864769*((T+273.15)*10**-3)**2 - 0.50568188*((T+273.15)*10**-3)**3 + 0.46537912*((T+273.15)*10**-3)**4 + 0.20378107*((T+273.15)*10**-3)**5 - 0.034771308*((T+273.15)*10**-3)**6) #kg/m^3
	return rhoK

def CpNa(T):
	CpNa = (38.12 - (0.069*10**6)*((T+273.15)**-2) - (19.493*10**-3)*(T+273.15) + (10.24*10**-6)*(T+273.15)**2)/22.99 #kJ/kg-K
	return CpNa

def CpK(T):
	CpK = (39.288 - (0.086*10**6)*((T+273.15)**-2) - (24.334*10**-3)*(T+273.15) + (15.863*10**-6)*(T+273.15)**2)/39.098 #kJ/kg-K
	return CpK

def k(T):
	k = 15.0006 + (30.2877*10**-3)*(T+273.15) - (20.8095*10**-6)*(T+273.15)**2; #W/m-K
	return k

def nu(T):
	nu = (200.7657 - 0.734683*(T+273.15) + (1.12102*10**-3)*(T+273.15)**2 - (0.774427*10**-6)*(T+273.15)**3 + (0.200382*10**-9)*(T+273.15)**4)/10**8 #m^2/s
	return nu