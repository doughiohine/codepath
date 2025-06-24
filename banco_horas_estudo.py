import tkinter as tk
from datetime import datetime

def salvar_registro():
    materia = entrada_materia.get()
    horas = entrada_horas.get()

    if materia and horas:
        with open("registro_estudos_semestre2.txt", "a") as arquivo:
            arquivo.write(f"{datetime.now()} - {materia} - {horas}h\n")
        status_label.config(text="Registro salvo com sucesso!")
        entrada_materia.delete(0, tk.END)
        entrada_horas.delete(0, tk.END)
    else:
        status_label.config(text="Preencha todos os campos!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Registro de Estudos")
janela.geometry("300x200")

# Campo para a matéria

tk.Label(janela, text="Matéria:").pack()
entrada_materia = tk.Entry(janela)
entrada_materia.pack()

# Campo para as horas estudadas
tk.Label(janela, text="Horas estudadas:").pack()
entrada_horas = tk.Entry(janela)
entrada_horas.pack()

# Botão para salvar
btn_salvar = tk.Button(janela, text="Salvar Registro", command=salvar_registro)
btn_salvar.pack(pady=10)

# Label para status
status_label = tk.Label(janela, text="")
status_label.pack() 

# Iniciar o loop da interface gráfica
janela.mainloop()   

