-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_canciones
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_canciones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_canciones` DEFAULT CHARACTER SET utf8 ;
USE `esquema_canciones` ;

-- -----------------------------------------------------
-- Table `esquema_canciones`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_canciones`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(225) NULL,
  `gmail` VARCHAR(225) NULL,
  `password` VARCHAR(225) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_canciones`.`canciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_canciones`.`canciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(225) NULL,
  `artista` VARCHAR(225) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_canciones`.`favoritos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_canciones`.`favoritos` (
  `usuario_id` INT NOT NULL,
  `cancion_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `cancion_id`),
  INDEX `fk_usuarios_has_canciones_canciones1_idx` (`cancion_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_canciones_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_canciones_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_canciones`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_canciones_canciones1`
    FOREIGN KEY (`cancion_id`)
    REFERENCES `esquema_canciones`.`canciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
