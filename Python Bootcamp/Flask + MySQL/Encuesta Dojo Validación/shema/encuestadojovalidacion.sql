-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_encuesta_dojo
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_encuesta_dojo` ;

-- -----------------------------------------------------
-- Schema esquema_encuesta_dojo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_encuesta_dojo` DEFAULT CHARACTER SET utf8 ;
USE `esquema_encuesta_dojo` ;

-- -----------------------------------------------------
-- Table `esquema_encuesta_dojo`.`encuestas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_encuesta_dojo`.`encuestas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `ubicacion` VARCHAR(45) NULL,
  `lenguaje` VARCHAR(45) NULL,
  `comentarios` VARCHAR(255) NULL,
  `updated_at` VARCHAR(45) NULL DEFAULT 'NOW()',
  `created_at` VARCHAR(45) NULL DEFAULT 'NOW()',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
