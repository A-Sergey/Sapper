import random
size = 5                            #размер поля
counter = 0
nMine = 5 

def counterMine(x):
    n = 0
    for i in x:
        if pole[i] == 'M':
            n += 1
    return(n)

cells = [n for n in range(1,size**2+1)]    
pole = {a:0 for a in cells} 
random.shuffle(cells)                  
for cell in cells:
    counter+=1
    if counter <= nMine:                     #первые nMine случайных ячеек - мины
        pole[cell] = 'M'
    else:                                   #остальные ячейки заполняем количеством мин
        if cell == 1:
            pole[cell] = counterMine([cell+1,cell+size,cell+size+1])
        elif cell == size:
            pole[cell] = counterMine([cell-1,cell+size,cell+size-1])
        elif cell == size*(size-1)+1:
            pole[cell] = counterMine([cell-size,cell-size+1,cell+1])
        elif cell == size**2:
            pole[cell] = counterMine([cell-size,cell-size-1,cell-1])

        elif cell%5 == 1:
            pole[cell] = counterMine([cell-size,cell-size+1,cell+1,cell+size,cell+size+1])
        elif cell < size:
            pole[cell] = counterMine([cell-1,cell+1,cell+size-1,cell+size,cell+size+1])
        elif cell%5 == 0:
            pole[cell] = counterMine([cell-size-1,cell-size,cell-1,cell+size-1,cell+size])
        elif cell > size*(size-1):
            pole[cell] = counterMine([cell-1,cell-size-1,cell-size,cell-size+1,cell+1])
        else:
            pole[cell] = counterMine([cell-size-1,cell-1,cell+size-1,cell+size,cell+size+1,cell+1,cell-size+1,cell-size])