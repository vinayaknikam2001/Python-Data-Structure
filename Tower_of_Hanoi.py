def TOH(discs,start,mid,last):
    if(discs >= 1):
        TOH(discs-1,start,last,mid)
        move_disc(discs,start,last)
        TOH(discs-1,mid,start,last)

def move_disc(no,st,la):
    print(f'\n\nMove disc:{no} from {st} to {la}')

A = 'A'
B = 'B'
C = 'C'

n = int(input('\nEnter no. of discs. '))
TOH(n,A,B,C)
