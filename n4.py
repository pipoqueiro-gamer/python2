
par = [0] * 8 
cont_par = 0
n: int = [3, 8, 15, 22, 27, 34, 41, 50]

for i in range(0, 8):
    if n[i] % 2 == 0:
        par[cont_par] = n[i]  
        cont_par += 1


par = par[:cont_par] 

print(par)


