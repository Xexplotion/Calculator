import storage

storage.numbStorage.append(1)
storage.numbStorage.append(3)
storage.numbStorage.append(5)
storage.numbStorage.append(9)
storage.numbStorage.append(2)


amountofnums = len(storage.numbStorage)

numStorageNumsStr = ''.join(str(storage.numbStorage))

numStorageNumsStrRemovingOpenBracket = numStorageNumsStr.replace('[', '')
numStorageNumsStrRemovingCloseBracket = numStorageNumsStrRemovingOpenBracket.replace(']', '')
numStorageNumsStrRemovingComma = numStorageNumsStrRemovingCloseBracket.replace(',', '')
numStorageNumsStrFinal = numStorageNumsStrRemovingComma

why = numStorageNumsStrFinal.split()

sumofit = 0

for float in why:
    sumofit += int(float)

print(sumofit)
