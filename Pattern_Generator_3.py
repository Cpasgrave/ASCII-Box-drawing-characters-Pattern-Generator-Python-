from random import  choice as choose
from numpy.random import choice

H = 10 # Height
W = 10# Width

grid = [[[None,None,None,None] for i in range(W)] for j in range(H)]
dic = {'0011':chr(201),'1001':chr(187),'0110':chr(200),'1100':chr(188),'0101':chr(186),'1010':chr(205),'1111':chr(206),'1110':chr(202),'1011':chr(203),'1101':chr(185),'0111':chr(204)}

for i in range(H):
    grid[i][0][0]=0
    grid[i][-1][2]=0
for j in range(W):
    grid[0][j][1]=0
    grid[-1][j][3]=0

def connect(grid):
    for i in range(H):
     for j in range(W):
      if grid[i][j].count(0)==2: grid[i][j]=[x if x==0 else 1 for x in grid[i][j]]
      for k in range(4):
        if grid[i][j][k]==1:
         grid[i+int(((-1)**k-1)*(2-k)/2)][j+int(((-1)**k+1)*(k-1)/2)][(k+2)%4]=1

def fill(grid):
    for i in range(H):
        for j in range(W):
            if grid[i][j].count(None)==1:
                grid[i][j] = [x if x != None else choice([0,1],p=[0.9,0.1]) for x in grid[i][j]]
            connect(grid)
            if grid[i][j].count(None)==2:
                grid[i][j][choose([x for x in range(4) if grid[i][j][x]==None])] = choice([0,1],p=[0.9,0.1])
            connect(grid)
            if grid[i][j].count(None)>=3:
                grid[i][j][choose([x for x in range(4) if grid[i][j][x]==None])] = choice([0,1],p=[0.9,0.1])

while True:
    connect(grid)
    fill(grid)
    if 'None' not in str(grid):
        break

pattern = '\n'.join([''.join([dic[''.join([str(d)for d in c])] for c in r]) for r in grid])
print(pattern)
