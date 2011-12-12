import cell_mdl
import multiprocessing as mp
import numpy as np
import shmarray as sa
reload(cell_mdl)
import cProfile
Nx,Ny,Nz = 50,50,0

print "creation du modele"
model = cell_mdl.Red3(Nx,Ny,Nz, cylindrical=True)

print "modele temporelle"
tmdl = cell_mdl.IntParaMP(model)

print 'calcul'
tmdl.compute(500,[2,10,2,10])

tmdl.save('testlog')

#def truc(n,V):
#    V[n,2] = n


#Vm = sa.ones((5,5))
##tmp = np.empty((5,5,2))
##Vm.value = tmp

#for n in range(4): 
#    print n
#    mp.Process(target=truc, args = (n,Vm)).start()
