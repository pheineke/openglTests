vertices = [
    (0,0,0)
]

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
n = 0
r = 1

def Morpher():
    global a,b,c,d,e,f,n,r
    x, y, z = vertices[len(vertices)-1]

    if f == 0:
        if n == 0:
            x += r
            n = 1

            v0 = x, y, 0
            vertices.append(v0)
        else:
            y += r
            n = 0
            f = 1
            r += 1

            v0 = x, y, 0
            vertices.append(v0)

    else:
        if n == 1:
            y -= r
            n = 0
            f = 0
            r += 1

            v0 = x, y, 0
            vertices.append(v0)
        else:
            x -= r
            n = 1

            v0 = x, y, 0
            vertices.append(v0)
            

    
    print(v0, f, n)


print(vertices[0], f, n)
for i in range(10):
    Morpher()