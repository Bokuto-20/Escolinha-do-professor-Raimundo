-- Script SQL para MySQL Workbench (Esquema do Projeto MorfossintaxeApp)
-- Este script contém apenas as tabelas da aplicação 'catalogacao'
-- e foi adaptado do dialeto SQLite para o MySQL para facilitar a Engenharia Reversa.

-- Tabela: catalogacao_periodo
CREATE TABLE IF NOT EXISTS `catalogacao_periodo` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `texto_original` TEXT NOT NULL,
  `tipo_periodo` VARCHAR(10) NOT NULL,
  `data_criacao` DATETIME NOT NULL
);

-- Tabela: catalogacao_oracao
CREATE TABLE IF NOT EXISTS `catalogacao_oracao` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `texto_oracao` TEXT NOT NULL,
  `tipo_oracao` VARCHAR(50) NOT NULL,
  `oracao_principal_id` INT NULL,
  `periodo_id` INT NOT NULL,
  
  -- Chaves Estrangeiras
  FOREIGN KEY (`oracao_principal_id`) REFERENCES `catalogacao_oracao` (`id`),
  FOREIGN KEY (`periodo_id`) REFERENCES `catalogacao_periodo` (`id`)
);

-- Tabela: catalogacao_componentesintatico
CREATE TABLE IF NOT EXISTS `catalogacao_componentesintatico` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `tipo_componente` VARCHAR(10) NOT NULL,
  `texto_componente` TEXT NOT NULL,
  `classificacao` VARCHAR(50) NULL,
  `oracao_id` INT NOT NULL,
  
  -- Chave Estrangeira
  FOREIGN KEY (`oracao_id`) REFERENCES `catalogacao_oracao` (`id`),
  
  -- Restrição de Unicidade (Adaptada do Django)
  UNIQUE KEY `oracao_id_tipo_componente_uniq` (`oracao_id`, `tipo_componente`)
);

-- Índices (Opcional, mas recomendado para performance)
CREATE INDEX `catalogacao_oracao_periodo_id_idx` ON `catalogacao_oracao` (`periodo_id`);
CREATE INDEX `catalogacao_oracao_oracao_principal_id_idx` ON `catalogacao_oracao` (`oracao_principal_id`);
CREATE INDEX `catalogacao_componentesintatico_oracao_id_idx` ON `catalogacao_componentesintatico` (`oracao_id`);
