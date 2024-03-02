from tkinter import *
import math

def operatcii(operation, formula, entry_field):
    if operation == "C":
        formula = ""
    elif operation == "DEL":
        formula = formula[:-1]
    elif operation == "X^2":
        if formula.isdigit():
            formula = str(int(formula) ** 2)
        else:
            formula = "Error"
    elif operation in ["sin", "cos", "tan"]:
        try:
            formula = str(eval(f"math.{operation}({formula})"))
        except Exception:
            formula = "Error"
    elif operation == "=":
        if vurazu(formula):
            formula = str(eval(formula))
        else:
            formula = "Error"
    elif operation == "Вихід":
        root.quit()
    else:
        if formula == "0" or formula == "Error":
            formula = ""
        formula += operation
    pola_dla_vedenna(formula, entry_field)

def vurazu(expr):
    valid_chars = set('1234567890+-*/(). ')
    for char in expr:
        if char not in valid_chars:
            return False
    return True

def pola_dla_vedenna(formula, entry_field):
    if formula == "":
        formula = "0"
    entry_field.delete(0, END)
    entry_field.insert(0, formula)

def check_input(event):
    if event.char.isdigit() or event.char in "+-*/().":
        return True
    else:
        return False

def knopku(btn, entry_field):
    current_formula = entry_field.get()
    operatcii(btn, current_formula, entry_field)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "black"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    rjadok(root)
    root.mainloop()