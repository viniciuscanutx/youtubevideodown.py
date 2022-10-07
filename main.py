# Importação de Pacotes
from pytube import YouTube
import os
 
#Não deixa o programa terminar
while True:

 print('\nSELECIONE: \n1 Para Video \n2 Para Musica \n')
 escolhe1 = input('Deseja baixar video ou musica? \n>>')
 
 
 def baixarmusica():
# Introdução de URL
  yt = YouTube(
    str(input("\nInsira a URL do Video/Musica \n>> ")))
# Extraindo apenas o áudio
  video = yt.streams.filter(only_audio=True).first()
# Destino do Arquivo
  print("\nInsira o Destino do Arquivo (Local a ser Salvo)")
  destination = str(input(">> ")) or '.'
# Linha que faz o download
  out_file = video.download(output_path=destination) 
# Salve o Arquivo - Converte para mp3
  base, ext = os.path.splitext(out_file)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)
# Resultado - Sucesso
  print("\n Sua Música ou Audio - " + yt.title + " - Foi baixado com sucesso!\n\n ")


 def baixarvideo(): 
# Introdução de URL 
    yt = YouTube(
    str(input("\nInsira a URL do Video/Musica \n>> ")))
# Linha de filtros
    video = yt.streams.filter(only_audio=False).first()
# Destino do Arquivo
    print("\nInsira o Destino do Arquivo (Local a ser Salvo)")
    destination = str(input(">> ")) or '.'
# Linha que faz o download
    out_file = video.download(output_path=destination)
# Salve o Arquivo - Deixa ele em mp4
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
# Resultado - Sucesso
    print("\n Seu video - " + yt.title + " - Foi baixado com sucesso!\n\n ")
#Repete a solução novamente - volta pro ínicio
 if escolhe1 == '2':
    baixarmusica()
 elif escolhe1 == '1':
    baixarvideo()
 else:
    print('Opção Inválida\n\n')
    continue