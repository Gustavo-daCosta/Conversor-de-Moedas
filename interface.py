from tkinter import *
from tkinter import messagebox, ttk
from requests import get

app = Tk()
app.title("Conversor de Moedas")
app.geometry( "495x355")
app.iconbitmap("image/coin-logo.ico")
app.resizable(False, False)
app.configure(background="#253a4e")



def converter():
    moedaOrigem = MoedaOrigemBox.get()
    moedaFinal = MoedaFinalBox.get()
    try:
        valor = float(ValorText.get('1.0', 'end-1c'))
    except:
        messagebox.showerror('ERRO', 'Digite um valor válido! Composto por somente números e pontos(.)')
        valor = None
    global resultadoExiste, resultado
    resultadoExiste = False
    moeda = f'{moedaOrigem}-{moedaFinal}'
    request = get(f'https://economia.awesomeapi.com.br/last/{moeda}').json()
    moedaExiste = False
    try:
        print(request['code'])
    except:
        moedaExiste = True
    if moedaExiste is True:
        coinInfo = request[moedaOrigem+moedaFinal]
        resultado = float(coinInfo['high']) * float(valor)
        resultadoExiste = True
        data = coinInfo['create_date']
        retorno = f'Data da Cotação: {data}\n\n\t{valor:.2f} {moedaOrigem} = {resultado:.2f} {moedaFinal}'
        TextBoxResultado.delete('1.0', END)
        TextBoxResultado.insert(END, retorno)
    else:
        if valor != None:
            messagebox.showerror('Erro', 'Erro ao acessar a API, moeda inválida')

def limpar():
    TextBoxResultado.delete('1.0', END)
    MoedaOrigemBox.set('')
    MoedaFinalBox.set('')
    ValorText.delete('1.0', END)

def sair():
    app.destroy()

def copiar():
    if resultadoExiste is True:
        app.clipboard_clear()
        app.clipboard_append(f'{resultado:.2f}')
        app.update()
    else:
        messagebox.showwarning('Aviso', 'Você deve converter algum valor antes de copiá-lo.')

def semComando():
    print('Função semComando')

backgroundColor = '#253a4e'
TextBoxColor = '#4c6378'


barra_menu = Menu(app)

menuComandos = Menu(barra_menu, tearoff=0)
menuComandos.add_command(label = 'Converter', command=converter)
menuComandos.add_command(label = 'Limpar', command=limpar)
menuComandos.add_command(label = 'Copiar', command=copiar)
menuComandos.add_separator()
menuComandos.add_command(label = 'Sair', command=sair)
barra_menu.add_cascade(label='Comandos', menu=menuComandos)

# Janela [Lista de moedas disponíveis] do Menu de comandos
def moedasDisponiveis():
    WindowMoedas = Toplevel(app)
    WindowMoedas.title('Lista de Moedas Disponíveis')
    WindowMoedas.geometry('820x435')
    WindowMoedas.iconbitmap("image/coin-logo.ico")
    WindowMoedas.resizable(False, False)
    WindowMoedas.configure(background="#253a4e")

    TituloWindowMoedas = Label(WindowMoedas, text="Lista de Moedas Disponíveis", bg=backgroundColor, fg='white', font=("Arial", 24))
    TituloWindowMoedas.place(x=200, y=10)

    separatorMoedas = ttk.Separator(WindowMoedas, orient=HORIZONTAL)
    separatorMoedas.pack(fill='x', pady=58)

    TitleMoeda = Label(WindowMoedas, text = "Moeda", bg = backgroundColor, fg='white')
    TitleMoeda.place(x=2, y=30)

    TextBoxMoedas = Text(WindowMoedas, width=110, height=16, bg=TextBoxColor, fg='white', font=("Arial", 12))
    TextBoxMoedas.pack(side=LEFT, padx=10, pady=10)

    request = get('https://economia.awesomeapi.com.br/json/all').json()
    moedas = ['USD', 'USDT', 'CAD', 'GBP', 'ARS', 'BTC', 'LTC', 'EUR', 'JPY', 'CHF', 'AUD', 'CNY', 'ILS', 'ETH', 'XRP', 'DOGE']
    for c in range(0, len(moedas)):
        code, codein, name, cotacao, data = request[moedas[c]]['code'] , request[moedas[c]]['codein'], request[moedas[c]]['name'], float(request[moedas[c]]['high']), request[moedas[c]]['create_date']
        retorno = (f'{code} → {codein}\t\t{name}\t\t\t\t\t{cotacao:.2f}\t\t{data}')
        TextBoxMoedas.insert(END, retorno)
        TextBoxMoedas.insert(END, '\n')
    
    def sair():
        WindowMoedas.destroy()

    BotaoSairMoedas = Button(WindowMoedas, text='Sair', bg='red', fg='white', font=("Arial", 12), command=sair)
    BotaoSairMoedas.place(x=750, y=10)

    WindowMoedas.mainloop()


