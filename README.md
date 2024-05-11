# Projeto desafio Imersão IA utilizando Google Gemini 

## Descrição do projeto

No meu desafio criei uma aplicativo chamado **ShopBot**, que é um chatbot alimentado pela tecnologia de IA Generativa Gemini, projetado para transformar a forma como você faz compras. 
O ShopBot emprega o poder do Processamento de Linguagem Natural para entender e responder às suas consultas de forma inteligente e precisa.

O ShopBot é mais do que apenas um assistente de compras, é o seu guia pessoal para compras inteligentes e econômicas. Aqui estão as principais características deste aplicativo revolucionário:  
   
- **Chatbot avançado**: O ShopBot utiliza a IA Generativa Gemini para interagir com você de maneira natural e intuitiva. Basta perguntar ao ShopBot onde encontrar o melhor preço para um produto, e ele irá fornecer a resposta em segundos.  
   
- **Comparação de preços**: O ShopBot permite que você compare preços de um mesmo produto em várias lojas com facilidade. Não é necessário navegar por vários sites ou lojas físicas; o ShopBot faz todo o trabalho pesado para você.  
   
- **Análise de histórico de compras**: Com o ShopBot, você pode analisar seus padrões de gastos, identificar onde você está gastando mais e encontrar maneiras de economizar. O ShopBot ajuda você a tomar decisões de compra mais informadas e a manter seu orçamento sob controle.  
   
- **Previsão de preços**: O ShopBot monitora as flutuações de preços e pode prever quando é o melhor momento para comprar um produto específico. Isso significa que você pode planejar suas compras de acordo e aproveitar as melhores ofertas.  
   
> **Observação:** O ShopBot é a ferramenta perfeita para qualquer comprador moderno. Seja você um caçador de ofertas experiente ou um comprador casual, o ShopBot fornece as informações e ferramentas que você precisa para fazer compras inteligentes. Experimente o ShopBot e descubra uma maneira totalmente nova de fazer compras!

## Configurando o ambiente para executar o projeto

### intalação do Visual Studio Code
https://code.visualstudio.com/Download

### Intalação do python versão 3.11.9 ou superior:
https://www.get-python.org/downloads/release/python-3119/

#### Criando o ambiente python:
```cmd
python -m venv venv3_11_9
```
### Ativando o ambiente python
```cmd
.\venv3_11_9\Scripts\activate
```

### Desativando o ambiente python
```cmd
.\venv3_11_9\Scripts\deactivate
```

### Instalação dos pacotes
```cmd
pip install -r requirements.txt
```

### Configurando a variável de ambiente para que o app obtenha o token de acesso ao Gemini:
Aqui estão as instruções passo a passo para criar a variável de ambiente nos sistemas operacionais Windows, Linux e macOS:
#### Windows
1. Abra o menu "Iniciar" e pesquise "Variáveis de ambiente". Selecione "Editar as variáveis de ambiente do sistema".
1. Na janela que aparece, clique em "Variáveis de Ambiente...".
1. Na janela "Variáveis de Ambiente", clique em "Novo..." abaixo de "Variáveis de usuário para [seu nome de usuário]".
1. No campo "Nome da variável", insira "GEMINI_TOKEN_KEY".
1. No campo "Valor da variável", insira o valor do seu token.
1. Clique em "OK" e "OK" novamente para salvar as alterações.

#### Linux
1. Abra um terminal.
1. Digite o seguinte comando: echo 'export GEMINI_TOKEN_KEY="seu_token"' >> ~/.bashrc (substitua "seu_token" pelo valor do seu token).
1. Recarregue o arquivo .bashrc com o comando: source ~/.bashrc.

#### macOS
1. Abra um terminal.
1. Digite o seguinte comando: echo 'export GEMINI_TOKEN_KEY="seu_token"' >> ~/.bash_profile (substitua "seu_token" pelo valor do seu token).
1. Recarregue o arquivo .bash_profile com o comando: source ~/.bash_profile.

**Observação**: Por favor, substitua "seu_token" pelo valor do seu token. Note que essas alterações farão com que a variável de ambiente esteja disponível apenas para o usuário atual. Se precisar que esteja disponível para todos os usuários, você precisará ajustar as instruções de acordo.

