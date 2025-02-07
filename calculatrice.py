import tkinter as tk

# Permet d'ajouter un chiffre au nombreCourantUser via parametre ou champ
def addchiffre(chiffre):
    pass
    global numberUserCurrent
    numberUserCurrent = unChamp.get()+str(chiffre)
    unChamp.delete(0, tk.END)
    unChamp.insert(0,numberUserCurrent)


# Permet de reset la calculatrice 
def reset():
    pass
    global resultCurrentUserStock
    global numberUserCurrent
    global expressionTotal

    numberUserCurrent = ""
    resultCurrentUserStock = ""
    expressionTotal = ""
    unChamp.delete(0,tk.END)
    labelexpressionTotal.config(text="")

# Permet de choisir un operateur et également de remplir expression totale avec le str complet saisie par l'user
def choiceoperator(operator):
    global numberUserCurrent
    global expressionTotal
    global operatorUserCurrent

    numberUserCurrent = unChamp.get()

    # Permet d'afficher et de stocker l'expression Totale saisie par l'user
    expressionTotal += unChamp.get()+operator
    labelexpressionTotal.config(text=expressionTotal)
    labelexpressionTotal.grid()



    # Vide le champ pour permettre a l'user d'ecrire a nouveau dessus 
    unChamp.delete(0,tk.END)
    # Vide la variable numberUserCurrent
    numberUserCurrent=""

def calculer():
    try:
        global expressionTotal
        global resultUserStock

        expressionTotal += unChamp.get()
        resultUserStock = eval(expressionTotal)
        expressionTotal += unChamp.get()
        
        expressionTotal = ""

        # Supprime le champ et le rerempli avec le resultat calculé plus haut
        unChamp.delete(0,tk.END)
        unChamp.insert(0,str(resultUserStock))

        # Affiche le resultat dans le label 
        labelexpressionTotal.config(text=resultUserStock)
    
    except Exception as e:
        labelexpressionTotal.config(text="Erreur : Vérifiez votre expression"+e)

 
numberUserCurrent = ""
resultUserStock =""
expressionTotal =""

uneCalculatrice = tk.Tk()
uneCalculatrice.resizable(None,None)

labelexpressionTotal = tk.Label()
labelexpressionTotal.grid(row=0,column=0,columnspan=4)

unChamp= tk.Entry(width=30,textvariable=numberUserCurrent)
unChamp.grid(row=1,column=0,columnspan=4)

button9 = tk.Button(text="9", width=5, command=lambda:addchiffre(9))
button8 = tk.Button(text="8", width=5, command=lambda:addchiffre(8))
button7 = tk.Button(text="7", width=5, command=lambda:addchiffre(7))
button3 = tk.Button(text="3" , width=5, command=lambda:addchiffre(3))
button2 = tk.Button(text="2" , width=5, command=lambda:addchiffre(2))
button1 = tk.Button(text="1" , width=5, command=lambda:addchiffre(1))
button6 = tk.Button(text="6" , width=5, command=lambda:addchiffre(6))
button5 = tk.Button(text="5" , width=5, command=lambda:addchiffre(5))
button4 = tk.Button(text="4" , width=5, command=lambda:addchiffre(4))

buttonDivision = tk.Button(text="/", width=5, command=lambda: choiceoperator("/"))
button9.grid(row=2,column=0)
button8.grid(row=2,column=1)
button7.grid(row=2,column=2)
buttonDivision.grid(row=2,column=3)
buttonMultiply = tk.Button(text="x" , width=5, command=lambda: choiceoperator("*"))
button6.grid(row=3,column=0)
button5.grid(row=3,column=1)
button4.grid(row=3,column=2)
buttonMultiply.grid(row=3,column=3)
buttonSoustraction = tk.Button(text="-" , width=5, command=lambda:choiceoperator("-"))
button3.grid(row=4,column=0)
button2.grid(row=4,column=1)
button1.grid(row=4,column=2)
buttonSoustraction.grid(row=4,column=3)
buttonreset = tk.Button(text="C", width=5, command=reset)
button0 = tk.Button(text="0", width=5, command=lambda:addchiffre(0))
buttonegal = tk.Button(text="=", width=5, command= calculer) 
buttonAddition = tk.Button(text="+", width=5, command=lambda:choiceoperator("+"))

buttonreset.grid(row=5,column=0)
button0.grid(row=5,column=1)
buttonegal.grid(row=5,column=2)
buttonAddition.grid(row=5,column=3)

uneCalculatrice.mainloop()