menuListaMoedas = Menu(barra_menu, tearoff=0)
menuListaMoedas.add_command(label = 'Moedas Disponíveis', command=moedasDisponiveis)
menuListaMoedas.add_separator()
menuListaMoedas.add_command(label = 'API Utilizada', command=semComando)
barra_menu.add_cascade(label='Lista de Moedas', menu=menuListaMoedas)


menuAjuda = Menu(barra_menu, tearoff=0)
menuAjuda.add_command(label='Como utilizar o programa?', command=semComando)
menuAjuda.add_command(label='Como o programa funciona?', command=semComando)
barra_menu.add_cascade(label='Ajuda', menu=menuAjuda)

menuSobre = Menu(barra_menu, tearoff=0)
menuSobre.add_command(label = 'Autor', command=semComando)
menuSobre.add_command(label = 'Código Fonte', command=semComando)
barra_menu.add_cascade(label='Sobre', menu=menuSobre)

app.config(menu = barra_menu)

Titulo = Label(app, text="Conversor de Moedas", bg=backgroundColor, fg='white', font=("Arial", 24))
Titulo.place(x=95, y=8)

separator = ttk.Separator(app, orient='horizontal')
separator.pack(fill='x', pady=58)

ValorLabel = Label(app, text='Valor :', bg=backgroundColor, fg='white', cnf={"width": 10, "height": 1}, font=("Arial", 14))
ValorLabel.place(x=95, y=65)

ValorText = Text(app, width=20, height=1, bg=TextBoxColor, fg='white', font='Arial')
ValorText.place(x=182, y=70)

msgMoedasLabel = Label(app, text='Selecione a moeda desejada.', bg=backgroundColor, fg='white', cnf={"width": 25, "height": 1}, font=("Arial", 12))
msgMoedasLabel.place(x=135, y=100)

listaMoedasDisponiveis = [
    'BRL', 'USD', 'EUR', 'BRLT', 'CAD', 'GBP', 'ARS', 'JPY', 'CHF', 'AUD', 'CNY', 'BTC', 'LTC', 'ETH', 'XRP', 'DOGE'
]
MoedaOrigemLabel = Label(app, text='Moeda de Origem:', bg=backgroundColor, fg='white', cnf={"width": 15, "height": 1}, font=("Arial", 12))
MoedaOrigemLabel.place(x=4, y=145)

MoedaOrigemBox = ttk.Combobox(app, values=listaMoedasDisponiveis, state='readonly', width=6, font=("Arial", 12))
MoedaOrigemBox.place(x=147, y=145)

MoedaFinalLabel = Label(app, text='Moeda de Destino:', bg=backgroundColor, fg='white', cnf={"width": 15, "height": 1}, font=("Arial", 12))
MoedaFinalLabel.place(x=247, y=145)

MoedaFinalBox = ttk.Combobox(app, values=listaMoedasDisponiveis, state='readonly', width=6, font=("Arial", 12))
MoedaFinalBox.place(x=392, y=145)

TextBoxResultado = Text(app, width=42, height=4, bg=TextBoxColor, fg='white', font=('Arial', 14))
TextBoxResultado.place(x=14, y=190)

BotaoConverter = Button(app, text='Converter', bg='#127a18', activebackground='#105213', fg='white', font=('Arial', 12), command=converter)
BotaoConverter.place(x=18, y=290)

BotaoCopiar = Button(app, text='Copiar', bg='#4c6378', activebackground='#2b3f52', fg='white', font=('Arial', 12), command=copiar)
BotaoCopiar.place(x=108, y=290)

BotaoLimpar = Button(app, text='Limpar', bg='#4c6378', activebackground='#2b3f52', fg='white', font=('Arial', 12), command=limpar)
BotaoLimpar.place(x=178, y=290)

BotaoSair = Button(app, text='Sair', bg='#ab2028', activebackground='#700f14', fg='white', font=('Arial', 12), command=sair)
BotaoSair.place(x=433, y=290)


app.mainloop()