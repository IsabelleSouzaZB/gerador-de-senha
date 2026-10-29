#criar interface

import tkinter as tk
from tkinter import messagebox
import secrets 
import string

## SENHAS ALEATORIAS


def gerar_senha():
    try:
        tamanho = int(campo_tamanho.get())

        if tamanho < 8 or tamanho > 64:
            messagebox.showwarning(
                "Aviso",
                "Escolha um tamanho entre 8 e 64."
            )
            return

        caracteres = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        senha = "".join(
            secrets.choice(caracteres)
            for _ in range(tamanho)
        )
        campo_senha.config(state="normal")
        campo_senha.delete(0, tk.END)
        campo_senha.insert(0, senha)
        campo_senha.config(state="readonly")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um tamanho válido."
        )

def copiar_senha():
    senha = campo_senha.get()
    
    if not senha:
        messagebox.showwarning("Aviso", "Não há senha para copiar.")
        return
    
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo(
    "Sucesso", 
    "Senha copiada para a área de transferência."
    )

# CONFIGURAÇÃO DA JANELA PRINCIPAL

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x300")
janela.resizable(False, False)
janela.configure(bg="#172554")

# TITULO 
titulo = tk.Label(
    janela,
    text="Gerador de Senhas",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#172554"
)

# TEXTO EXPLICATIVO

descricao = tk.Label(
    janela,
    text="Clique no botão para gerar uma senha aleatória e segura.",
    font=("Arial", 12),
    fg="#CBD5E1",
    bg="#172554"
)

descricao.pack(pady=5)

# CAMPO DE ESCOLHER O TAMANHO 

rotulo_tamanho = tk.Label(
    janela,
    text="Tamanho da senha (8 a 64):",
    bg="#172554",
    fg="white",
)

rotulo_tamanho.pack(pady=(15, 5 ))

campo_tamanho = tk.Spinbox(
    janela,
    from_=8,
    to=64,
    width=5,
    font=("Arial", 12),
    justify="center"
)

campo_tamanho.delete(0, tk.END)
campo_tamanho.insert(0, "16")  # Valor padrão
campo_tamanho.pack()

campo_senha = tk.Entry(
    janela,
    font=("Consolas", 12),
    state="readonly",
    readonlybackground="white",
    width=32,
    justify="center"
)

campo_senha.pack(pady=20)

botao_gerar = tk.Button(
    janela,
    text="Gerar Senha",
    command=gerar_senha,
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

botao_gerar.pack(fill="x", padx=45, pady=5, ipady=5)

botao_copiar = tk.Button(
    janela,
    text="Copiar Senha",
    command=copiar_senha,
    font=("Arial", 11),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

botao_copiar.pack(fill="x", padx=45, pady=5, ipady=5)



janela.mainloop()
