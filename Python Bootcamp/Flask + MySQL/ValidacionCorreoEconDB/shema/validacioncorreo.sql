-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema validacion_correo
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `validacion_correo` ;

-- -----------------------------------------------------
-- Schema validacion_correo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `validacion_correo` DEFAULT CHARACTER SET utf8 ;
USE `validacion_correo` ;

-- -----------------------------------------------------
-- Table `validacion_correo`.`Emails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `validacion_correo`.`Emails` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
