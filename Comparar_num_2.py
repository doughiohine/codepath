import tkinter as tk
from tkinter import messagebox

def comparar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())

        if num1 > num2:
            resultado = "O primeiro número é maior que o segundo."
        elif num1 < num2:
            resultado = "O primeiro número é menor que o segundo."
        else:
            resultado = "Os dois números são iguais!"

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor insira apenas números válidos!")

janela = tk.Tk()
janela.title("Comparar Números")

# Layout
tk.Label(janela,text="Digite o primeiro número:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Digite o segundo número:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="Comparar", command=comparar).pack(pady=10)

janela.mainloop()