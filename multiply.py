
def multiply():
    num1 = float(input("Enter Number Here: "))
    num2 = float(input("Enter Number Here: "))

    product = float(num1) * float(num2)

    if str(product).endswith('.0'):
        productstr = str(product)
        productRemovingDotZero = productstr.replace('.0', '')
        print(productRemovingDotZero)
    else:
        print(product)