## 1 Construindo o banco de dados utilizando prompt para ser executado no Google AI Studio
**Observação**: Todas as informações obtidas para popular esta base de dados são dados púbilcos encontrados na internet utilizando a IA Generativa do Google Gemini.

### 1.1 Parâmetros configuração Gemini Studio 
> Modelo: Gemini 1.5 <span style="color:red;">PREVIEW</span> Pro
> temperature: 1
> Safety settings: 
![](./images/Parametros-geracao-comando.png)

### 1.2 Prompt para criação do esquema de dados DER
Você é um especialista em banco de dados SQLite e eu quero que você gere um esquema de banco de dados para que eu possa consultar minhas compras em determinadas lojas e comparar os preços entre elas.

Não inclua nenhum comentário, nem antes e nem depois da geração do esquema, liste somente os comandos DDL.

A seguir, vou informar a estrutura de cada tabela e quero que você gere os comandos para a criação.
**loja:**
>codigo
>nome
>endereco
>cidade
>estado

**produto:**
>codigo 
>descricao
>categoria
>unidade_medida

**preco do produto na loja:**
>preco

**lista de compras:**
>id {número gerado automaticamente pelo banco de dados}
>quantidade tipo de dados numerico com 4 casas decimais
>preco_unitario
>valor_compra
>data_compra
>loja_produto_preco



### Resultado esperado:
```sql
CREATE TABLE loja (
  codigo INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  endereco TEXT,
  cidade TEXT,
  estado TEXT
);

CREATE TABLE produto (
  codigo INTEGER PRIMARY KEY,
  descricao TEXT NOT NULL,
  categoria TEXT,
  unidade_medida TEXT
);

CREATE TABLE preco_do_produto_na_loja (
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  preco REAL NOT NULL,
  PRIMARY KEY (loja_codigo, produto_codigo),
  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);

CREATE TABLE lista_de_compras (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  quantidade DECIMAL(10, 4) NOT NULL,
  preco_unitario REAL NOT NULL,
  valor_compra REAL NOT NULL,
  data_compra DATE NOT NULL,
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);
```

### 1.3  Prompt para geração da descrição do projeto ShopBot.
Você é um especialista em marketing de produto e eu gostaria que você gerasse uma descrição para este projeto, destacando as possibilidades de uso para este tipo de aplicação. Ela será utilizada por consumidores para realizar pesquisas de preços, comparando os valores dos produtos entre diferentes lojas. Além disso, o usuário também poderá comparar o histórico de suas compras para acompanhar a variação de preço a partir das compras realizadas nas lojas. O nome do projeto é Shopbot.

### 1.4 Resultado obtido, pode variar dependendo a temperatura ou do modelo selecionado para descrever o projeto.

**Abrace o poder da compra inteligente com Shopbot!**
Cansado de ficar pulando de loja em loja para encontrar o melhor preço? Diga olá ao **Shopbot**, o seu novo aliado para compras inteligentes e econômicas!

**Shopbot** é um aplicativo inovador que coloca você no controle do seu orçamento. Com ele, você pode:

- **Desvendar as melhores ofertas:** Compare preços de um mesmo produto em diversas lojas com apenas alguns toques. Encontre a pechincha perfeita sem precisar sair de casa!

- **Mergulhe no seu histórico de compras:** Analise seus hábitos de consumo e identifique áreas onde você pode economizar. Descubra onde você costuma gastar mais e ajuste suas compras futuras de forma inteligente.

- **Domine a arte da previsão de preços:** Monitore as flutuações de preços ao longo do tempo e antecipe as melhores épocas para comprar. Seja um mestre da pechincha e faça seu dinheiro render mais!
   
**Shopbot** é a ferramenta essencial para compradores modernos que valorizam seu tempo e dinheiro. Seja você um caçador de ofertas experiente ou um comprador casual, o Shopbot te equipa com as informações e ferramentas necessárias para tomar decisões de compra inteligentes e fazer seu dinheiro valer a pena.
Junte-se à revolução das compras inteligentes com Shopbot!


