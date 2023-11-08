-- --------------------------------------------------------
-- Host:                         127.0.0.2
-- Versión del servidor:         8.0.34 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


/* Base de datos de la Miselanía 
Miguel Angel Bonilla Torres
Juan Pablo Gomez 
Juan  Sebastian Fandiño   */

-- Volcando estructura de base de datos para micelania
CREATE DATABASE IF NOT EXISTS `micelania` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `micelania`;

-- Volcando estructura para tabla micelania.caja
CREATE TABLE IF NOT EXISTS `caja` (
  `idCaja` int NOT NULL,
  `Factura_IdFactura` int NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`idCaja`,`Factura_IdFactura`),
  KEY `fk_Caja_Factura1_idx` (`Factura_IdFactura`),
  CONSTRAINT `fk_Caja_Factura1` FOREIGN KEY (`Factura_IdFactura`) REFERENCES `factura` (`IdFactura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.caja: ~3 rows (aproximadamente)
REPLACE INTO `caja` (`idCaja`, `Factura_IdFactura`, `Fecha`) VALUES
	(1, 100, '2023-09-16'),
	(2, 101, '2023-09-16'),
	(3, 102, '2023-09-16');

-- Volcando estructura para tabla micelania.factura
CREATE TABLE IF NOT EXISTS `factura` (
  `IdFactura` int NOT NULL,
  `Productos` varchar(45) NOT NULL,
  `IdPersonal` int NOT NULL DEFAULT '0',
  `Cantidad Comprada` varchar(45) NOT NULL,
  `IdPersonaCLI` int NOT NULL,
  `Pedido_idPedido` int NOT NULL,
  `Productos_idProductos` int NOT NULL,
  PRIMARY KEY (`IdFactura`,`Productos_idProductos`),
  KEY `fk_Factura_Pedido1_idx` (`Pedido_idPedido`),
  KEY `fk_Factura_Productos1_idx` (`Productos_idProductos`) USING BTREE,
  KEY `fk_Factura_Persona2` (`IdPersonaCLI`),
  KEY `fk_Factura_Persona1` (`IdPersonal`) USING BTREE,
  CONSTRAINT `fk_Factura_Pedido1` FOREIGN KEY (`Pedido_idPedido`) REFERENCES `pedido` (`idPedido`),
  CONSTRAINT `fk_Factura_Persona1` FOREIGN KEY (`IdPersonal`) REFERENCES `persona` (`IdPersona`),
  CONSTRAINT `fk_Factura_Persona2` FOREIGN KEY (`IdPersonaCLI`) REFERENCES `persona` (`IdPersona`),
  CONSTRAINT `fk_Factura_Productos1` FOREIGN KEY (`Productos_idProductos`) REFERENCES `productos` (`idProductos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.factura: ~3 rows (aproximadamente)
REPLACE INTO `factura` (`IdFactura`, `Productos`, `IdPersonal`, `Cantidad Comprada`, `IdPersonaCLI`, `Pedido_idPedido`, `Productos_idProductos`) VALUES
	(100, 'Esfero negro', 570, '1', 691, 1, 310),
	(101, 'Caja de colores x30', 570, '1', 691, 2, 320),
	(102, 'Esfero azul', 570, '1', 691, 3, 360);

-- Volcando estructura para tabla micelania.pedido
CREATE TABLE IF NOT EXISTS `pedido` (
  `idPedido` int NOT NULL,
  `Persona_IdPersona` int NOT NULL,
  `Productos_idProductos` int NOT NULL,
  `Precio Total` int NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`idPedido`),
  KEY `fk_Pedido_Productos1_idx` (`Productos_idProductos`),
  KEY `fk_Pedido_Persona1_idx` (`Persona_IdPersona`),
  CONSTRAINT `fk_Pedido_Persona1` FOREIGN KEY (`Persona_IdPersona`) REFERENCES `persona` (`IdPersona`),
  CONSTRAINT `fk_Pedido_Productos1` FOREIGN KEY (`Productos_idProductos`) REFERENCES `productos` (`idProductos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.pedido: ~10 rows (aproximadamente)
REPLACE INTO `pedido` (`idPedido`, `Persona_IdPersona`, `Productos_idProductos`, `Precio Total`, `Fecha`) VALUES
	(1, 691, 310, 1000, '2023-09-16'),
	(2, 691, 320, 30000, '2023-09-16'),
	(3, 617, 360, 1000, '2023-09-16'),
	(4, 739, 330, 120000, '2023-09-19'),
	(5, 739, 380, 135000, '2023-09-19'),
	(6, 721, 440, 3500, '2023-09-10'),
	(7, 721, 350, 30000, '2023-09-10'),
	(8, 625, 350, 30000, '2023-09-05'),
	(9, 625, 410, 100000, '2023-09-05'),
	(10, 625, 350, 30000, '2023-09-01');

-- Volcando estructura para tabla micelania.persona
CREATE TABLE IF NOT EXISTS `persona` (
  `IdPersona` int NOT NULL,
  `TipoPersona` int NOT NULL,
  `Tipo de Documento` varchar(4) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Ciudad` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`IdPersona`),
  KEY `fk_Persona_TipoPersona_idx` (`TipoPersona`),
  CONSTRAINT `fk_Persona_TipoPersona` FOREIGN KEY (`TipoPersona`) REFERENCES `tipopersona` (`IdPersona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.persona: ~24 rows (aproximadamente)
REPLACE INTO `persona` (`IdPersona`, `TipoPersona`, `Tipo de Documento`, `Nombre`, `Telefono`, `Ciudad`, `Direccion`, `Email`) VALUES
	(524, 2, 'CC', 'Carmen Ruiz', '3202677046', 'Bogotá', 'Avenida 33 # 56-12', 'carmenruiz@outlook_es'),
	(540, 1, 'CC', 'Ana Martínez', '3193562651', 'Bogotá', 'Calle 89 # 34-12', 'anamartinez@gmail_com'),
	(570, 2, 'CC', 'Paula Jiménez', '3200257960', 'Bogotá', 'Avenida 56 # 34-23', 'paulajimenez@outlook_es'),
	(585, 3, 'NIT', 'Faber Castell', '3179767744', 'Medellín', 'Calle 34 # 12-45', 'fabercastell@gmail_com'),
	(617, 1, 'CC', 'Elena Ramírez', '3184028537', 'Bogotá', 'Calle 56A # 34-23', 'elenaramirez@outlook_es'),
	(625, 1, 'CC', 'Juan García', '3198525499', 'Bogotá', 'Calle 123 # 45-67', 'juangarcia@gmail_com'),
	(628, 3, 'NIT', 'Pelikan', '3201369509', 'Medellín', 'Carrera 67 # 12-23', 'pelikan@outlook_es'),
	(660, 3, 'CC', 'Norma', '3183598683', 'Barranquilla', 'Carrera 90 # 23-56', 'norma@outlook_es'),
	(662, 2, 'CC', 'Laura González', '3189728766', 'Bogotá', 'Calle 56 # 9-87', 'lauragonzalez@gmail_com'),
	(664, 2, 'CC', 'Francisco Vargas', '3201700926', 'Bogotá', 'Avenida 12 # 56-34', 'franciscovargas@gmail_com'),
	(666, 2, 'CC', 'Clara Castro', '3169261464', 'Bogotá', 'Carrera 23 # 45-7', 'claracastro@outlook_es'),
	(675, 1, 'CC', 'Luis Pérez', '3189707544', 'Bogotá', 'Carrera 22 # 78-90', 'luisperez@gmail_com'),
	(679, 1, 'CC', 'Jorge Morales', '3183415898', 'Bogotá', 'Carrera 78 # 45-67', 'jorgemorales@outlook_es'),
	(680, 1, 'CC', 'Manuel Ortiz', '3170934241', 'Bogotá', 'Carrera 34 # 90-23', 'manuelortiz@gmail_com'),
	(691, 1, 'CC', 'Sofia Castro', '3192080091', 'Bogotá', 'Calle 45 # 12-34', 'sofiacastro@gmail_com'),
	(695, 2, 'CC', 'Carlos Sánchez', '3199957388', 'Bogotá', 'Avenida 34 # 67-23', 'carlossanchez@outlook_es'),
	(699, 2, 'CC', 'Javier Silva', '3174916708', 'Bogotá', 'Calle 78 # 67-12', 'javiersilva@gmail_com'),
	(721, 1, 'CC', 'María Rodríguez', '3198400891', 'Bogotá', 'Carrera 56A # 12-3', 'mariarodriguez@gmail_com'),
	(723, 3, 'CC', 'Offi-Ecco', '3204316535', 'Cartagena', 'Calle 23 # 56-78', 'offiecco@gmail_com'),
	(734, 2, 'CC', 'Isabel Fernández', '3177206836', 'Bogotá', 'Carrera 12 # 45-78', 'isabelfernandez@outlook_es'),
	(739, 1, 'CC', 'Pedro López', '3202554917', 'Bogotá', 'Avenida 7 # 22-45', 'pedrolopez@gmail_com'),
	(747, 2, 'CC', 'Julia Herrera', '3189763751', 'Bogotá', 'Calle 67 # 23-56', 'juliaherrera@gmail_com'),
	(758, 1, 'CC', 'Antonio Díaz', '3199580828', 'Bogotá', 'Avenida 22 # 67-45', 'antoniodiaz@gmail_com'),
	(775, 2, 'CC', 'Andrés Torres', '3191945715', 'Bogotá', 'Calle 90 # 23-56', 'andrestorres@outlook_es');

-- Volcando estructura para tabla micelania.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `idProductos` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Precio` decimal(50,0) NOT NULL,
  `Stock_idStock` int NOT NULL,
  `Unidad` int NOT NULL,
  PRIMARY KEY (`idProductos`,`Stock_idStock`),
  KEY `fk_Productos_Stock1_idx` (`Stock_idStock`),
  CONSTRAINT `fk_Productos_Stock1` FOREIGN KEY (`Stock_idStock`) REFERENCES `stock` (`idStock`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.productos: ~15 rows (aproximadamente)
REPLACE INTO `productos` (`idProductos`, `Nombre`, `Precio`, `Stock_idStock`, `Unidad`) VALUES
	(310, 'Esfero Negro', 1000, 1, 1),
	(320, 'Caja de colores x30', 30000, 2, 1),
	(330, 'Calculadora cientifica FX-380 plus', 120000, 3, 1),
	(340, 'Esfero Negro', 1000, 4, 1),
	(350, 'Caja de colores x30', 30000, 5, 1),
	(360, 'Esfero azul', 1000, 6, 1),
	(370, 'Esfero rojo', 1000, 7, 1),
	(380, 'Calculadora cientifica FX-380', 135000, 8, 1),
	(390, 'Pintura Arcrilica x5', 35000, 9, 2),
	(400, 'Calculadora cientifica FX-750 plus', 135000, 10, 1),
	(410, 'Calculadora oficina HT-320', 100000, 11, 1),
	(420, 'Bloc de hojas x 50', 150000, 12, 1),
	(430, 'Carpeta lejadora x 5', 8500, 13, 1),
	(440, 'Temperas', 3500, 14, 3),
	(450, 'Pinceles x 3', 9500, 15, 3);

-- Volcando estructura para tabla micelania.stock
CREATE TABLE IF NOT EXISTS `stock` (
  `idStock` int NOT NULL,
  `Proveedor_IdPersona` int NOT NULL,
  `Producto` varchar(45) NOT NULL,
  `Stock` int NOT NULL,
  PRIMARY KEY (`idStock`,`Proveedor_IdPersona`),
  KEY `fk_Stock_Persona1_idx` (`Proveedor_IdPersona`),
  CONSTRAINT `fk_Stock_Persona1` FOREIGN KEY (`Proveedor_IdPersona`) REFERENCES `persona` (`IdPersona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.stock: ~15 rows (aproximadamente)
REPLACE INTO `stock` (`idStock`, `Proveedor_IdPersona`, `Producto`, `Stock`) VALUES
	(1, 585, 'Esfero Negro', 68),
	(2, 660, 'Caja de colores x30', 73),
	(3, 758, 'Calculadora cientifica FX-380 plus', 64),
	(4, 723, 'Esfero Negro', 71),
	(5, 628, 'Caja de colores x30', 54),
	(6, 585, 'Esfero azul', 75),
	(7, 585, 'Esfero rojo', 61),
	(8, 758, 'Calculadora cientifica FX-380', 78),
	(9, 660, 'Pintura arcrilica x 5', 58),
	(10, 758, 'Calculadora cientifica FX-750 plus', 78),
	(11, 758, 'Calculadora oficina HT-320', 62),
	(12, 723, 'Bloc de hojas x 50', 53),
	(13, 723, 'Carpeta lejadora x 5', 63),
	(14, 628, 'Temperas ', 53),
	(15, 628, 'Pinceles x 3', 79);

-- Volcando estructura para tabla micelania.tipopersona
CREATE TABLE IF NOT EXISTS `tipopersona` (
  `IdPersona` int NOT NULL AUTO_INCREMENT,
  `Tipo` int NOT NULL,
  `Cargo` varchar(45) NOT NULL,
  PRIMARY KEY (`IdPersona`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla micelania.tipopersona: ~3 rows (aproximadamente)
REPLACE INTO `tipopersona` (`IdPersona`, `Tipo`, `Cargo`) VALUES
	(1, 1, 'Cliente'),
	(2, 2, 'Proveedor'),
	(3, 3, 'Empleado');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
