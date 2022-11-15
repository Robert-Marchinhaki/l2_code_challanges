use mydb;

CREATE TABLE contratos (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    valor_parcela INT NOT NULL,
    parcelas INT NOT NULL
);

CREATE TABLE pessoas (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    contrato_id INT NOT NULL,
    inadimplente VARCHAR(1) NOT NULL,
    dt_completo VARCHAR(10) DEFAULT(Null),
    FOREIGN KEY (contrato_id) REFERENCES contratos(id)
);

CREATE TABLE pagamentos (
	id INT NOT NULL AUTO_INCREMENT,
    pessoa_id INT NOT NULL,
    dt_pagamento DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
);