from random import choice

# These are chars from the 128 ascii chars usable with python in CodePlayground :
# It may not display well on some devices.
charnums = (1,2,3,4,5,6,16,21,22,23,25)
ends = ('rd','ld','ur','lu','ud','lr','lurd','lur','lrd','lud','urd')

# If you copy this code to your IDE, you can use the two following lines instead of the previous ones, they give a much nicer result with rounded shapes :
#charnums = (9473, 9475, 9487, 9491, 9495, 9499, 9507, 9515, 9523, 9531, 9547, 9581, 9582, 9583, 9584)
#ends = ('lr', 'ud', 'rd', 'ld', 'ur', 'lu', 'urd', 'lud', 'lrd', 'lur', 'lurd', 'rd', 'ld', 'lu', 'ur')

chars = [chr(i) for i in charnums]
dic = {}
for i in range(len(chars)):
    dic[chars[i]] = ends[i]
dic[' '] = ''

# Function cc randomly chooses the next character in the line according to the rules defined in line and stored in a and b
def cc(a,b):
    try:
        c = choice([i for i in dic if all(j in dic[i] for j in a) and all(k not in dic[i] for k in b) and i != ' '])
    except:
        c = ' '
    return c

# Function line creates the next line for the grid, creating conditions for the whole line, stored in aa and bb and then calling the function cc(a, b) to create each character. It has special conditions for the last raw and the two last lines, to avoid having unfinished lines in the pattern.
def line(grid,last=0):
    line = ' '
    aa = []
    bb = []
    l = len(grid[-1])
    for i in range(l - 1):
        aa.append([])
        bb.append([])
        if 'd' in dic[grid[-1][i+1]]:
            aa[i].append('u')
        else:
            bb[i].append('u')
        if 'r' in dic[line[-1]]:
            aa[i].append('l')
        else:
            bb[i].append('l')
        if i == l-3:
            aa[i].append('r')
        if i == l-2:
            bb[-1].append('r')
        if last==2:
            aa[0].append('d')
            aa[-1].append('d')
        if last==1:
            if i < l-2:
                if 'd' not in dic[grid[-1][i+2]]:
                    aa[i].append('r')
            bb[i].append('d')
        line += cc(aa[i],bb[i])
    return line

# Function pat finally gather the lines together, with special 2 last lines, and returns the grid as a string
def pat(n, m = 0):
    grid = []
    if m == 0: m = n
    grid.append(' '*(m+1))
    for i in range(n-2):
        grid.append(line(grid))
    grid.append(line(grid,2))
    grid.append(line(grid,1))
    return '\n'.join(grid)

print(pat(40,30))
