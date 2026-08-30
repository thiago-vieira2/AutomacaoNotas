
import customtkinter as ctk
import Excel


def apenas_texto(valor):
    if valor == "":
        return True

    return valor.replace(" ", "").isalpha()


def apenas_numero(valor):
    if valor == "":
        return True

    return valor.isdigit()


def validar_valor(valor):
    if valor == "":
        return True

    valor = valor.replace(",", ".")

    try:
        float(valor)
        return True
    except ValueError:
        return False


def Button():
    fornecedor = InputFornecedor.get().upper()
    nf = InputNF.get()
    valor = InputValor.get()
    pedido = InputPedido.get()

    print("Fornecedor:", fornecedor)
    print("NF:", nf)
    print("Valor:", valor)

    Excel.AdicionarValores(nf, pedido, fornecedor, valor)


# =========================
# CONFIGURAÇÃO
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x650")
app.title("Controle de Notas Fiscais")
app.resizable(False, False)


# =========================
# CONTAINER PRINCIPAL
# =========================

main = ctk.CTkFrame(
    app,
    corner_radius=20
)

main.pack(
    padx=40,
    pady=40,
    fill="both",
    expand=True
)


# =========================
# CABEÇALHO
# =========================

titulo = ctk.CTkLabel(
    main,
    text="Lançamento de Nota Fiscal",
    font=ctk.CTkFont(
        size=28,
        weight="bold"
    )
)

titulo.pack(
    padx=40,
    pady=(35, 5),
    anchor="w"
)


subtitulo = ctk.CTkLabel(
    main,
    text="Preencha os dados da nota fiscal abaixo",
    font=ctk.CTkFont(size=14),
    text_color="gray"
)

subtitulo.pack(
    padx=40,
    pady=(0, 30),
    anchor="w"
)


# =========================
# ÁREA DOS CAMPOS
# =========================

form = ctk.CTkFrame(
    main,
    fg_color="transparent"
)

form.pack(
    padx=40,
    fill="x"
)


# =========================
# VALIDAÇÕES
# =========================

vcmd_texto = (
    app.register(apenas_texto),
    "%P"
)

vcmd_numero = (
    app.register(apenas_numero),
    "%P"
)

vcmd_valor = (
    app.register(validar_valor),
    "%P"
)


# =========================
# FORNECEDOR
# =========================

label_fornecedor = ctk.CTkLabel(
    form,
    text="Fornecedor",
    font=ctk.CTkFont(
        size=13,
        weight="bold"
    )
)

label_fornecedor.grid(
    row=0,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=(0, 8)
)


InputFornecedor = ctk.CTkEntry(
    form,
    placeholder_text="Digite o fornecedor",
    height=45,
    corner_radius=10,
    validate="key",
    validatecommand=vcmd_texto
)

InputFornecedor.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=(0, 15),
    pady=(0, 25)
)


# =========================
# NÚMERO DA NF
# =========================

label_nf = ctk.CTkLabel(
    form,
    text="Número da NF",
    font=ctk.CTkFont(
        size=13,
        weight="bold"
    )
)

label_nf.grid(
    row=0,
    column=1,
    sticky="w",
    pady=(0, 8)
)


InputNF = ctk.CTkEntry(
    form,
    placeholder_text="Digite o número da NF",
    height=45,
    corner_radius=10,
    validate="key",
    validatecommand=vcmd_numero
)

InputNF.grid(
    row=1,
    column=1,
    sticky="ew",
    pady=(0, 25)
)


# =========================
# VALOR
# =========================

label_valor = ctk.CTkLabel(
    form,
    text="Valor da NF",
    font=ctk.CTkFont(
        size=13,
        weight="bold"
    )
)

label_valor.grid(
    row=2,
    column=0,
    sticky="w",
    padx=(0, 15),
    pady=(0, 8)
)


InputValor = ctk.CTkEntry(
    form,
    placeholder_text="R$ 0,00",
    height=45,
    corner_radius=10,
    validate="key",
    validatecommand=vcmd_valor
)

InputValor.grid(
    row=3,
    column=0,
    sticky="ew",
    padx=(0, 15),
    pady=(0, 25)
)


# =========================
# PEDIDO
# =========================

label_pedido = ctk.CTkLabel(
    form,
    text="Número do Pedido",
    font=ctk.CTkFont(
        size=13,
        weight="bold"
    )
)

label_pedido.grid(
    row=2,
    column=1,
    sticky="w",
    pady=(0, 8)
)


InputPedido = ctk.CTkEntry(
    form,
    placeholder_text="Digite o número do pedido",
    height=45,
    corner_radius=10,
    validate="key",
    validatecommand=vcmd_numero
)

InputPedido.grid(
    row=3,
    column=1,
    sticky="ew",
    pady=(0, 25)
)


# =========================
# CONFIGURAÇÃO DAS COLUNAS
# =========================

form.grid_columnconfigure(
    0,
    weight=1
)

form.grid_columnconfigure(
    1,
    weight=1
)


# =========================
# SEPARADOR
# =========================

separador = ctk.CTkFrame(
    main,
    height=1,
    fg_color="gray30"
)

separador.pack(
    padx=40,
    pady=5,
    fill="x"
)


# =========================
# BOTÃO
# =========================

button = ctk.CTkButton(
    main,
    text="Cadastrar Nota Fiscal",
    height=48,
    corner_radius=10,
    font=ctk.CTkFont(
        size=14,
        weight="bold"
    ),
    command=Button
)

button.pack(
    padx=40,
    pady=(25, 35),
    fill="x"
)


app.mainloop()
