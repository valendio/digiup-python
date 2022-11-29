# len()
nama = 'Oryza Valendio'
print("Panjang string",len(nama))
#filter
umur = [5, 12, 17, 18, 24, 32]
def myFunc(x):
    if x < 18:
        return False
    else:
        return True
dewasa = filter(myFunc, umur)
print("kategori dewasa : ")
for x in dewasa:
    print(x)