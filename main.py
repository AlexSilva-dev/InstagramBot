import argparse
import datetime
import os
import pickle
import sys

from modules.instagramBot import InstagramBot
from modules.instagramLinksExtractor import InstagramLinksExtractor


class Main:
    
    def __init__(self):
        self.file_path ='data_sheet/'
        self.column_name=''
        self.fileInput_path ='data/input/messagem.txt'
        self.txtInput=''

    def input(self, nameFile):
        
        #file_path = input("Digite o caminho do arquivo .csv que será usado: \n")
        #column_name = input("Digite o nome da coluna que contem o site (o nome tem que ser identico): \n") 
        self.column_name= "Site"
        self.file_path+=nameFile[0]
        self.txtInput=''
        self.listMessage=[]
        if(os.path.exists(self.fileInput_path)):
            with open(self.fileInput_path, 'r') as f:
                self.txtInput = f.read()
            
            if len(self.txtInput.strip())<=10:
                print('\n\nAntes de continuar é necessario criar entradas no arquivo localizado em: \n' + self.fileInput_path )
                print('\n\n')

                exit()
                
        else:
            createFile=open(self.fileInput_path,'w')
            createFile.close()
            print('\n\nAntes de continuar é necessario criar entradas no arquivo localizado em: \n' + self.fileInput_path )
            print('\n\n')
            exit()




    def handleInput(self):
        self.listMessage=self.txtInput.split("\\fim")



    def run(self, login, nameFile):

        self.log='data/output/log.txt'
        if(not os.path.isfile(self.log)):
                with open(self.log, 'w') as log:
                    log.write('\t\tArquivo log:\n\n')
                
        
        self.input(nameFile=nameFile)
        self.handleInput()
        
        print('Aguarde a captura de instagram...')
        #return
        try:
            objInstagramLinksExtractor = InstagramLinksExtractor(self.file_path, self.column_name, log=self.log)
            new_csv = objInstagramLinksExtractor.extract_links()
        except Exception as e:
            with open(self.log, 'a') as log:
                now = datetime.datetime.now()
                hour = now.strftime("\n\n\n\t\t%d/%m/%Y %H:%M")    
                log.write(hour + '\tmain>run')
                log.write('\n' + str(e.args))
            exit()
        print()

        
        instagramBot = InstagramBot(listMessage=self.listMessage, login=login, log=self.log)
        instagramBot.run(file_csv=new_csv)
        print('Concluido com sucesso!')

    

parser= argparse.ArgumentParser()
parser.add_argument('arquivos', metavar='arquivos.csv', nargs='+', help='Digite o nome do arquivo com sua extenção (exem;arquivo.csv) que está na pasta data_sheet.' )
parser.add_argument('--login', action='store_true' ,help='Argumento para usar fazer login no instagram')

args = parser.parse_args()
main = Main()
main.run(login=args.login, nameFile=args.arquivos)
