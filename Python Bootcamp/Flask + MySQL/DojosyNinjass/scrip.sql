-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_dojos_y_ninjas2
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_dojos_y_ninjas2` ;

-- -----------------------------------------------------
-- Schema esquema_dojos_y_ninjas2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_dojos_y_ninjas2` DEFAULT CHARACTER SET utf8 ;
USE `esquema_dojos_y_ninjas2` ;

-- -----------------------------------------------------
-- Table `esquema_dojos_y_ninjas2`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_dojos_y_ninjas2`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_dojos_y_ninjas2`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_dojos_y_ninjas2`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `dojo_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `esquema_dojos_y_ninjas2`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
