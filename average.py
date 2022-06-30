import storage

if __name__ == '__main__':
    quit()
else:
    def averageOut():



        amountofnums = len(storage.numbStorage)

        numStorageNumsStr = ' '.join(storage.numbStorage)

        numStorageNumsStrRemovingOpenBracket = numStorageNumsStr.replace('[', '')
        numStorageNumsStrRemovingCloseBracket = numStorageNumsStrRemovingOpenBracket.replace(']', '')
        numStorageNumsStrRemovingComma = numStorageNumsStrRemovingCloseBracket.replace(',', '')
        numStorageNumsStrFinal = numStorageNumsStrRemovingComma

        why = numStorageNumsStrFinal.split()

        sumofit = 0

        for entry in why:
            sumofit += float(entry)

        average = float(sumofit) / int(amountofnums)

        if str(average).endswith('.0'):
            averagestr = str(average)
            averageRemovingDotZero = averagestr.replace(".0", '')
            print(averageRemovingDotZero)
            outputNumber = float(averageRemovingDotZero)
            quit()

        else:
            print(average)
            outputNumber = float(average)
            quit()