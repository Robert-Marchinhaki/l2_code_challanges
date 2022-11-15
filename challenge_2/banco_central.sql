use mydb;

SELECT * FROM contratos;
SELECT * FROM pessoas;
SELECT * FROM pagamentos;

SELECT p.nome as "NOME", DAY(pg.dt_pagamento) as "DIA_MES", c.valor_parcela as "VALOR_PARCELA"
FROM pessoas p, pagamentos pg, contratos c
WHERE p.inadimplente = "S" and p.contrato_id = c.id and pg.pessoa_id = p.id;

select p.nome as "NOME", c.valor_parcela * c.parcelas as "VALOR_TOTAL" 
FROM pessoas p, pagamentos pg, contratos c
WHERE p.inadimplente = "N" and p.contrato_id = c.id and pg.pessoa_id = p.id;