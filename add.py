import storage

def add():
    numStorageNumsStr = ' '.join(storage.numbStorage)

    numStorageNumsStrRemovingOpenBracket = numStorageNumsStr.replace('[', '')
    numStorageNumsStrRemovingCloseBracket = numStorageNumsStrRemovingOpenBracket.replace(']', '')
    numStorageNumsStrRemovingComma = numStorageNumsStrRemovingCloseBracket.replace(',', '')
    numStorageNumsStrFinal = numStorageNumsStrRemovingComma

    why = numStorageNumsStrFinal.split()

    sumofit = 0

    for entry in why:
        sumofit += float(entry)

    if str(sumofit).endswith('.0'):
        sumstr = str(sumofit)
        sumRemovingDotZero = sumstr.replace('.0', '')
        print(sumRemovingDotZero)
    else:
        print(sumofit)



