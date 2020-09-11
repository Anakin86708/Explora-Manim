#!/usr/bin/env python3
import json
import subprocess
from os import path
from os import system


def render(index_video, resolucao):
    # Inicia render
    nome_desejado = nomes_videos[index_video]
    video_desejado = file['videos']['nome' == nome_desejado]
    for item in file['videos']:
        if item['nome'] == nome_desejado:
            video_desejado = item
            break

    caminho = video_desejado['caminho']
    num_scenes = video_desejado['num_scenes']
    itens_to_render = [str(i) for i in range(1, num_scenes + 1)]
    itens_to_render = ','.join(itens_to_render)
    query = f'manim {caminho} -r {resolucao} <<< {itens_to_render}'
    print(f'running {query}')
    subprocess.run(query, shell=True, executable='/bin/bash')

    # Verifica se o diretório existe
    nome_dir = file['destino_render']
    if not path.isdir(nome_dir):
        system(f'mkdir {nome_dir}')
    if not path.isdir(f'{nome_dir}{resolucao}p60'):
        system(f'mkdir {nome_dir}{resolucao}p60')

    # Cria vídeo final
    destino_render = file['destino_render']
    lista = video_desejado['lista_concat']
    query = f'ffmpeg -loglevel warning -f concat -safe 0 -i {lista} -c copy '\
        f'{destino_render}{resolucao}p60/{nome_desejado}_{resolucao}.mp4 <<< y'
    print(f'running {query}')
    subprocess.run(query, shell=True, executable='/bin/bash')


# Lê a config, ou cria, se necessário
try:
    config = open('.config.json', 'r')
except FileNotFoundError:
    open('.config.json', 'x')
    config = open('.config.json', 'r')
# Apresenta opções de render
file = json.load(config)
nomes_videos = [item['nome'] for item in file['videos']]
print('Selecione um vídeo para renderizar:')
print('0 - Todos')
for index, nome in enumerate(nomes_videos):
    print(f'{index + 1} - {nome}')

# Espera por um valor válido
while True:
    try:
        ans = int(input())
        if ans in range(len(nomes_videos)+1):
            index_video = ans - 1
            break
        else:
            raise ValueError
    except ValueError:
        print('Insira um número correspondente ao vídeo')

# Pergunta resolução
print('Resolução desejada (insira apenas o número):')
while True:
    try:
        resolucao = int(input())
        break
    except ValueError:
        print('Insira um número válido')

# Verifica se irá renderizar todos os itens
if ans == 0:
    for index_video in range(len(nomes_videos)):
        render(index_video, resolucao)
else:
    render(index_video, resolucao)
