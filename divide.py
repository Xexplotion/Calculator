
def divide():
    num1 = float(input("Enter Number Here: "))
    num2 = float(input("Enter Number Here: "))

    quotient = float(num1) / float(num2)

    if str(quotient).endswith('.0'):
        quotientstr = str(quotient)
        quotientRemovingDotZero = quotientstr.replace('.0', '')
        print(quotientRemovingDotZero)
    else:
        print(quotient)
