import tkinter as tk

def espace(nombredeligne):

    for _ in range(nombredeligne):
        print("")

# Permet d'ajouter un chiffre au nombreCourantUser via parametre ou champ
def addchiffre(chiffre):
    global numberUserCurrent
    unChamp.delete(0, tk.END)
    numberUserCurrent += unChamp.get()+str(chiffre)
    unChamp.insert(0,numberUserCurrent)
    
# Permet de choisir un operateur et également de remplir expression totale avec numberUserCurrent et operator
def choiceoperator(operator):
    global numberUserCurrent
    global numberUserStock

    global operatorUserCurrent
    global operatorUserStock

    global expression

    espace(2)
    print("Fonction Choice Operator")
    espace(1)
    print(f"Operateur en mémoire : {operatorUserCurrent}")

    operatorUserCurrent=operator

    if numberUserCurrent != "":

        if numberUserStock =="":
            print("If numberUserStock est vide = True")
            numberUserStock = numberUserCurrent
            operatorUserStock=operatorUserCurrent
            expression = f"{numberUserStock} {operatorUserStock}"
            labelexpressionTotal.config(text=expression)
            print(f"operatorUserStock = {operatorUserStock}")
            print(f"operatorUserCurrent = {operatorUserCurrent}")
            print(f"numberUserStock = {numberUserStock}")
            print(f"numberUserCurrent = {numberUserCurrent}")
        else:
            # Faire le calcul entre numberusercurrent et numberuserstock
            # via une fonction calculer
            print("If numberUserStock est vide = False")
            print(f"numberUserStock = {numberUserStock}")
            print(f"numberUserCurrent = {numberUserCurrent}")
            calculer() 

    elif numberUserCurrent == "" and numberUserStock != "":
        print("NumberUSerCurrent est vide")
        numberUserCurrent=numberUserStock
        operatorUserStock=operatorUserCurrent

    else: 
        print("Merci de choisir une valeur a numberUserCurrent avant d'appuyer sur un opérateur !")

    unChamp.delete(0,tk.END)
    unChamp.insert(0,"")
    numberUserCurrent=""


def calculer():
    global numberUserCurrent
    global numberUserStock
    
    global operatorUserCurrent
    global operatorUserStock

    global resultUserStock
    global expression

    espace(2)
    print(f"Fonction Calculer : ")
    espace(1)
    print(f"numberUserStock = {numberUserStock}")
    print(f"numberUserCurrent = {numberUserCurrent}")    
    print(f"Operateur en mémoire : {operatorUserStock}")
    print(f"Opératuer Courant : {operatorUserCurrent}")

    expression = f"({numberUserStock} {operatorUserStock} {numberUserCurrent}){operatorUserCurrent}"
    print(f"expression est égal à : {expression}")
    labelexpressionTotal.config(text=expression)

    espace(1)
    match operatorUserStock:
        case "+":
            resultUserStock = int(numberUserCurrent)+int(numberUserStock)
            print(f"Cas + : {numberUserCurrent} + {numberUserStock} = {resultUserStock}")
        case "-":
            resultUserStock = int(numberUserStock)-int(numberUserCurrent)
            print(f"Cas - : {numberUserCurrent} - {numberUserStock} = {resultUserStock}")
        case "*":
            resultUserStock = int(numberUserStock)*int(numberUserCurrent)
            print(f"Cas * : {numberUserCurrent} * {numberUserStock} = {resultUserStock}")
        case "/":
            resultUserStock = int(numberUserStock)/int(numberUserCurrent)
            print(f"Cas / : {numberUserCurrent} / {numberUserStock} = {resultUserStock}")
        case _:
            print("Choix Invalide !")
    espace(1)

    print("Fin du Calcul : ")
    numberUserCurrent=resultUserStock
    numberUserStock=numberUserCurrent
    numberUserCurrent=""
    operatorUserStock = operatorUserCurrent
    operatorUserCurrent = ""        
    print(f"numberUserStock = {numberUserStock}")
    print(f"numberUserCurrent = {numberUserCurrent}")
    print(f"operateur courant : {operatorUserCurrent}")

    unChamp.delete(0, tk.END)
    unChamp.insert(0,resultUserStock)

# Permet de reset la calculatrice 
def reset():
    global numberUserCurrent
    global numberUserStock
    global operatorUserCurrent 
    global operatorUserStock
    global resultUserStock
    global expression

    espace(2)
    print("Fonction RESET : ")
    espace(1)

    numberUserCurrent = ""
    numberUserStock = ""
    operatorUserCurrent = ""
    operatorUserStock = ""
    resultUserStock = ""
    expression = ""

    print(f"numberUserCurrent = {numberUserCurrent}")
    print(f"numberUserStock = {numberUserStock}")
    print(f"operatorUserCurrent = {operatorUserCurrent}")
    print(f"operatorUserStock = {operatorUserStock}")
    print(f"resultUserStock = {numberUserCurrent}")

    unChamp.delete(0,tk.END)
    
    labelexpressionTotal.config(text="")
 

numberUserCurrent = ""
numberUserStock = ""

operatorUserCurrent = ""
operatorUserStock = ""

resultUserStock =""

expression =""

uneCalculatrice = tk.Tk()
uneCalculatrice.resizable(None,None)

labelexpressionTotal = tk.Label()
labelexpressionTotal.grid(row=0,column=0,columnspan=4)

unChamp= tk.Entry(width=30,textvariable=numberUserCurrent)
unChamp.grid(row=1,column=0,columnspan=4)

for i in range(9):

    button = tk.Button(text=str(i+1), width=5, command=lambda x=i: addchiffre(x+1))
    button.grid(row=(i//3)+2,column=i%3)


buttonreset = tk.Button(text="C", width=5, command=reset)
buttonreset.grid(row=5,column=0)
buttonZero = tk.Button(text="0" , width=5, command=lambda:addchiffre(0))
buttonZero.grid(row=5,column=1)
buttonEgal = tk.Button(text="=", width=5, command= calculer) 
buttonEgal.grid(row=5,column=2)

buttonDivision = tk.Button(text="/", width=5, command=lambda: choiceoperator("/"))
buttonDivision.grid(row=2,column=3)
buttonMultiply = tk.Button(text="x" , width=5, command=lambda: choiceoperator("*"))
buttonMultiply.grid(row=3,column=3)
buttonSoustraction = tk.Button(text="-" , width=5, command=lambda:choiceoperator("-"))
buttonSoustraction.grid(row=4,column=3)
buttonAddition = tk.Button(text="+", width=5, command=lambda:choiceoperator("+"))
buttonAddition.grid(row=5,column=3)

uneCalculatrice.mainloop()