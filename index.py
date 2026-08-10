import customtkinter as ctk


def button_callback():
    print("button clicked")

    print(nome)


app = ctk.CTk()
ctk.set_appearance_mode("system")
app.geometry("800x600")



InputFornecedor = ctk.CTkEntry(app,placeholder_text="Digite o fornecedor")
InputNF = ctk.CTkEntry(app,placeholder_text="Digite o número da NF")
InputValor = ctk.CTkEntry(app,placeholder_text="Digite o valor")
InputFornecedor.pack()
InputNF.pack()
InputValor.pack()

button = ctk.CTkButton(app, text="Enviar", fg_color="red", text_color='green', command=button_callback)
button.pack()

app.mainloop()