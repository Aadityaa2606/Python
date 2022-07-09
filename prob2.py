N = int(input(''))
grps = [int(input('')) for i in range(N)]
cabs = []
z = False
for grp in grps:
    for cab in cabs:
        if sum(cab)+grp <= 4:
            cabs[0].append(grp)
            z=True
        else:
            z=False
    if not z:
        cabs.append([grp])
print(len(cabs))