### 1.5 Prompt para gerando dados para popular o banco de dados tabela loja.
Liste os 4 maiores atacadistas existentes no Brasil, incluindo 1 lojas para cada atacadista. Os dados você pode encontrar em sua base de conhecimento na internet.

Não inclua nenhuma explicação adicional, nem antes e nem depois. Quero que liste somente os comandos SQL para que eu possa utilizar posteriormente no sistema ShopBot.

Gere comandos de inclusão de dados na sintaxe SQL-Lite para incluir os registros na tabela 'loja', preenchendo os seguintes campos:

>codigo INTEGER PRIMARY KEY {Gere uma numeração sequencial para este campo}
nome TEXT
endereco TEXT
cidade TEXT
estado TEXT

### 1.6 Resultado gerado
```sql
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (1, 'Atacadão', 'Avenida Brasil, 123', 'São Paulo');
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (2, 'Assaí Atacadista', 'Avenida Paulista, 101112', 'São Paulo');
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (3, 'Makro', 'Rua da Consolação, 131415', 'São Paulo');
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (4, 'Roldão Atacadista', 'Rua Augusta, 192021', 'São Paulo');
```

### 1.7 Prompt para geração de dados para popular o banco de dados tabela produto.
gere uma memoria de 30 produtos da cesta básica. Os dados você pode encontrar em sua base de conhecimento na internet. Liste os produtos incluindo os seguintes campos:

>codigo
descricao
categoria
unidade_medida

Quero que use a memoria de produtos da cesta básica e gere comandos sql-lite para eu incluir estes dados em uma tabela com o nome "produto" que irei utilizar posteriormente no banco de dados do ShopBot.

Não é necessário incluir o comando DDL para criação da tabela

Quero que liste somente os comandos SQL sem nenhuma explicação adiconal, nem antes e nem depois.

