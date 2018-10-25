import numpy as np
from numpy.linalg import norm
from numpy import dot,sign
from random import uniform
from time import sleep

'''
Notas:
        Realizar Mediciones
        Intentar animar
        Mejorar Rendimiento
        Insertar variacion de Volumen
'''



class particula(object):
    '''Defino mi particula'''
    def __init__(self,r,v):
        self.radius=1
        self.mass=1
        self.pos=np.array(r)
        self.vel=np.array(v)
    def __str__(self):
        r = 'r = ('  + str(self.pos[0]) + ', ' + str(self.pos[1]) + ') \nv = ('  + str(self.vel[0]) + ', ' + str(self.vel[1]) + ')'
        return r
    def get_r(self):
        return self.pos
    def get_v(self):
        return self.vel

def collide():
    for part in part_list:
        if part.pos[0]>=dimA or part.pos[0]<=-dimA:
            part.vel[0]=-part.vel[0]
            part.pos[0]=dimA*sign(part.pos[0])
        elif part.pos[1]>=dimB or part.pos[1]<=-dimB:
            part.vel[1]=-part.vel[1]
            part.pos[1]=dimB*sign(part.pos[1])
        part.pos=part.pos+part.vel*step
    for i in range(len(part_list)):
        for j in range(i+1,len(part_list)):
            if norm(part_list[i].pos-part_list[j].pos)<=2:
                r=part_list[i].pos-part_list[j].pos
                r=r/norm(r)
                vi=dot(part_list[i].vel,r)
                vj=dot(part_list[j].vel,r)
                change=vi-vj
                part_list[i].vel=part_list[i].vel-change*r
                part_list[j].vel=part_list[j].vel+change*r
                print('Colision')
            else:
                pass

no_part=100
dimA=200
dimB=100
step=0.1
part_list=[]
for i in range(no_part):
    part=particula([uniform(-dimA,dimA),uniform(-dimB,dimB)],
                        [uniform(-1,1),uniform(-1,1)])
    part_list.append(part)
T=[]
for i in range(15):
    collide()
