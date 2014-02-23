## autor: luiz.anjos
##
## 1 - crie uma pasta temporária e mova todos os seus XHTML onde você procuraria os botões;
## 2 - usando o Notepad++, remova todos os caracteres ocultos dos arquivos (certifique-se que removeu, usando a opção de exibi-los);
## 3 - execute-me e passe o caminho do diretório temporário que você criou (sem "\" ou "/" no final);
## 4 - informe qual tag você deseja encontrar.
##
## Serão encontrados todas as tags do tipo informado.

from html.parser import HTMLParser
import codecs
import os

tagType = ""

## classe que extende o parser
class MyHTMLParser(HTMLParser):

    ## função chamada para cada tag econtrada no arquivo
    def handle_starttag(self, tag, attrs):

        global tagType

        ## obtém o id e o title dos botões
        if tag == tagType:

            print("Encontrei um", tag)
            print("Atributos:")

            for attr in attrs:
                print(attr[0] + "=\"" + attr[1] + "\"")

folderPath = input('Caminho do diretório (sem \"\\\" ou \"/\" no final):')
tagType = input('Tipo da tag (por ex.: \"h:commandbutton\"):')

for dirname, dirnames, filenames in os.walk(folderPath):

    ## para cada arquivo encontrado no diretório, faz o parse e imprime o bloco com as permissões do @Menu
    for filename in filenames:
        print("\n\n===================================", filename, "===================================")

        filePath = folderPath + "\\" + filename

        dados = open(filePath, "r", -1, "UTF-8").read()

        parser = MyHTMLParser(strict=False)
        parser.feed(dados)

