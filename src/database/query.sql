-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Universidad
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Universidad
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS Universidad DEFAULT CHARACTER SET utf8 ;
USE Universidad ;

-- -----------------------------------------------------
-- Table Universidad.Role
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Role (
  Role_id INT NOT NULL,
  name_rol VARCHAR(45) NULL,
  Crate_at_time VARCHAR(45) NULL,
  update_at_time VARCHAR(45) NULL,
  PRIMARY KEY (Role_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.UserUni
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.UserUni (
  User_id INT NOT NULL,
  name VARCHAR(60) NULL,
  email VARCHAR(60) NULL,
  password VARCHAR(255) NULL,
  fk_User_Role INT NOT NULL,
  PRIMARY KEY (User_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Carreras
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Carreras (
  id_carrrera INT NOT NULL,
  Cve_Carrera VARCHAR(200) NULL,
  Nombre_Carrera VARCHAR(200) NULL,
  Duracion VARCHAR(45) NULL,
  Requisitos_ad VARCHAR(200) NULL,
  Creditos_gradu VARCHAR(45) NULL,
  PRIMARY KEY (id_carrrera))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Contacto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Contacto (
  id_Contacto INT NOT NULL,
  nombre VARCHAR(45) NULL,
  apellido_ma VARCHAR(45) NULL,
  apellido_pa VARCHAR(45) NULL,
  Genero VARCHAR(45) NULL,
  email VARCHAR(45) NULL,
  telefono VARCHAR(45) NULL,
  celular VARCHAR(45) NULL,
  direcion VARCHAR(45) NULL,
  colonia VARCHAR(45) NULL,
  Estado VARCHAR(45) NULL,
  Municipio VARCHAR(45) NULL,
  Fecha_nacimiento DATETIME NULL,
  Contactocol VARCHAR(45) NULL,
  PRIMARY KEY (id_Contacto))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Profesor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Profesor (
  Cve_Profesor VARCHAR(200) NOT NULL,
  Especializacion VARCHAR(45) NULL,
  materia_impar VARCHAR(45) NULL,
  nivel_acade VARCHAR(45) NULL,
  titulo_acade VARCHAR(45) NULL,
  fecha_ingreso DATE NULL,
  User_User_id INT NOT NULL,
  Contacto_id_Contacto INT NOT NULL,
  PRIMARY KEY (Cve_Profesor))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Grupos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Grupos (
  Cve_grupo VARCHAR(200) NOT NULL,
  Uni_Carreras_id_carrrera INT NOT NULL,
  Uni_Profesor_Cve_Profesor VARCHAR(200) NOT NULL,
  PRIMARY KEY (Cve_grupo))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Materias
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Materias (
  id_materia VARCHAR(200) NOT NULL,
  nombre_Materia VARCHAR(45) NULL,
  Cred_Materia VARCHAR(45) NULL,
  Requisitos_Previos VARCHAR(45) NULL,
  Uni_Grupos_Cve_grupo VARCHAR(200) NOT NULL,
  PRIMARY KEY (id_materia))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Acreditacion_Materia
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Acreditacion_Materia (
  idi_Acreditacion_Mat INT NOT NULL,
  Tipo_de_Acreditacion VARCHAR(45) NULL,
  Estado_actual VARCHAR(45) NULL,
  PRIMARY KEY (idi_Acreditacion_Mat))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Calficacion
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Calficacion (
  id_calficacion INT NOT NULL AUTO_INCREMENT,
  fecha_evaluacion DATE NULL,
  Uni_Materias_id_materia VARCHAR(200) NOT NULL,
  Uni_Acreditacion_Materia_idi_Acreditacion_Mat INT NOT NULL,
  PRIMARY KEY (id_calficacion)
) ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table Universidad.Uni_Alumnos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Alumnos (
  Matricula VARCHAR(45) NOT NULL,
  Esta_Civil VARCHAR(45) NULL,
  User_User_id INT NOT NULL,
  Contacto_id_Contacto INT NOT NULL,
  Uni_Calficacion_id_calficacion INT NOT NULL,
  PRIMARY KEY (Matricula))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Egresados
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Egresados (
  Matricula INT NOT NULL,
  id_carrera INT NULL,
  año_grad VARCHAR(45) NULL,
  Uni_Carreras_id_carrrera INT NOT NULL,
  PRIMARY KEY (Matricula))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Kardex
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Kardex (
  id_kardex INT NOT NULL,
  Matricula VARCHAR(200) NULL,
  Historico VARCHAR(45) NULL,
  Uni_Acreditacion_Materia_idi_Acreditacion_Mat INT NOT NULL,
  Uni_Materias_id_materia VARCHAR(200) NOT NULL,
  Uni_Egresados_idUni_Egresados INT NOT NULL,
  Uni_Alumnos_Matricula VARCHAR(45) NOT NULL,
  Uni_Calficacion_id_calficacion INT NOT NULL,
  PRIMARY KEY (id_kardex))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_semestre
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_semestre (
  id_semestre INT NOT NULL,
  semestre VARCHAR(45) NULL,
  creditos VARCHAR(45) NULL,
  Uni_Carreras_id_carrrera INT NOT NULL,
  PRIMARY KEY (id_semestre))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Alumnos_has_Uni_semestre
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Alumnos_has_Uni_semestre (
  Uni_Alumnos_Matricula VARCHAR(45) NOT NULL,
  Uni_semestre_id_semestre INT NOT NULL,
  PRIMARY KEY (Uni_Alumnos_Matricula, Uni_semestre_id_semestre))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Uni_Alumnos_has_Uni_Carreras
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Uni_Alumnos_has_Uni_Carreras (
  Uni_Alumnos_Matricula VARCHAR(45) NOT NULL,
  Uni_Carreras_id_carrrera INT NOT NULL,
  PRIMARY KEY (Uni_Alumnos_Matricula, Uni_Carreras_id_carrrera))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Universidad.Bitacora
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Universidad.Bitacora (
  idBitacora INT NOT NULL,
  Cambio_act VARCHAR(45) NULL,
  Cambio_anterior VARCHAR(45) NULL,
  Fecha_hora VARCHAR(45) NULL,
  User VARCHAR(45) NULL,
  PRIMARY KEY (idBitacora))
ENGINE = InnoDB;

DELIMITER //

CREATE TRIGGER carreras_after_update
AFTER UPDATE ON uni_carreras
FOR EACH ROW
BEGIN
    INSERT INTO Bitacora (Cambio_act, Fecha_hora, User)
    VALUES ('Registro modificado en carreras', NOW(), SUBSTRING(USER(), 1, INSTR(USER(), "@") - 1));
END//

DELIMITER ;
DELIMITER //

CREATE TRIGGER carreras_after_delete
AFTER DELETE ON uni_carreras
FOR EACH ROW
BEGIN
    INSERT INTO Bitacora (Cambio_act, Fecha_hora, User)
    VALUES ('Registro eliminado en carreras', NOW(), SUBSTRING(USER(), 1, INSTR(USER(), "@") - 1));
END//

DELIMITER ;
  DELIMITER //

  CREATE TRIGGER carreras_after_delete
  AFTER INSERT ON uni_carreras
  FOR EACH ROW
  BEGIN
      INSERT INTO Bitacora (Cambio_act, Fecha_hora, User)
      VALUES ('Registro acgregado en carreras', NOW(), SUBSTRING(USER(), 1, INSTR(USER(), "@") - 1));
  END//

  DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;