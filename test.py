
#Import de Bibliotecas
import PySimpleGUI as sg   
from pytube import YouTube
import os

#Tema do Aplicativo
sg.theme ('DarkRed2')

#lAYOUT DO PROGRAMA
layout = [
                 [sg.CB('Música'), sg.CB('Vídeo')], 
                 [sg.Text('Informe o link do video:           '), sg.InputText()],
                 [sg.Text('Informe o diretório para salvar: '), sg.InputText(), sg.FolderBrowse('Procurar')],
                 [sg.Button('Download', size=(12, 1), key='Download'), sg.Button('Info', size=(5, 1))]]

#Configurações da Janela
popup = sg.Window("YT Download", icon='Images/igm.ico').Layout(layout)

#While Configurado para sempre voltar ao ínicio
while True:
    
    #Eventos
    event, values = popup.read()
    
    #Evento para fechar a janela
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    
    #Evento para Informações do Programa
    elif event == 'Info':
        sg.popup_ok('Selecione uma das caixas, Cole o link, Procure o diretório que deseja salvar, Clique em Download!', icon='Images/igm.ico')  
    
    #Impedir que o Usuário tente baixar algo sem o link e o programa feche
    if values[2] == '':
         sg.popup_ok('Insira um link!', icon='Images/igm.ico')    
    
    #Evento de download de músicas
    elif event == 'Download':
       if values[0] == True:
           video = YouTube(values[2])
           out_file = video.streams.filter(only_audio=True).first().download(output_path=values[3])
           base, ext = os.path.splitext(out_file)
           new_file = base + '.mp3'
           os.rename(out_file, new_file)
           sg.popup_ok('Sua Música ou Audio foi baixada(o) com sucesso!\n' + video.title, icon='Images/igm.ico')
     
     #Evento de Download dos Vídeos
       elif values[1] == True:
           yt = YouTube(values[2])
           video = yt.streams.filter(only_audio=False).first()
           out_file = video.download(output_path=values[3])
           base, ext = os.path.splitext(out_file)
           new_file = base + '.mp4'
           os.rename(out_file, new_file)
           sg.popup_ok('Seu video foi baixado com sucesso!\n' + yt.title, icon='Images/igm.ico')
       
       #Caso o usuário não escolha nada 
       else: 
            sg.popup_ok('Escolha uma das opções ou Insira um link!', icon='Images/igm.ico')  
            

#Fechamento de popup
popup.close()