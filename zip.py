#https://stackoverflow.com/questions/12040989/printing-all-the-values-from-multiple-lists-at-the-same-time
l1,l2,l3 = [1,2,3],[4,5,6],[7,8,9]

for l in (l1,l2,l3):
    print(l)

print("*"*80)

for l in (l1+l2+l3):
    print(l, end=" ")
print("\n")
print('*'*80)
for l in zip(l1,l2,l3):
    print(l)