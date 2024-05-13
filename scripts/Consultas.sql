

Assaí Atacadista	Feijão

select * from produto where descricao = 'Feijão';
select * from loja;
select * from loja_produto_preco where produto_codigo = 2;

BEGIN TRANSACTION;    
update loja_produto_preco
SET
        preco = 30.45
where
        loja_codigo = 2
        and 
        produto_codigo = 2;
COMMIT;

codigo	nome	                endereco	cidade	estado
2	Assaí Atacadista	Avenida Paulista, 101112	São Paulo	NULL
3	Makro	                Rua da Consolação, 131415	São Paulo	NULL