Abaixo está a estrutura da tabela que será utilizada:
> codigo INTEGER PRIMARY KEY {Gere uma numeração sequencial para este campo| 
  codigo INTEGER PRIMARY KEY,
  descricao TEXT,
  categoria TEXT,
  unidade_medida TEXT

### 1.8 Resultado obtido:
```sql
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (1, 'Arroz', 'Grãos', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (2, 'Feijão', 'Grãos', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (3, 'Óleo de Soja', 'Óleos e Gorduras', 'L');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (4, 'Açúcar', 'Outros', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (5, 'Sal', 'Outros', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (6, 'Café', 'Bebidas', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (7, 'Macarrão', 'Massas', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (8, 'Farinha de Trigo', 'Farinhas', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (9, 'Leite', 'Laticínios', 'L');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (10, 'Manteiga', 'Laticínios', 'g');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (11, 'Pão Francês', 'Pães', 'un');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (12, 'Carne', 'Carnes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (13, 'Frango', 'Aves', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (14, 'Ovos', 'Outros', 'dz');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (15, 'Tomate', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (16, 'Cebola', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (17, 'Batata', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (18, 'Cenoura', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (19, 'Banana', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (20, 'Maçã', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (21, 'Laranja', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (22, 'Alface', 'Frutas e Legumes', 'un');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (23, 'Couve', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (24, 'Extrato de Tomate', 'Enlatados', 'Lata');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (25, 'Milho em Conserva', 'Enlatados', 'Lata');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (26, 'Sardinha em Lata', 'Enlatados', 'Lata');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (27, 'Papel Higiênico', 'Higiene', 'un');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (28, 'Sabonete', 'Higiene', 'un');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (29, 'Creme Dental', 'Higiene', 'un');
INSERT INTO produto (codigo, descricao, descricao, categoria, unidade_medida) VALUES (30, 'Detergente', 'Limpeza', 'L');
```

### 1.9 Prompt para geração de dados para popular o banco de dados tabela loja_produto.
Gere uma memoria de preços para 30 produtos para cada atacadista produto relacionados abaixo. O preço você pode gerar de forma aleatória conforme dados existentes na internet. 

Quero que utilize a memória de preços para gerar comandos sql-lite para inserção  dos dados na tabela loja_produto_preco, use a estrutura abaixo para criar os comandos, utilize os codigos do atacadista e o codigo do produto para criar o comando de inserção:
>loja_codigo INTEGER,
produto_codigo INTEGER,
preco REAL,

Você deverá listar todas as combinações entre a tabela de loja versus produto, não inclua nenhum comentário, nem antes e nem depois. 

Liste somente os comandos SQL para eu poder utilizar posteriormente.

#### Aqui está a relação de atacadistas:
|Código|Nome
|-|-
|1	|Atacadão
|2	|Assaí Atacadista
|3	|Makro
|4	|Roldão Atacadista

### Aqui está a relação de produtos:
|Código	|Descrição
|-|-|
|1	|Arroz
|2	|Feijão
|3	|Óleo de Soja
|4	|Açúcar
|5	|Sal
|6	|Café
|7	|Macarrão
|8	|Farinha de Trigo
|9	|Leite
|10	|Manteiga
|11	|Pão Francês
|12	|Carne
|13	|Frango
|14	|Ovos
|15	|Tomate
|16	|Cebola
|17	|Batata
|18	|Cenoura
|19	|Banana
|20	|Maçã
|21	|Laranja
|22	|Alface
|23	|Couve
|24	|Extrato de Tomate
|25	|Milho em Conserva
|26	|Sardinha em Lata
|27	|Papel Higiênico
|28	|Sabonete
|29	|Creme Dental
|30	|Detergente

### 1.10 Resultado obtido:
```sql
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 1, 25.99);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 2, 8.75);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 3, 12.48);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 4, 10.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 5, 2.35);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 6, 14.89);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 7, 3.78);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 8, 5.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 9, 4.59);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 10, 7.98);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 11, 12.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 12, 32.87);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 13, 15.6);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 14, 12.99);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 15, 6.45);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 16, 4.89);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 17, 3.98);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 18, 5.12);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 19, 4.99);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 20, 8.79);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 21, 5.3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 22, 2.89);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 23, 3.48);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 24, 2.99);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 25, 3.87);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 26, 6.75);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 27, 11.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 28, 1.98);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 29, 3.25);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (1, 30, 8.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 1, 24.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 2, 8.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 3, 11.98);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 4, 9.89);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 5, 2.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 6, 14.49);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 7, 3.65);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 8, 4.99);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 9, 4.39);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 10, 7.75);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 11, 11.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 12, 31.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 13, 15.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 14, 12.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 15, 6.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 16, 4.69);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 17, 3.85);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 18, 4.98);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 19, 4.85);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 20, 8.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 21, 5.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 22, 2.75);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 23, 3.35);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 24, 2.89);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 25, 3.75);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 26, 6.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 27, 11.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 28, 1.89);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 29, 3.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (2, 30, 8.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 1, 26.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 2, 8.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 3, 12.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 4, 11.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 5, 2.4);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 6, 15.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 7, 3.85);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 8, 5.3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 9, 4.65);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 10, 8.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 11, 12.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 12, 33.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 13, 15.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 14, 13.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 15, 6.6);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 16, 5.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 17, 4.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 18, 5.3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 19, 5.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 20, 9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 21, 5.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 22, 3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 23, 3.6);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 24, 3.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 25, 4);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 26, 7);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 27, 12.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 28, 2.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 29, 3.4);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (3, 30, 8.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 1, 25.7);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 2, 8.6);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 3, 12.3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 4, 10.7);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 5, 2.3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 6, 14.7);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 7, 3.7);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 8, 5.1);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 9, 4.5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 10, 7.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 11, 12.3);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 12, 32.6);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 13, 15.4);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 14, 12.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 15, 6.4);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 16, 4.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 17, 3.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 18, 5);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 19, 4.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 20, 8.7);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 21, 5.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 22, 2.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 23, 3.4);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 24, 2.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 25, 3.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 26, 6.6);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 27, 11.8);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 28, 1.9);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 29, 3.2);
INSERT INTO loja_produto_preco (loja_codigo, produto_codigo, preco) VALUES (4, 30, 8.4);
```


### 1.11 Prompt para geração de dados para popular o banco de dados tabela lista_compras.
Você é especialista en análise de dados. 

Vou fornecer uma tabela com exemplos de dados e quero utilize estes dados para gerar uma memória considerando o menor preço de cada produto loja:

Agora quero que use esta memória e gere comandos sql-lite de insersões de dados para eu utilizar posteriormente,

Na primeira lista você deverá utilizar como data base da compra a data 2024-05-11, inclua todos os registros em um único comando sql.

Considere incluir na quantidade de produto uma variação de quantidade entre 1 a 4 de e calcule o valor total do produto comprado, multiplicando o preço da lista pela quantidade de produtos comprados.

Gere mais 4 listas de compras com datas anteriores à data do item 1, considere criar datas com 3 meses de diferença. Utilize os mesmos produtos selecionados, mas altere o valor unitário dos produtos, decrescendo 2% para cada nova lista gerada.

Gere um comando sql para cada lista de compras

Gere somente os comandos sql-lite para insersão dos dadism sem nenhum comentário, nem antes nem depois.

tabela lista_compras:
>quantidade DECIMAL(10, 4) NOT NULL,
>preco_unitario REAL NOT NULL,
>valor_compra REAL NOT NULL,
>data_compra DATE NOT NULL,
>loja_codigo INTEGER,
>produto_codigo INTEGER,

Exemplo de dados tabela loja_produto_preco:
|loja_codigo|produto_codigo|preco
|-|-|-
|1	|1	|25.99
|1	|2	|8.75
|1	|3	|12.48
|1	|9	|4.59
|1	|10	|7.98
|1	|11	|12.5
|1	|17	|3.98
|1	|30	|8.5
|2	|1	|24.9
|2	|2	|8.5
|2	|3	|11.98
|2	|9	|4.39
|2	|10	|7.75
|2	|11	|11.8
|2	|17	|3.85
|2	|20	|8.5
|2	|30	|8.2
|3	|1	|26.5
|3	|2	|8.9
|3	|3	|12.8
|3	|9	|4.65
|3	|10	|8.1
|3	|11	|12.8
|3	|17	|4.1
|3	|20	|9
|3	|30	|8.8
|4	|1	|25.7
|4	|2	|8.6
|4	|3	|12.3
|4	|9	|4.5
|4	|10	|7.9
|4	|11	|12.3
|4	|17	|3.9
|4	|20	|8.7
|4	|30	|8.4

### 1.12 Resultado obtido.
```sql
INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_codigo, produto_codigo) 
VALUES 
    (2,24.9,49.8,'2024-05-11',2,1),
    (4,8.5,34,'2024-05-11',2,2),
    (1,11.98,11.98,'2024-05-11',2,3),
    (3,4.39,13.17,'2024-05-11',2,9),
    (2,7.75,15.5,'2024-05-11',2,10)
    ,(3,11.8,35.4,'2024-05-11',2,11),
    (4,3.85,15.4,'2024-05-11',2,17),
    (1,8.2,8.2,'2024-05-11',2,30); 

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_codigo, produto_codigo) 
VALUES 
    (3,24.402,73.206,'2024-02-11',2,1),
    (2,8.33,16.66,'2024-02-11',2,2),
    (4,11.7604,47.0416,'2024-02-11',2,3),
    (1,4.2922,4.2922,'2024-02-11',2,9),
    (3,7.5725,22.7175,'2024-02-11',2,10),
    (2,11.564,23.128,'2024-02-11',2,11),
    (4,3.7615,15.046,'2024-02-11',2,17),
    (2,8.036,16.072,'2024-02-11',2,30);

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_codigo, produto_codigo) 
VALUES 
  (1,23.90596,23.90596,'2023-11-11',2,1),
  (4,8.1632,32.6528,'2023-11-11',2,2),
  (3,11.532796,34.598388,'2023-11-11',2,3),
  (2,4.19436,8.38872,'2023-11-11',2,9),
  (4,7.39025,29.561,'2023-11-11',2,10),
  (1,11.3276,11.3276,'2023-11-11',2,11),
  (3,3.67785,11.03355,'2023-11-11',2,17),
  (3,7.86528,23.59584,'2023-11-11',2,30);

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_codigo, produto_codigo) 
VALUES 
    (2,23.4108804,46.8217608,'2023-08-11',2,1),
    (3,7.99648,23.98944,'2023-08-11',2,2),
    (1,11.30527804,11.30527804,'2023-08-11',2,3),
    (4,4.096444,16.385776,'2023-08-11',2,9),
    (2,7.208025,14.41605,'2023-08-11',2,10),
    (3,11.09084,33.27252,'2023-08-11',2,11),
    (1,3.594165,3.594165,'2023-08-11',2,17),
    (4,7.694512,30.778048,'2023-08-11',2,30);

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_codigo, produto_codigo) 
VALUES 
    (4,22.91572119,91.66288476,'2023-05-11',2,1),
    (1,7.830736,7.830736,'2023-05-11',2,2),
    (2,11.07775608,22.15551216,'2023-05-11',2,3),
    (3,3.9985288,11.9955864,'2023-05-11',2,9),
    (3,7.0258025,21.0774075,'2023-05-11',2,10),
    (4,10.854056,43.416224,'2023-05-11',2,11),
    (2,3.5104815,7.020963,'2023-05-11',2,17),
    (1,7.5237456,7.5237456,'2023-05-11',2,30);
```

### 1.13 Prompt principal utilizado pelo ShopBot:
Você é um assistente pessoal atencioso especializado em banco de dados relacional com profundamente conhecimento em PNL. 

Como assistente pessoal, você deverá retornar a estrutura do exemplo 1.
Exemplo 1:
```json  
{
     "question": "question name",  
     "response": "response name"  
}  
```


Como especialista em banco de dados relacional você deverá analisar o esquema de dados definido abaixo e gerar comandos SQL para executar consultas no banco de dados e deverá retornar a estrutura de exemplo 2:
&Exemplo 2:
```json   
{  
     "intent": "SQL",  
     "question": "question name",  
     "response": "response name",  
     "query": "command sql"  
}
```
```sql
CREATE TABLE loja (
  codigo INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  endereco TEXT,
  cidade TEXT,
  estado TEXT
);

CREATE TABLE produto (
  codigo INTEGER PRIMARY KEY,
  descricao TEXT NOT NULL,
  categoria TEXT,
  unidade_medida TEXT
);

CREATE TABLE preco_do_produto_na_loja (
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  preco REAL NOT NULL,
  PRIMARY KEY (loja_codigo, produto_codigo),
  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);

CREATE TABLE lista_de_compras (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  quantidade DECIMAL(10, 4) NOT NULL,
  preco_unitario REAL NOT NULL,
  valor_compra REAL NOT NULL,
  data_compra DATE NOT NULL,
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);
````

### 1.14 Prompt instrução do sistema.

Você é um assistente pessoal atencioso especializado em banco de dados relacional com profundamente conhecimento em PNL.

- Como assistente pessoal, você deverá retornar a estrutura do exemplo 1.
**Exemplo 1:** 
```json  
{
    "question": "question name",
    "response\": "response name" 
}  
```

- Como especialista em banco de dados relacional você deverá analisar o esquema de dados definido abaixo e gerar comandos SQL para executar consultas no banco de dados e deverá retornar a estrutura de exemplo 2:
**&Exemplo 2:**
```json
{
    "intent": "SQL",
    "question": "question name",
    "response": "response name", 
    "query": "command sql"
}
```

- **Esquema de dados**
```json   
{  
     "intent": "SQL",  
     "question": "question name",  
     "response": "response name",  
     "query": "command sql"  
}
```
```sql
CREATE TABLE loja (
  codigo INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  endereco TEXT,
  cidade TEXT,
  estado TEXT
);

CREATE TABLE produto (
  codigo INTEGER PRIMARY KEY,
  descricao TEXT NOT NULL,
  categoria TEXT,
  unidade_medida TEXT
);

CREATE TABLE preco_do_produto_na_loja (
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  preco REAL NOT NULL,
  PRIMARY KEY (loja_codigo, produto_codigo),
  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);

CREATE TABLE lista_de_compras (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  quantidade DECIMAL(10, 4) NOT NULL,
  preco_unitario REAL NOT NULL,
  valor_compra REAL NOT NULL,
  data_compra DATE NOT NULL,
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  FOREIGN KEY (loja_codigo) REFERENCES loja (codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto (codigo)
);
````

### 1.15 Prompt de Aperfeiçoamento para Implementação do RAG.
