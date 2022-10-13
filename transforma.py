import tkinter as tk
import pyperclip

frame = tk.Tk()
frame.title("Transforme seu texto errado")
frame.geometry('700x300')

def captalizar():
    inp = inputtxt.get(1.0, "end-1c") 
    
    varTXT = inp.capitalize();
    pyperclip.copy(varTXT)
    lbl.config(text = "Seu texto: " + varTXT)

def upperCase():
    inp = inputtxt.get(1.0, "end-1c") 
    
    varTXT = inp.upper();

    pyperclip.copy(varTXT)

    lbl.config(text = "Seu texto: " + varTXT)

def lowerCase():
    inp = inputtxt.get(1.0, "end-1c") 
    
    varTXT = inp.lower();
    pyperclip.copy(varTXT)
    lbl.config(text = "Seu texto: " + varTXT)



inputtxt = tk.Text(frame,
				height = 5,
				width = 80)

inputtxt.pack()


printButton = tk.Button(frame,
						text = "Transformar primeira letra maiuscula",
						command = captalizar
                        )
printButton2 = tk.Button(frame,
						text = "Transformar todas letras maiusculas",
						command = upperCase)

printButton3 = tk.Button(frame,
						text = "Transformar todas letra minusculas",
						command = lowerCase)


printButton.pack()
printButton2.pack()
printButton3.pack()


lbl = tk.Label(frame, text = "")
lbl.pack()



frame.mainloop()
