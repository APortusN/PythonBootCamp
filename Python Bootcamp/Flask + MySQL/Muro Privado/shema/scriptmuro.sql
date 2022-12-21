-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema muro_privado
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `muro_privado` ;

-- -----------------------------------------------------
-- Schema muro_privado
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `muro_privado` DEFAULT CHARACTER SET utf8 ;
USE `muro_privado` ;

-- -----------------------------------------------------
-- Table `muro_privado`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `muro_privado`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `contraseña` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `muro_privado`.`mensajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `muro_privado`.`mensajes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `contenido` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `emisor_id` INT NOT NULL,
  `receptor_id1` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mensajes_usuarios_idx` (`emisor_id` ASC) VISIBLE,
  INDEX `fk_mensajes_usuarios1_idx` (`receptor_id1` ASC) VISIBLE,
  CONSTRAINT `fk_mensajes_usuarios`
    FOREIGN KEY (`emisor_id`)
    REFERENCES `muro_privado`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mensajes_usuarios1`
    FOREIGN KEY (`receptor_id1`)
    REFERENCES `muro_privado`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
