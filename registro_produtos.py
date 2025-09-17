import pyautogui, pandas as pd, time

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=974, y=472)
pyautogui.write("dony@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=961, y=663)
time.sleep(3)

# cadastrar produto 
# codigo,marca,tipo,categoria,preco_unitario,custo,obs

tabela = pd.read_csv("aula_1/produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=748, y=318)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    