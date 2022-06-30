import add
import average
import divide
import multiply
import storage
import subtract



def updateInputNum():
    inputData = input("Enter number or operation here: ")

    inputDataFloat = str(inputData)

    if inputDataFloat.isalpha():
        if inputDataFloat == "avrg":
            average.averageOut()
        elif inputDataFloat == "add":
            add.add()
        elif inputDataFloat == "subtract":
            subtract.subtract()
        elif inputDataFloat == "multiply":
            multiply.multiply()
        elif inputDataFloat == "divide":
            divide.divide()
        else:
            print("Error: Input must be a Float or Decimal.")
    if inputDataFloat.isdecimal or inputDataFloat.contains(''):
        storage.numbStorage.append(inputData)
        numstr = str("num")
        inputnumlistnum = str(len(storage.numbStorage))
        inputNumStr = str(numstr) + str(inputnumlistnum)
        updateInputNum()
    if inputDataFloat.contains('!'):
        print("Unrecognized symbol.")
        quit()

updateInputNum()
#average.averageOut()


