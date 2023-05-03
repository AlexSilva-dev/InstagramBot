
# Documentação




## Usuário

### uso:

#### Estrutura dos arquivos e pastas (usuário)
- Para usar é necessário entender algumas estruturas de pastas do programa e alguns arquivos.
- Primeiro arquivo mais relevante `main.py`, esse arquivo é o inicio do programa, onde as coisas acontecem, ele é o arquivo que deve ser executado.
- `data_sheet/`, é nela que deve ser armazenado a planilha .csv que contém os sites para capturar instagram, ou até mesmo a própria url do instagram (de forma direta).
- `data/input/` - Nessa pasta vai ter as entradas, no momento só vai ter um arquivo `message.txt`
    - `message.txt` - Nesse arquivo vai ser onde vai ter as mensagens
- `data/output/` - Nessa pasta vamos ter a saída do programa, como os arquivos .csv com a coluna de instagram add, o arquivo `log.txt`, nele vai ter os erros encontrados durante a execução, tanto de páginas que não existem, tanto por erro ou bug no programa, e por fim, alguns prints programado, ao passar do tempo essa pasta pode ficar cheia, então é recomendado uma limpeza, vez ou outra.

#### Como usar
- Para usar o programa, basta executar o `main.py` com o seguinte comando:
~~~
python main.py arquivo.csv --login
~~~
- No qual o arquivo.csv se refere a entrada que está dentro da pasta `data_sheet/`
- E `--login` é um parametro usado para caso você está executando a primeira vez, para entrar na sua conta no Instagram.
    - Para entrar na conta, o programa abre uma aba do Chrome no site do Instagram, a parti dai vc faz o login, e quando tiver tudo completo, vc fecha essa janela do Chrome. Com isso o programa começa a rodar.


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
