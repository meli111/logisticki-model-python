#!/usr/bin/env python3
import matplotlib.pyplot as pl
from logisticki import logisticki
vr=[1,2,3,4,5,6,7,8,9,10]
K=19
a=0.5
Vo=2
rez=logisticki(K,a,Vo,vr)
pl.plot(vr, rez, marker='.')
pl.xlabel('vreme')
pl.ylabel('zapremina')
pl.title('Logisticki model')
pl.show()
