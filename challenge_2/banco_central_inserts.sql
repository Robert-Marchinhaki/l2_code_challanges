USE mydb;

SELECT * FROM contratos;
INSERT INTO contratos (valor_parcela, parcelas) VALUES (150, 100);
INSERT INTO contratos (valor_parcela, parcelas) VALUES (300, 48);
INSERT INTO contratos (valor_parcela, parcelas) VALUES (550, 24);
INSERT INTO contratos (valor_parcela, parcelas) VALUES (1000, 12);

SELECT * FROM pessoas;
INSERT INTO pessoas (nome, contrato_id, inadimplente, dt_completo) VALUES ("Cristian
Ghyprievy", 2, "S", Null);
INSERT INTO pessoas (nome, contrato_id, inadimplente, dt_completo) VALUES ("Joana Cabel", 1, "S", Null);
INSERT INTO pessoas (nome, contrato_id, inadimplente, dt_completo) VALUES ("John Serial", 3, "S", Null);
INSERT INTO pessoas (nome, contrato_id, inadimplente, dt_completo) VALUES ("Michael Seven", 2, "N", "2021-09-25");

SELECT * FROM pagamentos;
INSERT INTO pagamentos (pessoa_id, dt_pagamento) VALUES (4, "2021-09-01");
INSERT INTO pagamentos (pessoa_id, dt_pagamento) VALUES (3, "2021-09-05");
INSERT INTO pagamentos (pessoa_id, dt_pagamento) VALUES (1, "2021-09-19");
INSERT INTO pagamentos (pessoa_id, dt_pagamento) VALUES (2, "2021-09-25");