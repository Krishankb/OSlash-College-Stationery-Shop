from sys import argv

#price list
priceList = {"TSHIRT" : (1000,0.10),"JACKET" : (2000,0.05),"CAP" : (500,0.20),
            "NOTEBOOK" : (200,0.20),"PENS" : (300,0.10),"MARKERS" : (500,0.05)}

purchase = {}



def taxBill(amount):
    amountFinal = amount * 0.10
    amountTotal = amount + amountFinal
    return amountTotal

def outPrint():
    totalValue = 0
    discountTotal = 0
    if purchase["TotalPrice"] <=999:
        print("TOTAL_DISCOUNT {:0.2f}".format(0))
        am = taxBill(purchase["TotalPrice"])
        print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(am))

    elif purchase["TotalPrice"] >= 1000 and purchase["TotalPrice"] <=2999:
        for keys in purchase:
            if keys != "TotalPrice":
                cValue = purchase[keys] * priceList[keys][0]
                discount = cValue * priceList[keys][1]
                totalValue += cValue
                discountTotal += discount 
        for keys in purchase:
            if keys == "TotalPrice":
                tfvalue = totalValue - discountTotal
                print("TOTAL_DISCOUNT {:0.2f}".format(discountTotal))
                am = taxBill(tfvalue)
                print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(am))

               
    elif  purchase["TotalPrice"] >=3000:
        for keys in purchase:
            if keys != "TotalPrice":
                cValue = purchase[keys] * priceList[keys][0]
                discount = cValue * priceList[keys][1]
                totalValue += cValue
                discountTotal += discount 
        for keys in purchase:
            if keys == "TotalPrice":
                tfvalue = totalValue - discountTotal
                discountValue = tfvalue * 0.05
                disTotal = discountTotal + discountValue
                finaleValue = tfvalue - discountValue

                print("TOTAL_DISCOUNT {:0.2f}".format(disTotal))
                am = taxBill(finaleValue)
                print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(am))

def main():
    # Sample code to read inputs from the file
    cartValue = 0
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        data = line.split()
        if data[0] == "ADD_ITEM":
            if data[1] == "TSHIRT" or data[1] == "JACKET" or data[1] == "CAP":
                if int(data[2]) <= 2:
                    purchase[data[1]] = int(data[2])
                    abc = int(data[2]) * priceList[data[1]][0]
                    cartValue += abc
                    print("ITEM_ADDED")
                else:
                    print("ERROR_QUANTITY_EXCEEDED")
            elif data[1] == "NOTEBOOK" or data[1] == "PENS" or data[1] == "MARKERS" :
                if int(data[2]) <=3:
                    purchase[data[1]] = int(data[2])
                    abc = int(data[2]) * priceList[data[1]][0]
                    cartValue += abc
                    print("ITEM_ADDED")
                else:
                    print("ERROR_QUANTITY_EXCEEDED")
            purchase["TotalPrice"] = cartValue
            
        elif data[0] == "PRINT_BILL":
            outPrint()
    
if __name__ == "__main__":
    main()
