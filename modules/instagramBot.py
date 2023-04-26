import os
import sys
import time
import random
import warnings
import datetime
import pandas as pd

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


warnings.filterwarnings("ignore", message="This pattern is interpreted as a regular expression, and has match groups.")

class InstagramBot:


    def __init__(self, login:bool=False, listMessage:str=[], log:str=''):
        
        self.log=log
        self.listMessage=listMessage
        self.cont_messagesSent=0
        self.input_path='data/output/'
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=selenium")
        options.add_argument("--remote-debugging-port=9222")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=selenium')
        self.options.add_argument("--remote-debugging-port=9222")
        self.options.add_argument('--headless')
        
        self.driver = webdriver.Chrome(options=options)
        self.waitTime=60
        if(login==True):
            try:
                self.driver.get('https://www.instagram.com/')
                
                while self.driver.window_handles:
                    try:
                        # código para acessar a janela
                        time.sleep(1)  # espera 1 segundo antes de verificar novamente

                    except NoSuchWindowException:
                        break
            except:
                print("\n\nLogin feito com sucesso!\n\n")


                # ATIVAR MODO BACKGROUND
                #self.driver = webdriver.Chrome(options=self.options)
                self.driver = webdriver.Chrome(options=options)
                return
        else:
            return


    def send_message(self, url):
        
        try:
            self.driver.get(url)
        except Exception as e:
                with open(self.log, 'a') as log:
                    now = datetime.datetime.now()
                    hour = now.strftime("%d/%m/%Y %H:%M")    
                    log.write('\n\n\n\t\t' + hour + '\tInstagramBot>send_message')
                    log.write('\nErro no get da url; {} \n'.format(url))
                    log.write("\n"+url)
                    log.write('\n' + str(e.args))
                return 

        now = datetime.datetime.now()
        hour = now.strftime("%d-%m-%Y_%H-%M")
        path_screenshot=self.input_path + "screenshot-{}.png".format(hour)
        try:
            try:
                element_notification = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
                element_notification.click()
            except Exception as e:

                mensagem_button = WebDriverWait(self.driver, random.randrange(3, 10)).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 x10w6t97 xl56j7k x17ydfre x1f6kntn x1swvt13 x1pi30zi x2b8uid xlyipyv x87ps6o x14atkfc x1n2onr6 x1d5wrs8 x1gjpkn9 x175jnsf xsz8vos"]')))
                self.driver.save_screenshot(path_screenshot )
                mensagem_button.click()
        except:
            try:
                follow_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
                follow_button.click()
            except Exception as e:
                with open(self.log, 'a') as log:
                    now = datetime.datetime.now()
                    hour = now.strftime("%d/%m/%Y %H:%M")    
                    log.write('\n\n\n\t\t' + hour + '\tInstagramBot>send_message')
                    log.write('\nErro ao clickar no botão de mensagem para abrir o direct da pagina alvo \n')
                    log.write("\n"+url)
                    log.write('\n' + str(e.args))
                return 
        
        if(os.path.exists(path_screenshot)):
            os.remove(path_screenshot)
        
        try:
            # Espera até que o campo esteja visível na página
            campo = WebDriverWait(self.driver, random.randrange(3,10)).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
            
            # Digita no campo
            randomMessage = self.listMessage[random.randrange(len(self.listMessage))]
            randomMessage+='\n'
            time.sleep(random.randrange(1,3))
            action_chains = ActionChains(self.driver)
            for char in randomMessage:
                action_chains.send_keys(char).perform()
                time.sleep(random.uniform(0.0, 0.15))
            time.sleep(random.randint(1,4))
            action_chains.send_keys(Keys.RETURN)
            #campo.send_keys(randomMessage)
             # Envia o formulário
            #campo.send_keys(Keys.RETURN)
            time.sleep(random.randint(3,10))

        except Exception as e:
            with open(self.log, 'a') as log:
                now = datetime.datetime.now()
                hour = now.strftime("%d/%m/%Y %H:%M")    
                log.write('\n\n\n\t\t' + hour + '\tInstagramBot>send_message')
                log.write('\nErro ao escrever no campo e enviar a mensagem \n')
                log.write('\n' + str(e.args))
            
            print("Erro ao escrever no campo e enviar a mensagem  (InstagramBot>send_message)", file=sys.stderr)
            return
        self.cont_messagesSent+=1

       
    def run(self, column:str='Instagram', file_csv:str=''):
        try:
            df = pd.read_csv(file_csv)
            instagram_urls = df[df[column].str.contains('(https?://)?(www\.)?instagram\.com', na=False)][column].tolist()

        except Exception as e:
            with open(self.log, 'a') as log:
                now = datetime.datetime.now()
                hour = now.strftime("%d/%m/%Y %H:%M")    
                log.write('\n\n\n\t\t' + hour + '\tInstagramBot>run')
                log.write('\nErro ao ler coluna/arquivo \n')
                log.write('\n' + str(e.args))
            
            print("Erro, verifique se o caminho e a coluna foi digitada corretamente", file=sys.stderr)
            return
        
        print('Enviando mensagens para {} instagram, aguarde...\n'.format(len(instagram_urls)))
        
        for url in instagram_urls:
            self.send_message(url)
        self.driver.quit()
        print(str(self.cont_messagesSent) + ' enviadas de ' + str(len(instagram_urls))) #, end='\n',flush=True

if __name__ == '__main__':
    bot = InstagramBot()
    bot.run()