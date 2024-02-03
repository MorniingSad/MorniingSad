#Hashtag passo a passo


import pyautogui
import time
# entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


# escrever -> pyautogui.write
# clicar -> pyautogui.click
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
pyautogui.PAUSE = 1


# apertar a tecla do windows
pyautogui.press("win")

# digitar o nome do prrenanheiro@gmail.com  123456  

pyautogui.write("chrome")

# entrar no programa
pyautogui.press("enter")

# digitar o link 
link = "https://mail.google.com/mail/u/0/?hl=pt_BR#inbox"
pyautogui.write(link)

# apertar o enter 
pyautogui.press("enter")
pyautogui.PAUSE = 1
# passo 2: fazer login no sistema
pyautogui.click(x=62, y=222)
pyautogui.write("Ola tudo bem ? ")
pyautogui.press("tab")
pyautogui.write("teste")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
# passo 3: importar base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# cadastrar um produto 
for linha in tabela.index:
# clicar no campo de cogido
    pyautogui.click(x=590, y=299)

    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    
    #marca
    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    #categoria

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #colocar números entre aspas ou srt() string 

    #preco unitario
    pyautogui.write (str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    #custo 
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
     pyautogui.press("tab")
    
    #Nan= not a number 
    #finalizar 
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# repetir o processo até finalizar a lista 
    


    






# passo 4: cadastrar um produto 
# passo 5: repetir isso até acabar renanheiro@gmail.com 123456  
