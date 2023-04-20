import argparse
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

    def input(self):
        
        #file_path = input("Digite o caminho do arquivo .csv que será usado: \n")
        #column_name = input("Digite o nome da coluna que contem o site (o nome tem que ser identico): \n") 
        self.column_name= "Website"
        self.file_path+='a.csv'
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
    def run(self, login):
        
        self.input()
        self.handleInput()
        print(len(self.listMessage)-1)
        
        #return
        try:
            nstagramLinksExtractor = InstagramLinksExtractor(self.file_path, self.column_name)
            new_csv = nstagramLinksExtractor.extract_links()
        except:
            exit()
        print()


        instagramBot = InstagramBot(listMessage=self.listMessage, login=login)
        instagramBot.run(file_csv=new_csv)

    

parser= argparse.ArgumentParser()
parser.add_argument('--login', action='store_true' ,help='Argumento para usar fazer login no instagram')
args = parser.parse_args()
print(args.login)
main = Main()
main.run(login=args.login)
