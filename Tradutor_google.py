from tkinter import Tk, ttk, Text
from ttkthemes import ThemedTk
from ttkbootstrap import Style
from googletrans import Translator

translator = Translator()

#Janela TK Default
#janela = Tk()

#janela = ThemedTk(theme='clearlooks')
style = Style(theme='superhero')
janela = style.master

frame_geral = ttk.Frame()

janela.title('Google Translate')

def traduzir(evento=None):
    #resultado = translator.translate()
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=texto, src=src, dest=dest)

    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado.text)
    saida.configure(state='disable')


#janela.configure(bg='black')

values = ['pt', 'es', 'en']

#Entradas
frame_entrada = ttk.Frame(frame_geral)

label_entrada = ttk.Label(
    frame_entrada,
    text='Entrada',
    font=(None, 10)
)

combo_entrada = ttk.Combobox(
    frame_entrada,
    values=values,
    font=(None, 10)
)
combo_entrada.set('pt')

label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
frame_entrada.pack()

entrada = Text(frame_geral, height=10, width=50)
entrada.pack(padx=10, fill='both', expand='yes')

#Saidas
frame_saida = ttk.Frame(frame_geral)

label_saida = ttk.Label(
    frame_saida,
    text='Saída',
    font=(None, 10)
)

combo_saida = ttk.Combobox(
    frame_saida,
    values=values,
    font=(None, 10)
)
combo_saida.set('en')

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)
frame_saida.pack()

saida = Text(frame_geral,height=10, width=50, font=(None, 15))
saida.pack(padx=10, fill='both', expand='yes')

botao = ttk.Button(
    frame_geral,
    text='Traduzir',
    command=traduzir
)
botao.pack(padx=10, pady=10)

janela.bind('<Return>', traduzir)
frame_geral.pack()

janela.mainloop()

