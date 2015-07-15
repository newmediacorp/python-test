-- MySQL dump 10.13  Distrib 5.5.24, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: pythontest
-- ------------------------------------------------------
-- Server version	5.5.24-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(2,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(3,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(4,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(5,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(6,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(7,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(8,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(9,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(10,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(11,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(12,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(13,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(14,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(15,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(16,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(17,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(18,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(19,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(20,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(21,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(22,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(23,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(24,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(25,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(26,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(27,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(28,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(29,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(30,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(31,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(32,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(33,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(34,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(35,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(36,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(37,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(38,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(39,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(40,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(41,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(42,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(43,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(44,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(45,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(46,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(47,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(48,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(49,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(50,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(51,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(52,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan'),(53,'Goren','AngelKovski','38971371213','info@newmediacorp.com','Bitola, Fyro','Macedonia'),(54,'Nawazish','Qadir','923314133340','nawazish@gmail.com','Dera Ghazi Khan','Pakistan');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL DEFAULT '0',
  `product_id` int(11) NOT NULL DEFAULT '0',
  `quantity` int(11) DEFAULT NULL,
  `price` float(11,2) DEFAULT NULL,
  PRIMARY KEY (`customer_id`,`product_id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,1,25,35.55),(2,1,2,12,45.00);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `price` float(11,2) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(2,'Synology Storage',25.00,'Product with storing network attached data.'),(3,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(4,'Synology Storage',25.00,'Product with storing network attached data.'),(5,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(6,'Synology Storage',25.00,'Product with storing network attached data.'),(7,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(8,'Synology Storage',25.00,'Product with storing network attached data.'),(9,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(10,'Synology Storage',25.00,'Product with storing network attached data.'),(11,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(12,'Synology Storage',25.00,'Product with storing network attached data.'),(13,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(14,'Synology Storage',25.00,'Product with storing network attached data.'),(15,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(16,'Synology Storage',25.00,'Product with storing network attached data.'),(17,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(18,'Synology Storage',25.00,'Product with storing network attached data.'),(19,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(20,'Synology Storage',25.00,'Product with storing network attached data.'),(21,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(22,'Synology Storage',25.00,'Product with storing network attached data.'),(23,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(24,'Synology Storage',25.00,'Product with storing network attached data.'),(25,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(26,'Synology Storage',25.00,'Product with storing network attached data.'),(27,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(28,'Synology Storage',25.00,'Product with storing network attached data.'),(29,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(30,'Synology Storage',25.00,'Product with storing network attached data.'),(31,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(32,'Synology Storage',25.00,'Product with storing network attached data.'),(33,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(34,'Synology Storage',25.00,'Product with storing network attached data.'),(35,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(36,'Synology Storage',25.00,'Product with storing network attached data.'),(37,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(38,'Synology Storage',25.00,'Product with storing network attached data.'),(39,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(40,'Synology Storage',25.00,'Product with storing network attached data.'),(41,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(42,'Synology Storage',25.00,'Product with storing network attached data.'),(43,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(44,'Synology Storage',25.00,'Product with storing network attached data.'),(45,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(46,'Synology Storage',25.00,'Product with storing network attached data.'),(47,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(48,'Synology Storage',25.00,'Product with storing network attached data.'),(49,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(50,'Synology Storage',25.00,'Product with storing network attached data.'),(51,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(52,'Synology Storage',25.00,'Product with storing network attached data.'),(53,'Facial Skin Care',5.00,'Awesome product to use for facial.'),(54,'Synology Storage',25.00,'Product with storing network attached data.');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-15 14:41:03
