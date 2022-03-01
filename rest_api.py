from re import T
import requests
import json
from PIL import Image, ImageFilter
import textwrap

#site = "http://www.themealdb.com/api/json/v1/1/lookup.php?i=52926"
site = "http://www.themealdb.com/api/json/v1/1/random.php"


class Comida:
    def __init__(self):
        request = requests.get(site)
        dados = json.loads(request.content)['meals'][0]
        self.data = dados


def bandera_pais(x):
    if x == "British":
        code = "gb"
    elif x == "American":
        code = "us"
    elif x == "French":
        code = "fr"
    elif x == "Canadian":
        code = "ca"
    elif x == "Jamaican":
        code = "jm"
    elif x == "Chinese":
        code = "cn"
    elif x == "Dutch":
        code = "de"
    elif x == "Egyptian":
        code = "eg"
    elif x == "Greek":
        code = "gr"
    elif x == "Indian":
        code = "in"
    elif x == "Irish":
        code = "ie"
    elif x == "Italian":
        code = "it"
    elif x == "Japanese":
        code = "jp"
    elif x == "Kenyan":
        code = "ke"
    elif x == "Malaysian":
        code = "my"
    elif x == "Mexican":
        code = "mx"
    elif x == "Moroccan":
        code = "ma"
    elif x == "Croatian":
        code = "hr"
    elif x == "Norwegian":
        code = "no"
    elif x == "Portuguese":
        code = "pt"
    elif x == "Russian":
        code = "ru"
    elif x == "Argentinian":
        code = "ar"
    elif x == "Spanish":
        code = "es"
    elif x == "Slovakian":
        code = "sk"
    elif x == "Thai":
        code = "th"
    elif x == "Saudi Arabian":
        code = "sa"
    elif x == "Vietnamese":
        code = "vn"
    elif x == "Turkish":
        code = "tr"
    elif x == "Syrian":
        code = "sy"
    elif x == "Algerian":
        code = "dz"
    elif x == "Tunisian":
        code = "tn"
    elif x == "Polish":
        code = "pl"

    url = "https://flagcdn.com/108x81/"+code+".png"
    response = requests.get(url)
    return response.content


def gera_texto(data2):
    texto = " • " + \
        arruma_nome2(data2['strIngredient1']) + " - " + \
        arruma_nome2(data2['strMeasure1'])
    texto += "\n • " + \
        arruma_nome2(data2['strIngredient2']) + " - " + \
        arruma_nome2(data2['strMeasure2'])
    texto += "\n • " + \
        arruma_nome2(data2['strIngredient3']) + " - " + \
        arruma_nome2(data2['strMeasure3'])
    texto += "\n • " + \
        arruma_nome2(data2['strIngredient4']) + " - " + \
        arruma_nome2(data2['strMeasure4'])

    if(data2['strIngredient5'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient5']) + \
            " - " + arruma_nome2(data2['strMeasure5'])

    if (data2['strIngredient6'] != ""):
        texto += "\n • " + arruma_nome2(data2['strIngredient6']) + \
            " - " + arruma_nome2(data2['strMeasure6'])

    if (data2['strIngredient7'] != "" and data2['strIngredient7'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient7']) + \
            " - " + arruma_nome2(data2['strMeasure7'])

    if (data2['strIngredient8'] != "" and data2['strIngredient8'] != ""):

        texto += "\n • " + \
            arruma_nome2(data2['strIngredient8']) + " - " + \
            arruma_nome2(data2['strMeasure8'])

    if (data2['strIngredient9'] != "" and data2['strIngredient9'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient9']) + \
            " - " + arruma_nome2(data2['strMeasure9'])

    if (data2['strIngredient10'] != "" and data2['strIngredient10'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient10']) + \
            " - " + arruma_nome2(data2['strMeasure10'])

    if (data2['strIngredient11'] != "" and data2['strIngredient11'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient11']) + \
            " - " + arruma_nome2(data2['strMeasure11'])

    if (data2['strIngredient12'] != "" and data2['strIngredient12'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient12']) + \
            " - " + arruma_nome2(data2['strMeasure12'])

    if (data2['strIngredient13'] != "" and data2['strIngredient13'] != ""):

        texto += "\n • " + arruma_nome2(data2['strIngredient13']) + \
            " - " + arruma_nome2(data2['strMeasure13'])

    if (data2['strIngredient14'] != "" and data2['strIngredient14'] != ""):

        texto += "\n • " + \
            arruma_nome2(data2['strIngredient14']) + " - " + \
            arruma_nome2(data2['strMeasure14'])

    if (data2['strIngredient15'] != "" and data2['strIngredient15'] != ""):
        texto += "\n • " + \
            arruma_nome2(data2['strIngredient15']) + " - " + \
            arruma_nome2(data2['strMeasure15'])

    return texto


def arruma_nome2(nome):
    nome = textwrap.fill(text=nome, width=25,
                         max_lines=22, initial_indent=" ")
    return nome
