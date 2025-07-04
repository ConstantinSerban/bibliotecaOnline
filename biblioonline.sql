-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for biblioonline
CREATE DATABASE IF NOT EXISTS `biblioonline` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `biblioonline`;

-- Dumping structure for table biblioonline.books
CREATE TABLE IF NOT EXISTS `books` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Bid` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `Title` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Author` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Status` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'disp',
  PRIMARY KEY (`Id`) USING BTREE,
  UNIQUE KEY `Bid` (`Bid`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table biblioonline.books_issued
CREATE TABLE IF NOT EXISTS `books_issued` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Bid` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `Issueto` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Bid` (`Bid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table biblioonline.cont
CREATE TABLE IF NOT EXISTS `cont` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `utilizator` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `parola` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tip` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
