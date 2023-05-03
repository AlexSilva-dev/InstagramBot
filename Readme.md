
# Documentação

[GitHub](https://github.com/AlexSilva-dev/InstagramBot)


## Usuário


### Estrutura dos arquivos e pastas (usuário)
- Para usar é necessário entender algumas estruturas de pastas do programa e alguns arquivos.
- Primeiro arquivo mais relevante `main.py`, esse arquivo é o inicio do programa, onde as coisas acontecem, ele é o arquivo que deve ser executado.
- `data_sheet/`, é nela que deve ser armazenado a planilha .csv que contém os sites para capturar instagram, ou até mesmo a própria url do instagram (de forma direta).
- `data/input/` - Nessa pasta vai ter as entradas, no momento só vai ter um arquivo `message.txt`
    - `message.txt` - Nesse arquivo vai ser onde vai ter as mensagens
- `data/output/` - Nessa pasta vamos ter a saída do programa, como os arquivos .csv com a coluna de instagram add, o arquivo `log.txt`, nele vai ter os erros encontrados durante a execução, tanto de páginas que não existem, tanto por erro ou bug no programa, e por fim, alguns prints programado, ao passar do tempo essa pasta pode ficar cheia, então é recomendado uma limpeza, vez ou outra.

### Como usar
- Para usar o programa, basta executar o `main.py` com o seguinte comando:
~~~
python main.py arquivo.csv --login
~~~

1. Para fazer isso no WINDOWS 10 basta ir na pasta dos arquivos da automoção Clicar em Arquivos, ir em "Abrir o Windows PowerShell" > "Abrir o Windows PowerShell como administrador"
    - ![235978507-64ff9616-ca59-4490-a1e0-5ef4aa122afc](https://user-images.githubusercontent.com/89947341/235983074-a9e32e19-d88c-4e40-b074-48e71da20aa7.png)

2. Após abrir o PowerShell, basta executar o comando `python main.py arquivo.csv --login`.
    - ![png](https://user-images.githubusercontent.com/89947341/235984337-e8f9e01d-767f-4a54-847e-4e68db6092df.png)
3. Nesse momento irá pedir para vc digitar o nome da coluna que contém as URLs no arquivo.csv de entrada. É importante que o nome seja identico.
    - Exemplo: se no meu arquivo.csv a coluna que está a URL o nome é; "Sites", vc vai digitar "Sites" no PowerShell e aperta `enter` do teclado.
5. Após essa etapa irá começar a execução do programa, caso tudo ocorreu bem. Como está com o parametro `--login`, irá abrir uma janela no Instagram para fazer o login da conta. Após realizar o login, basta fechar a **Janela** do Chrome, que o programa começará a enviar as mensagens.

#### Observações:
- arquivo.csv se refere a entrada que está dentro da pasta `data_sheet/`
- `--login` é um parametro usado para caso você está executando a primeira vez, para entrar na sua conta no Instagram.
    - Para entrar na conta, o programa abre uma janela do Chrome no site do Instagram, a parti dai vc faz o login na conta que deseja automatizar o envio de mensagem, e quando tiver tudo completo, vc fecha essa janela do Chrome, para o programa identificar que o login foi realizado. Com isso o programa começará a rodar e fazer os envios.


### Instalação:

Para o uso do sistema é necessário instalar as suas dependências, que são:
- Python v3.10.6
- pip v22.0.2
- Chrome v112.0
- Bibliotecas Python:
    - argparse
    - datetime
    - pandas
    - selenium
    - Beautifulsoup4
    - request

#### Instalação do python e pip Win:
- https://www.python.org/downloads/
    - Basta acessar o site e fazer a instalação como qualquer outro programa, acho que nada impede de instalar na versão mais recente, mas o recomendado é instalar a versão correspodente.
        - *IMPORTANTE QUE A OPÇÃO DE ADD PYTHON.exe AO PATH, SEJA ATIVADA NA INSTALAÇÃO*
    - O pip já vem com o Python, para certificar que ele foi intalado, basta abrir o PowerShell ou cmd e digitar o seguinte comando; `pip --version`, se ele retornar o número da versão do pip, está instalado corretamente


#### Instalação do pip e as bibliotecas:
- Para instalação das bibliotecas basta digitar o seguinte comando no PowerShell (abra no modo administrador):
~~~
pip install argparse datetime pandas selenium beautifulsoup4 requests
~~~


## Desenvolvedor:

### Estrutura das pastas e arquivos
- Pasta `modules/` contém as classes usadas no programa.
    - `instagramLinksExtractor.py` - É a classe que extrai os Instagram's pela URL
    - `ìnstagramBot.py` - É a classe que faz login e envia as mensagens de forma automatizada.
