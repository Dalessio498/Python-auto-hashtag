import pyautogui
import time

# pyautogui.click -> clicar
#|| .press apertar (1) tecla
#|| .write escrever um texto
#|| .hotkey aperta uma combinação de teclas ("ctrl", "c") + 1 tecla
# Passo 1: entrar no sistema do arquivo - https://dlp.hashtagtreinamentos.com/python/intensivao/login

#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.PAUSE = 1
pyautogui.press("enter")

#digitar o treco
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pyautogui.write(site)
#pyautogui.press("enter")


time.sleep(5) #tempo do codigo entre linhas

# Passo 2: fazer login

pyautogui.click(x=390, y=366) #se precisar tu adapta pro pc q usar!amtoniomarco91@gmail.com clicks=2
pyautogui.write("amtoniomarco91@gmail.com")
time.sleep(1)

pyautogui.press("tab")
pyautogui.write("psplus14")
time.sleep(1)
pyautogui.press("enter")

time.sleep(3)

# Passo 3: importar a base de dados

# .csv maior parte de empresas usam para exportar (base de dados)

import pandas as pd

#importa a bibloteca que importa a base de dados!
#armazena na var tabela, melhor usar nomes intuitivos, e seguir regras de variavel.

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: cadastrar um produto

#marca = "Logitech" para ir um a um
    #pyautogui.press("tab")
    #pyautogui.write(marca)

# Passo 5: repetir para todos os produtos

for linha in tabela.index: #para cada linha dentro da minha tabela, executar isso daqui (indice/linha - index)
#ele sabe q quer uma linha por chamar o .index, com coluna seria .columns
    pyautogui.click(x=469, y=259)

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)

    #marca = "Logitech" para ir um a um
    #pyautogui.press("tab")
    #pyautogui.write(marca)

    marca = tabela.loc[linha,"marca"]
    pyautogui.press("tab")
    pyautogui.write(marca)


    tipo = tabela.loc[linha,"tipo"]
    pyautogui.press("tab")
    pyautogui.write(tipo)


    categoria = str(tabela.loc[linha,"categoria"]) #string - texto / str()
    pyautogui.press("tab")
    pyautogui.write(categoria)


    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)


    custo = str((tabela.loc[linha,"custo"]))       
    pyautogui.press("tab")
    pyautogui.write(custo)
    
    
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.press("tab")
        pyautogui.write(obs)
       

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000) #É valido usar o press home

#selecionar tudo e dar tab - identação, diz q esta dentro do for

