from random import choice
# This code I made gave me the idea for the challenge here:
# https://www.sololearn.com/Discuss/1026806/challenge-random-visual-pattern-generator
# It's quite a messy code, I would be happy to learn a way to get the sameresult in a more elegant way.
# I suggest you to try UTF-8 on a computer, it gives nicer results with rounded shapes :)

# ---Choose the size and character set here
width = 25
height = 17
AorU = 'A'# choose between ASCII ('A') or UTF-8 here (UTF-8 won't work on CodePlayground)
# Next lines represent different character sets, unfortunately you can use only the 128 ascii one here, if you want to try the other ones, copy them into your favorite IDE.

set = choice([1,2,3,4])
if AorU == 'U':
        # -----UTF-8 tables (random choice)
    if set==1 or 4:
        charnums = (9473, 9475, 9487, 9491, 9495, 9499, 9507, 9515, 9523, 9531, 9547, 9581, 9582, 9583, 9584)
        ends = ('lr', 'ud', 'rd', 'ld', 'ur', 'lu', 'urd', 'lud', 'lrd', 'lur', 'lurd', 'rd', 'ld', 'lu', 'ur')
    if set==2:
        charnums = (9552, 9553, 9556, 9559, 9562, 9565, 9568, 9571, 9574, 9577, 9580)
        ends = ('lr', 'ud', 'rd', 'ld', 'ur', 'lu', 'urd', 'lud', 'lrd', 'lur', 'lurd')
    if set==3:
        charnums = (9473, 9475, 9487, 9491, 9495, 9499, 9507, 9515, 9523, 9531, 9547)
        ends = ('lr', 'ud', 'rd', 'ld', 'ur', 'lu', 'urd', 'lud', 'lrd', 'lur', 'lurd')


else:
    # -----ASCII tables (random choice)
    if set==1:
        charnums = (201,187, 200, 188, 186, 205, 206, 202, 203, 185, 204)
    if set==2:
        charnums = (213, 184, 212, 190, 179, 205, 216, 207, 209, 181, 198)
    if set==3:
        charnums = (218, 191, 192, 217, 179, 196, 197, 193, 194, 180, 195)
    ends = ('rd','ld','ur','lu','ud','lr','lurd','lur','lrd','lud','urd')
    if set==4:
        charnums = (179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218)
        ends = ('ud', 'lud', 'lud', 'lud','ld','ld','lud','ud','ld','lu','lu','lu','ld','ur','lur','lrd','urd','lr','lurd','urd','urd','ur','rd','lur','lrd','urd','lr','lurd','lur','lur','lrd','lrd','ur','ur','rd','rd','lurd','lurd','lu','rd')

# Producing the dictionary I'll work with
chars = [chr(i) for i in charnums]
dic = {}
for i in range(len(chars)):
    dic[chars[i]] = ends[i]
dic[' '] = ''

# The cc function is giving a random character, respecting some condition about the connections : 'a' gives the instructions about what connections the character must have, 'b' gives the instructions about which connnections the character must not have.
# Example : if a = 'l' and b = 'd', the char will have to connnect left, but not down. This lets '┛', '━', '┻'as possible characters and thus the cc() function will randomly return one of these.
def cc(a,b):
    try:
        c = choice([i for i in dic if all(j in dic[i] for j in a) and all(k not in dic[i] for k in b) and i != ' '])
    except:
        c = 'not'
    return c

# The pattern function will use the cc function to progressively produce the pattern.
# It produces it progressively, starting with edges, and then filling it in, because of the difficulty to get all the lines connected, without having to make a symmetrical pattern or to close it with some after-correction.
def pattern(n, m = 0):
    if m == 0: m = n
    pat = [[' ']*m] +[[' ', ' '] for i in range(n)]+ [[' ']*m]
    
    # corners
    pat[1].insert(1, cc('', 'lu'))
    pat[1].insert(-1, cc('', 'ur'))
    pat[-1 - 1].insert(1, cc('', 'ld'))
    pat[-1 - 1].insert(-1, cc('', 'dr'))
    
    # first and last columns
    for i in range(1, -2, -2):
        for j in range(n - 2):
            a = ''
            b = 'l' if i == 1 else 'r'
            if 'd' in dic[pat[j + 1][int((3 * i - i ** 2) / 2)]]:
                a += 'u'
            else:
                b += 'u'
            if 'u' in dic[pat[j + 3][int((3 * i ** 2 - i) / 2)]]:
                a += 'd'
            pat[j + 2].insert(i, cc(a, b))
            
    # first and last lines
    for i in range(1, -3, -3):
        for j in range(m - 2):
            a = ''
            b = 'u' if i == 1 else 'd'
            if 'r' in dic[pat[i][j + 1]]:
                a += 'l'
            else:
                b += 'l'
            if j == m - 3:
                a += 'r'
            pat[i].insert(j + 2, cc(a, b))
            
    # filling columns from left to right
    for i in range(n - 2):
        for j in range(m - 2):
            a = ''; b = ''
            if 'd' in dic[pat[i + 1][j + 2]]:
                a += 'u'
            else:
                b += 'u'
            if 'r' in dic[pat[i + 2][j + 1]]:
                a += 'l'
            else:
                b += 'l'
            if i == n - 3:
                if 'u' in dic[pat[-2][j + 2]]:
                    a += 'd'
                else:
                    b += 'd'
            if j == m - 3:
                if 'l' in dic[pat[i + 2][-2]]:
                    a += 'r'
                else:
                    b += 'r'
            ch = cc(a, b)
            
            # Final touch : solving the situations when no solution is available
            # Here I modify randomly the previous upper or left char if there are not enough possibilities to connect the new character to produce.
            while ch=='not':
                u, v, w, y = choice([(1, 2, 'd', 'u'), (2, 1, 'r', 'l')])
                a_ = dic[pat[i + u][j + v]] + w
                b_ = ''.join([e for e in 'lurd' if e not in a_])
                pat[i + u][j + v] = cc(a_, b_)
                a += y
                b = b.replace(y,'')
                ch = cc(a, b)
            pat[i + 2].insert(j + 2, ch)

    print('\n'.join([''.join(r) for r in pat]))

pattern(height,width)

