import sys
import pickle
import os
from modules.instagramLinksExtractor import InstagramLinksExtractor
from modules.instagramBot import InstagramBot


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

    def run(self):
        self.input()
        print("certo")
        return
        try:
            nstagramLinksExtractor = InstagramLinksExtractor(self.file_path, self.column_name)
            new_csv = nstagramLinksExtractor.extract_links()
        except:
            exit()
        print()


        instagramBot = InstagramBot()
        instagramBot.run(file_csv=new_csv)

    


main = Main()
main.run()
