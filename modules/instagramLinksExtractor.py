import os
import sys
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

class InstagramLinksExtractor:
    
    def __init__(self, file_path, column_name):
        self.file_path = file_path
        self.column_name = column_name
    
    def extract_links(self):
        # Lê o arquivo .csv e seleciona a coluna especificada
        try:
            df = pd.read_csv(self.file_path)
            urls = (df[self.column_name])
        except:
            print("\n\nErro, verifique se o caminho e a coluna foi digitada corretamente", file=sys.stderr)
            print("extract_links>read_cvs-urls\n\n", file=sys.stderr)

            return

        
        # Cria uma lista para armazenar os links do Instagram encontrados
        instagram_links = []
        
        # Loop pelos URLs dos sites para buscar o link do Instagram
        for url in urls:
            #print(url + '1')
             # verifica se a URL é válida
            
            
            try:
                
                if (url.startswith('www.instagram.com/') or url.startswith('http://instagram.com/') or url.startswith('http://www.instagram.com/') or url.startswith('https://instagram.com/') or url.startswith('https://www.instagram.com/')):
                    instagram_links.append(url)
                    continue
            except:
                instagram_links.append('')
                continue
            #print(url)
            try:
                

                response = requests.get(url)
            except:
                instagram_links.append('')
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            instagram_link = soup.find('a', href=re.compile(r'^https:\/\/www\.instagram\.com\/'))
            if instagram_link :
                instagram_links.append(instagram_link['href'])
            else:
                instagram_links.append('')
        
        
        # Cria um novo dataframe com os links do Instagram encontrados
        df_instagram = pd.DataFrame({'Instagram': instagram_links})
        print(df_instagram)
        #Criar nova coluna no .csv
        file_name= os.path.splitext(os.path.basename(self.file_path))
        cvs_name= 'data/output/{self.file_name}-withInstagram.csv'
        df['Instagram'] = instagram_links
        df.to_csv(cvs_name, index=False)
        # Concatena o novo dataframe com o dataframe original
        #df_result = pd.concat([df, df_instagram], axis=1)
        
        return cvs_name
