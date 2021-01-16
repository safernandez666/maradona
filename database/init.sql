CREATE DATABASE IF NOT EXISTS `maradona` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE `maradona`;

# Volcado de tabla frases
# -----------------------------------------------------------

DROP TABLE IF EXISTS `frases`;

CREATE TABLE `frases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `frase` varchar(1000) NOT NULL,
  `detalle` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `frases` (`frase`, `detalle`)
VALUES
	('X','X1'),
	('Y','Y1');

UNLOCK TABLES;
