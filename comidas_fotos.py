import requests
import json
from rest_api import *
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import textwrap
from instagrapi import Client


def arruma_nome(nome, num):
    separados = nome.split()
    lengh = len(separados)

    if(lengh >= 4):
        nome_final = separados[0] + " "
        for vz in range(1, lengh):
            if((vz == num) or (vz == (2*num)) or (vz == (3*num)) or (vz == (4*num)) or (vz == (5*num))):
                nome_final += "\n" + separados[vz] + " "
            else:
                nome_final += separados[vz] + " "
            vz += 1
        return nome_final

    else:
        return nome


def monta_capa(food):
    # Pega Img Fundo
    response = requests.get(food['strMealThumb'])
    img = Image.open(BytesIO(response.content))
# Largura e comprimento
    larg = img.size[0]
    comp = img.size[1]

# Ajuste para Edicoes
    montagem = ImageDraw.Draw(img)
    nome_comida = arruma_nome(food['strMeal'], 3)
    font1 = ImageFont.truetype('./Pacotes/NTWagner.otf', 45)

# Pega Bandeira
    pais = Image.open(BytesIO(bandera_pais(food['strArea'])))
    pais = pais.convert("RGBA")
    Image.Image.paste(
        img, pais, ((((larg*3)//4)+57), (((comp*8)//9)-10)), mask=pais)


# Ajuste de cor
    colors = img.getpixel(((larg/2), (comp/9)))
    r = (255-colors[0])
    g = (255-colors[1])
    b = (255-colors[2])

    if((r < 50) and (g < 50) or (b < 50)):
        cont = 240
    else:
        cont = 0

# Marca Dagua
    marca = Image.open("./Pacotes/marca_dagua.png")
    marca = marca.convert("RGBA")
    Image.Image.paste(
        img, marca, (0, 0), mask=marca)

# Montagem do texto
    montagem.multiline_text(((larg/2), (comp/9)), nome_comida,
                            (r, g, b), font=font1, anchor="ms", stroke_width=1, stroke_fill=(cont, cont, cont), align="center")
    img.save("./Imagens/comida.jpg")


def monta_ingredientes(food):
    # Gera texto com ingredientes
    texto = gera_texto(food)

    # Gera imagem com a lista
    lista = Image.open("./Pacotes/fundo_papel.jpg")
    montagem_lista = ImageDraw.Draw(lista)
    font1 = ImageFont.truetype('./Pacotes/Arial.ttf', 40)

    # Coloca os Textos
    montagem_lista.text((45, 65), texto, (0, 0, 0),
                        font=font1, align="left", spacing=5)
    lista.save("./Imagens/ingredientes.jpg")


def monsta_instrucoes(food):
    # Pega texto com instrucoes
    passos = food['strInstructions']
    passos = textwrap.fill(text=passos, width=50,
                           max_lines=22, initial_indent=" ")

    # Gera imagem com as instrucoes
    instru = Image.open("./Pacotes/fundo_passos.jpg")
    montagem_instru = ImageDraw.Draw(instru)
    font2 = ImageFont.truetype('./Pacotes/Arial.ttf', 25)

    # Coloca os Textos
    montagem_instru.multiline_text((50, 60), passos, (0, 0, 0),
                                   font=font2, align="left", spacing=5)
    instru.save("./Imagens/instrucoes.jpg")


def posta_instagram(food):
    # Atribui login e senha para conta
    with open("login.json", encoding='utf-8') as infs:
        dados = json.load(infs)
    cl = Client()
    cl.login(dados[0]['login'], dados[0]['senha'])

    # Lista com as fotos e dados para postar
    fotos = ["./Imagens/comida.jpg",
             "./Imagens/ingredientes.jpg", "./Imagens/instrucoes.jpg"]
    escrito = '{}!! \n \n #{} #{}food #{} #food #foodbot #recipe #python  \n Made in Python'.format(
        food['strMeal'], food['strCategory'], food['strArea'], food['strArea'])

    # Faz a postagem
    media = cl.album_upload(
        fotos,
        escrito,

    )


def verifica_post(id):
    # Abre o arquivo
    registro = open("./Imagens/ids.txt")

    # Cria variavel com todas as linhas
    ids = registro.readlines()
    registro.close()

    # Procura para ver se ja  foi postada
    for x in ids:
        if(x == id):
            return False
    return True


def salva_id(id):
    # Abre o arquivo
    registro = open("./Imagens/ids.txt","a")

    # Salva id  na linha
    registro.write("\n"+id)
    registro.close()


def pegar_comida():
    print("|---------------| Obtendo dados")
    food = Comida().data
    print(food['strMeal'])
    if(verifica_post(food['idMeal'])):
        print("|===------------| Montando Capa")
        monta_capa(food)
        print("|======---------| Montando Ingredientes")
        monta_ingredientes(food)
        print("|=========------| Montando instrucoes")
        monsta_instrucoes(food)
        print("|============---| Postando")
        posta_instagram(food)
        print("|===============| Completo")
        salva_id(food['idMeal'])
    else:
        print("|xxxxxxxxxxxxxxx| Comida já postada")
        pegar_comida()


if __name__ == '__main__':
    pegar_comida()
