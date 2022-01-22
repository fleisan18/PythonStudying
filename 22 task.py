#22. Найти расстояние между точками в пространстве 2D/3D
import random

x1 = random.randint(-10,10)
x2 = random.randint(-10,10)
y1 = random.randint(-10,10)
y2 = random.randint(-10,10)
z1 = random.randint(-10,10)
z2 = random.randint(-10,10)

def Distance2D (x1, x2, y1, y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

print(f'Расстояние между {x1,y1} и {x2,y2} = {Distance2D(x1,x2,y1,y2)}')

def Distance3D (x1, x2, y1, y2,z1,z2):
    return ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(1/2)

print(f'Расстояние между {x1,y1,z1} и {x2,y2,z2} = {Distance3D(x1,x2,y1,y2,z1,z2)}')
