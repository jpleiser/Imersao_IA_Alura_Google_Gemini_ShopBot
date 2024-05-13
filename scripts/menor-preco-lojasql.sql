SELECT 
        loja_produto_preco.loja_codigo,
        loja_produto_preco.produto_codigo,
        loja_produto_preco.preco
FROM 
        loja_produto_preco
        INNER JOIN (
                SELECT 
                        loja_produto_preco.loja_codigo,
                        loja_produto_preco.produto_codigo,
                        min(loja_produto_preco.preco) AS preco
                FROM 
                        loja_produto_preco
                
        ) AS preco 
        ON 
            loja_produto_preco.loja_codigo = preco.loja_codigo
            AND
            loja_produto_preco.
            AND
            loja_produto_preco.

SELECT 
    loja.nome as Loja,
    loja.endereco as Endereco,
    loja.cidade as Cidade,
    loja.estado as Estado,
    produto.descricao as Produto,
    produto.categoria as Categoria,
    loja_produto_preco.preco as preco
FROM loja_produto_preco
    INNER JOIN (
        SELECT 
                menor_preco.produto_codigo,
                min(menor_preco.preco) AS preco
        FROM 
                loja_produto_preco AS menor_preco
        GROUP BY
                menor_preco.produto_codigo
    ) AS menor_preco
    ON 
        loja_produto_preco.produto_codigo = menor_preco.produto_codigo
        AND
        loja_produto_preco.preco = menor_preco.preco
    INNER JOIN loja 
        ON loja_produto_preco.loja_codigo = loja.codigo  
    INNER JOIN produto 
        ON loja_produto_preco.produto_codigo = produto.codigo  
WHERE  
    (
        Produto like 'arroz' 
        OR
        Produto like 'feijão'
        OR 
        Produto like 'papel higiênico'
    )












