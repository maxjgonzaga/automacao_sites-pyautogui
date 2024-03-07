import webbrowser
import pyautogui
from time import sleep

# Abrir site
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(1)
# Clicar dentro do site
pyautogui.click(1119, 235, duration=1)
# scrolar até ponto desejado
pyautogui.scroll(-2300)
sleep(2)
# Encontrar e clicar no campo "digite seu nome"
pyautogui.click(915,227, duration=1)
sleep(2)
# Digitar seu nome
pyautogui.typewrite('Max Gonzaga')
# Abrir a alerta
pyautogui.click(894,269, duration=1)
sleep(2)
# Fechar a alerta
pyautogui.click(1250,208, duration=1)
sleep(2)
# Subir toda a Pagina
pyautogui.scroll(2300)
sleep(2)
# Descer a página ate arquivos
pyautogui.scroll(-3300)
sleep(1)
# Baixar arquivo excel
pyautogui.click(911,478, duration=1)
sleep(5)
# Clicar em algum ponto para sair da janela de download
pyautogui.click(944,597, duration=1)
# Alertar que TERMINOU
pyautogui.alert('TERMINOU')
