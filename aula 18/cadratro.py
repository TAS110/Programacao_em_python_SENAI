import tkinter as tk
from tkinter import messagebox

def enviar_dados():

    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()
    cep = entry_cep.get()
    cidade = entry_cidade.get()
    cursos = entry_cursos.get()

 
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular: {celular}")
    print(f"Cep: {cep}")
    print(f"Cidade: {cidade}")
    print(f"Cursos: {cursos}")


    messagebox.showinfo("Cadastro", "Cadastro enviado com sucesso!")

janela = tk.Tk()
janela.geometry("1700x750")  
janela.config(bg="#F5F5F5") 

titulo = tk.Label(janela, text="Cadastro de Clientes", font=("Helvetica", 24, "bold"), bg="#4CAF50", fg="white")
titulo.pack(fill="x", pady=20)

frame_form = tk.LabelFrame(janela, font=("Helvetica", 16, "bold"), padx=20, pady=20, bg="#F5F5F5", bd=0, relief="flat")
frame_form.pack(padx=20, pady=10, fill="both", expand=True)

label_nome = tk.Label(frame_form, text="Nome:", font=("Helvetica", 12), bg="#F5F5F5")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(frame_form, text="Idade:", font=("Helvetica", 12), bg="#F5F5F5")
label_idade.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_idade = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(frame_form, text="E-mail:", font=("Helvetica", 12), bg="#F5F5F5")
label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_endereco = tk.Label(frame_form, text="Endereço:", font=("Helvetica", 12), bg="#F5F5F5")
label_endereco.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_endereco = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_endereco.grid(row=3, column=1, padx=10, pady=10)

label_celular = tk.Label(frame_form, text="Celular:", font=("Helvetica", 12), bg="#F5F5F5")
label_celular.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_celular = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_celular.grid(row=4, column=1, padx=10, pady=10)

label_cep = tk.Label(frame_form, text="CEP:", font=("Helvetica", 12), bg="#F5F5F5")
label_cep.grid(row=5, column=0, padx=10, pady=10, sticky="w")
entry_cep = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_cep.grid(row=5, column=1, padx=10, pady=10)

label_cidade = tk.Label(frame_form, text="Cidade:", font=("Helvetica", 12), bg="#F5F5F5")
label_cidade.grid(row=6, column=0, padx=10, pady=10, sticky="w")
entry_cidade = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_cidade.grid(row=6, column=1, padx=10, pady=10)

label_cursos = tk.Label(frame_form, text="Cursos:", font=("Helvetica", 12), bg="#F5F5F5")
label_cursos.grid(row=7, column=0, padx=10, pady=10, sticky="w")
entry_cursos = tk.Entry(frame_form, width=40, font=("Helvetica", 12), bd=0, relief="flat")
entry_cursos.grid(row=7, column=1, padx=10, pady=10)


btn_enviar = tk.Button(janela, text="Enviar", command=enviar_dados, width=20, height=2, bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"))
btn_enviar.pack(pady=20)


janela.mainloop()
