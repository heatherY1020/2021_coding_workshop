#problem1
'2020'
'Check the data again.'
'193'
'2019'
#problem2
def palindrome(t):
    k = []
    for x in range(len(t)):
        k.append(t[x])
    if k[0] == k[len(t)-1]:
        return True
a = int(input())
b = str(a)
for x in range(a+1):
    if palindrome(str(x)) == True:
        print(x)
#problem3
{
    ‘1864939’: {
        ‘SUB’: {
            ‘image’ : ‘../data/dicoms/1864939/1-1864939/SUB/10007 (2601171)-(2601161).nrrd’,
        ‘mask’ : ‘../data/dicoms/1864939/1-1864939/SUB/Segmentation.seg.nrrd’
        }
    },
    ‘7098873’: {
        ‘SUB’: {
            ‘image’ : ‘../data/dicoms/7098873/18-7098873/SUB/10007 (2388471)-(2388461).nrrd’,
        ‘mask’ : ‘../data/dicoms/7098873/18-7098873/SUB/Segmentation.seg.nrrd’
        }
    }
    ‘7128189’: {
        ‘SUB’: {
            ‘image’ : ‘../data/dicoms/7128189/20-7128189/SUB/10007 (3004471)-(3004461).nrrd’,
        ‘mask’ : ‘../data/dicoms/7128189/20-7128189/SUB/Segmentation.seg.nrrd’
        }
    },
    ‘7158991’: {
        ‘SUB’: {
            ‘image’ : ‘../data/dicoms/7158991/24-7158991/SUB/10007 (3737971)-(3737961).nrrd’,
        ‘mask’ : ‘../data/dicoms/7158991/24-7158991/SUB/Segmentation.seg.nrrd’
    	}
    }
    ‘7162170’: {
        ‘SUB’: {
            ‘image’ : ‘../data/dicoms/7162170/25-7162170/SUB/10007 (3835571)-(3835561).nrrd’,
        ‘mask’ : ‘../data/dicoms/7162170/25-7162170/SUB/Segmentation.seg.nrrd’
    	}
    }

}
#problem4

#problem5
sereja = 0
dima = 0
a = int(input())
b = input()
c = b.split(' ')
d = []
for x in range(len(c)):
    d.append(int(c[x]))
def big_number(d):
    if d[0] > d[len(d)-1]:
        return 0
    else:
        return len(d)-1
if a%2 == 1:
    while a != 1:
        sereja = sereja + d[big_number(d)]
        d.pop(big_number(d))
        dima = dima + d[big_number(d)]
        d.pop(big_number(d))
        a = a-2
    sereja = sereja + d[big_number(d)]
else:
    while a != 0:
        sereja = sereja + d[big_number(d)]
        d.pop(big_number(d))
        dima = dima + d[big_number(d)]
        d.pop(big_number(d))
        a = a-2        
print(sereja,dima)

#problem6
t = input()
a = input()
b = input()
sum = 0
n,m,x,y = t.split(' ')
A_a = a.split(' ')
B_b = b.split(' ')
A = []
B = []
C = []
D = []
for k in range(len(A_a)):
    A.append(int(A_a[k]))
for k in range(len(B_b)):
    B.append(int(B_b[k]))
n = int(n)
m = int(m)
x = int(x)
y = int(y)
def t(n,m,x,y):
    if A[n]-x <= B[m] and B[m] <= A[n]+y:
        return True
    else:
        return False
for j in range(len(A)):
    for k in range(len(B)):
        if t(j,k,x,y) == True:
            C.append(j+1)
            D.append(k+1+sum)
            sum = sum + 1
            B.pop(k)
            break
print(sum)
for k in range(len(C)):
    print(C[k], D[k])
