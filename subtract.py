import storage

def subtract():
    numStorageNumsStr = ' '.join(storage.numbStorage)

    numStorageNumsStrRemovingOpenBracket = numStorageNumsStr.replace('[', '')
    numStorageNumsStrRemovingCloseBracket = numStorageNumsStrRemovingOpenBracket.replace(']', '')
    numStorageNumsStrRemovingComma = numStorageNumsStrRemovingCloseBracket.replace(',', '')
    numStorageNumsStrFinal = numStorageNumsStrRemovingComma

    why = numStorageNumsStrFinal.split()

    #1 + 5 = 4
    #5 - 1 = 4


    for entry in why:
        entry.




    if str(returnnum).endswith('.0'):
        differencestr = str(returnnum)
        differenceRemoveDotZero = differencestr.replace('.0', '')
        print(differenceRemoveDotZero)
    else:
        print(returnnum)



