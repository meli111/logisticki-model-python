#!/usr/bin/env python3
import math
import numpy
def logisticki(K,a,Vo,t):
	d=len(t)
	l=numpy.zeros(d)
	for i in range(0,d):
		l[i]=Vo*K/(Vo+(K-Vo)*math.exp(-a*t[i]))
	
	return l

