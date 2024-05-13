CREATE TABLE loja (
  codigo INTEGER PRIMARY KEY,
  nome TEXT,
  endereco TEXT,
  cidade TEXT,
  estado TEXT
);

CREATE TABLE produto (
  codigo INTEGER PRIMARY KEY,
  descricao TEXT,
  categoria TEXT,
  unidade_medida TEXT
);

CREATE TABLE loja_produto_preco (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  loja_codigo INTEGER,
  produto_codigo INTEGER,
  preco REAL,
  FOREIGN KEY (loja_codigo) REFERENCES loja(codigo),
  FOREIGN KEY (produto_codigo) REFERENCES produto(codigo)
);

CREATE TABLE lista_compras (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  quantidade DECIMAL(10,4),
  preco_unitario REAL,
  valor_compra REAL,
  data_compra DATE,
  loja_produto_preco_loja_codigo INTEGER,
  loja_produto_preco_produto_codigo INTEGER,
  FOREIGN KEY (loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) REFERENCES loja_produto_preco(loja_codigo, produto_codigo)
);

INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (1, 'Atacadão', 'Avenida Brasil, 123', 'São Paulo');
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (2, 'Assaí Atacadista', 'Avenida Paulista, 101112', 'São Paulo');
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (3, 'Makro', 'Rua da Consolação, 131415', 'São Paulo');
INSERT INTO loja (codigo, nome, endereco, cidade) VALUES (4, 'Roldão Atacadista', 'Rua Augusta, 192021', 'São Paulo');

INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (1, 'Arroz', 'Grãos', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (2, 'Feijão', 'Grãos', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (3, 'Óleo de Soja', 'Óleos e Gorduras', 'L');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (4, 'Açúcar', 'Outros', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (5, 'Sal', 'Outros', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (6, 'Café', 'Bebidas', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (7, 'Macarrão', 'Massas', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (8, 'Farinha de Trigo', 'Farinhas', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (9, 'Leite', 'Laticínios', 'L');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (10, 'Manteiga', 'Laticínios', 'g');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (11, 'Pão Francês', 'Pães', 'un');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (12, 'Carne', 'Carnes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (13, 'Frango', 'Aves', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (14, 'Ovos', 'Outros', 'dz');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (15, 'Tomate', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (16, 'Cebola', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (17, 'Batata', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (18, 'Cenoura', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (19, 'Banana', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (20, 'Maçã', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (21, 'Laranja', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (22, 'Alface', 'Frutas e Legumes', 'un');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (23, 'Couve', 'Frutas e Legumes', 'kg');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (24, 'Extrato de Tomate', 'Enlatados', 'Lata');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (25, 'Milho em Conserva', 'Enlatados', 'Lata');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (26, 'Sardinha em Lata', 'Enlatados', 'Lata');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (27, 'Papel Higiênico', 'Higiene', 'un');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (28, 'Sabonete', 'Higiene', 'un');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (29, 'Creme Dental', 'Higiene', 'un');
INSERT INTO produto (codigo, descricao, categoria, unidade_medida) VALUES (30, 'Detergente', 'Limpeza', 'L');

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

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) 
VALUES 
    (2,24.9,49.8,'2024-05-11',2,1),
    (4,8.5,34,'2024-05-11',2,2),
    (1,11.98,11.98,'2024-05-11',2,3),
    (3,4.39,13.17,'2024-05-11',2,9),
    (2,7.75,15.5,'2024-05-11',2,10)
    ,(3,11.8,35.4,'2024-05-11',2,11),
    (4,3.85,15.4,'2024-05-11',2,17),
    (1,8.2,8.2,'2024-05-11',2,30); 

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) 
VALUES 
    (3,24.402,73.206,'2024-02-11',2,1),
    (2,8.33,16.66,'2024-02-11',2,2),
    (4,11.7604,47.0416,'2024-02-11',2,3),
    (1,4.2922,4.2922,'2024-02-11',2,9),
    (3,7.5725,22.7175,'2024-02-11',2,10),
    (2,11.564,23.128,'2024-02-11',2,11),
    (4,3.7615,15.046,'2024-02-11',2,17),
    (2,8.036,16.072,'2024-02-11',2,30);

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) 
VALUES 
  (1,23.90596,23.90596,'2023-11-11',2,1),
  (4,8.1632,32.6528,'2023-11-11',2,2),
  (3,11.532796,34.598388,'2023-11-11',2,3),
  (2,4.19436,8.38872,'2023-11-11',2,9),
  (4,7.39025,29.561,'2023-11-11',2,10),
  (1,11.3276,11.3276,'2023-11-11',2,11),
  (3,3.67785,11.03355,'2023-11-11',2,17),
  (3,7.86528,23.59584,'2023-11-11',2,30);

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) 
VALUES 
    (2,23.4108804,46.8217608,'2023-08-11',2,1),
    (3,7.99648,23.98944,'2023-08-11',2,2),
    (1,11.30527804,11.30527804,'2023-08-11',2,3),
    (4,4.096444,16.385776,'2023-08-11',2,9),
    (2,7.208025,14.41605,'2023-08-11',2,10),
    (3,11.09084,33.27252,'2023-08-11',2,11),
    (1,3.594165,3.594165,'2023-08-11',2,17),
    (4,7.694512,30.778048,'2023-08-11',2,30);

INSERT INTO lista_compras (quantidade, preco_unitario, valor_compra, data_compra, loja_produto_preco_loja_codigo, loja_produto_preco_produto_codigo) 
VALUES 
    (4,22.91572119,91.66288476,'2023-05-11',2,1),
    (1,7.830736,7.830736,'2023-05-11',2,2),
    (2,11.07775608,22.15551216,'2023-05-11',2,3),
    (3,3.9985288,11.9955864,'2023-05-11',2,9),
    (3,7.0258025,21.0774075,'2023-05-11',2,10),
    (4,10.854056,43.416224,'2023-05-11',2,11),
    (2,3.5104815,7.020963,'2023-05-11',2,17),
    (1,7.5237456,7.5237456,'2023-05-11',2,30);