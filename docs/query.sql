-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Role` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Role` (
  `Role_id` INT NOT NULL,
  `name_rol` VARCHAR(45) NULL,
  `Crate_at_time` VARCHAR(45) NULL,
  `update_at_time` VARCHAR(45) NULL,
  PRIMARY KEY (`Role_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`UserUni`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`UserUni` ;

CREATE TABLE IF NOT EXISTS `mydb`.`UserUni` (
  `User_id` INT NOT NULL,
  `name` VARCHAR(60) NULL,
  `email` VARCHAR(60) NULL,
  `Role_Role_id` INT NOT NULL,
  PRIMARY KEY (`User_id`),
  INDEX `fk_User_Role_idx` (`Role_Role_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Carreras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Carreras` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Carreras` (
  `id_carrrera` INT NOT NULL,
  `Cve_Carrera` VARCHAR(200) NULL,
  `Nombre_Carrera` VARCHAR(200) NULL,
  `Duracion` VARCHAR(45) NULL,
  `Requisitos_ad` VARCHAR(200) NULL,
  `Creditos_gradu` VARCHAR(45) NULL,
  PRIMARY KEY (`id_carrrera`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Contacto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Contacto` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Contacto` (
  `id_Contacto` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido_ma` VARCHAR(45) NULL,
  `apellido_pa` VARCHAR(45) NULL,
  `Genero` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `celular` VARCHAR(45) NULL,
  `direcion` VARCHAR(45) NULL,
  `colonia` VARCHAR(45) NULL,
  `Estado` VARCHAR(45) NULL,
  `Municipio` VARCHAR(45) NULL,
  `Fecha_nacimiento` DATETIME NULL,
  `Contactocol` VARCHAR(45) NULL,
  PRIMARY KEY (`id_Contacto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Profesor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Profesor` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Profesor` (
  `Cve_Profesor` VARCHAR(200) NOT NULL,
  `Cve_Dependencia` VARCHAR(200) NULL,
  `User_User_id` INT NOT NULL,
  `Contacto_id_Contacto` INT NOT NULL,
  `Especializacion` VARCHAR(45) NULL,
  `materia_impar` VARCHAR(45) NULL,
  `nivel_acade` VARCHAR(45) NULL,
  `titulo_acade` VARCHAR(45) NULL,
  `fecha_ingreso` DATE NULL,
  PRIMARY KEY (`Cve_Profesor`),
  INDEX `fk_Uni_Profesor_User1_idx` (`User_User_id` ASC),
  INDEX `fk_Uni_Profesor_Contacto1_idx` (`Contacto_id_Contacto` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Grupos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Grupos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Grupos` (
  `Cve_grupo` VARCHAR(200) NOT NULL,
  `Uni_Carreras_id_carrrera` INT NOT NULL,
  `Uni_Profesor_Cve_Profesor` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`Cve_grupo`),
  INDEX `fk_Uni_Grupos_Uni_Carreras1_idx` (`Uni_Carreras_id_carrrera` ASC) ,
  INDEX `fk_Uni_Grupos_Uni_Profesor1_idx` (`Uni_Profesor_Cve_Profesor` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Materias`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Materias` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Materias` (
  `id_materia` VARCHAR(200) NOT NULL,
  `nombre_Materia` VARCHAR(45) NULL,
  `Cred_Materia` VARCHAR(45) NULL,
  `Requisitos_Previos` VARCHAR(45) NULL,
  `Uni_Grupos_Cve_grupo` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id_materia`),
  INDEX `fk_Uni_Materias_Uni_Grupos1_idx` (`Uni_Grupos_Cve_grupo` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Acreditacion_Materia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Acreditacion_Materia` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Acreditacion_Materia` (
  `idi_Acreditacion_Mat` INT NOT NULL,
  `Tipo_de_Acreditacion` VARCHAR(45) NULL,
  `Estado_actual` VARCHAR(45) NULL,
  PRIMARY KEY (`idi_Acreditacion_Mat`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Calficacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Calficacion` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Calficacion` (
  `id_calficacion` INT NOT NULL AUTO_INCREMENT,
  `fecha_evaluacion` DATE NULL,
  `Uni_Materias_id_materia` VARCHAR(200) NOT NULL,
  `Uni_Acreditacion_Materia_idi_Acreditacion_Mat` INT NOT NULL,
  PRIMARY KEY (`id_calficacion`),
  INDEX `fk_Uni_Calficacion_Uni_Materias1_idx` (`Uni_Materias_id_materia` ASC),
  INDEX `fk_Uni_Calficacion_Uni_Acreditacion_Materia1_idx` (`Uni_Acreditacion_Materia_idi_Acreditacion_Mat` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Alumnos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Alumnos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Alumnos` (
  `Matricula` VARCHAR(45) NOT NULL,
  `Esta_Civil` VARCHAR(45) NULL,
  `User_User_id` INT NOT NULL,
  `Contacto_id_Contacto` INT NOT NULL,
  `Uni_Calficacion_id_calficacion` INT NOT NULL,
  PRIMARY KEY (`Matricula`),
  INDEX `fk_Uni_Alumnos_User1_idx` (`User_User_id` ASC) ,
  INDEX `fk_Uni_Alumnos_Contacto1_idx` (`Contacto_id_Contacto` ASC) ,
  INDEX `fk_Uni_Alumnos_Uni_Calficacion1_idx` (`Uni_Calficacion_id_calficacion` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Egresados`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Egresados` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Egresados` (
  `Matricula` INT NOT NULL,
  `id_carrera` INT NULL,
  `año_grad` VARCHAR(45) NULL,
  `Uni_Carreras_id_carrrera` INT NOT NULL,
  PRIMARY KEY (`Matricula`),
  INDEX `fk_Uni_Egresados_Uni_Carreras1_idx` (`Uni_Carreras_id_carrrera` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Kardex`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Kardex` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Kardex` (
  `id_kardex` INT NOT NULL,
  `Matricula` VARCHAR(200) NULL,
  `Uni_Acreditacion_Materia_idi_Acreditacion_Mat` INT NOT NULL,
  `Uni_Materias_id_materia` VARCHAR(200) NOT NULL,
  `Uni_Egresados_idUni_Egresados` INT NOT NULL,
  `Uni_Alumnos_Matricula` VARCHAR(45) NOT NULL,
  `Uni_Calficacion_id_calficacion` INT NOT NULL,
  PRIMARY KEY (`id_kardex`),
  INDEX `fk_Uni_Kardex_Uni_Acreditacion_Materia1_idx` (`Uni_Acreditacion_Materia_idi_Acreditacion_Mat` ASC) ,
  INDEX `fk_Uni_Kardex_Uni_Materias1_idx` (`Uni_Materias_id_materia` ASC) ,
  INDEX `fk_Uni_Kardex_Uni_Egresados1_idx` (`Uni_Egresados_idUni_Egresados` ASC) ,
  INDEX `fk_Uni_Kardex_Uni_Alumnos1_idx` (`Uni_Alumnos_Matricula` ASC) ,
  INDEX `fk_Uni_Kardex_Uni_Calficacion1_idx` (`Uni_Calficacion_id_calficacion` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_semestre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_semestre` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_semestre` (
  `id_semestre` INT NOT NULL,
  `semestre` VARCHAR(45) NULL,
  `creditos` VARCHAR(45) NULL,
  `Uni_Carreras_id_carrrera` INT NOT NULL,
  PRIMARY KEY (`id_semestre`),
  INDEX `fk_Uni_semestre_Uni_Carreras1_idx` (`Uni_Carreras_id_carrrera` ASC)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Uni_Alumnos_has_Uni_semestre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Alumnos_has_Uni_semestre` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Alumnos_has_Uni_semestre` (
  `Uni_Alumnos_Matricula` VARCHAR(45) NOT NULL,
  `Uni_semestre_id_semestre` INT NOT NULL,
  PRIMARY KEY (`Uni_Alumnos_Matricula`, `Uni_semestre_id_semestre`),
  INDEX `fk_Uni_Alumnos_has_Uni_semestre_Uni_semestre1_idx` (`Uni_semestre_id_semestre` ASC) ,
  INDEX `fk_Uni_Alumnos_has_Uni_semestre_Uni_Alumnos1_idx` (`Uni_Alumnos_Matricula` ASC)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uni_Alumnos_has_Uni_Carreras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uni_Alumnos_has_Uni_Carreras` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uni_Alumnos_has_Uni_Carreras` (
  `Uni_Alumnos_Matricula` VARCHAR(45) NOT NULL,
  `Uni_Carreras_id_carrrera` INT NOT NULL,
  PRIMARY KEY (`Uni_Alumnos_Matricula`, `Uni_Carreras_id_carrrera`),
  INDEX `fk_Uni_Alumnos_has_Uni_Carreras_Uni_Carreras1_idx` (`Uni_Carreras_id_carrrera` ASC) ,
  INDEX `fk_Uni_Alumnos_has_Uni_Carreras_Uni_Alumnos1_idx` (`Uni_Alumnos_Matricula` ASC)
) ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




-- -- Create database --
-- CREATE DATABASE IF NOT EXISTS flask_crud;

-- -- Select database --
-- USE flask_crud;

-- CREATE TABLE tasks (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     description TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
