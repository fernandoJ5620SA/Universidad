-- Datos de ejemplo para la tabla Role
INSERT INTO Universidad.Role (Role_id, name_rol, Crate_at_time, update_at_time) VALUES
(5, 'Admin', '2024-01-01 00:00:00', '2024-01-01 00:00:00'),
(6, 'Profesor', '2024-01-01 00:00:00', '2024-01-01 00:00:00'),
(7, 'Estudiante', '2024-01-01 00:00:00', '2024-01-01 00:00:00'),
(8, 'Coordinador', '2024-01-01 00:00:00', '2024-01-01 00:00:00');

-- Datos de ejemplo para la tabla UserUni
INSERT INTO Universidad.UserUni (User_id, name, email, password, fk_User_Role) VALUES
(5, 'John Doe', 'john.doe@example.com', 'password123', 5),
(6, 'Jane Smith', 'jane.smith@example.com', 'password456', 6),
(7, 'Alice Johnson', 'alice.johnson@example.com', 'password789', 7),
(8, 'Bob Brown', 'bob.brown@example.com', 'password012', 8);

-- Datos de ejemplo para la tabla Uni_Carreras
INSERT INTO Universidad.Uni_Carreras (id_carrrera, Cve_Carrera, Nombre_Carrera, Duracion, Requisitos_ad, Creditos_gradu) VALUES
(5, 'CS101', 'Computer Science', '4 años', 'High School Diploma', '240'),
(6, 'MATH202', 'Mathematics', '4 años', 'High School Diploma', '240'),
(7, 'PHYS303', 'Physics', '4 años', 'High School Diploma', '240'),
(8, 'CHEM404', 'Chemistry', '4 años', 'High School Diploma', '240');

-- Datos de ejemplo para la tabla Contacto
INSERT INTO Universidad.Contacto (id_Contacto, nombre, apellido_ma, apellido_pa, Genero, email, telefono, celular, direcion, colonia, Estado, Municipio, Fecha_nacimiento, Contactocol) VALUES
(5, 'Carlos', 'Lopez', 'Garcia', 'Masculino', 'carlos.lopez@example.com', '1234567890', '0987654321', 'Calle Falsa 123', 'Centro', 'CDMX', 'CDMX', '1990-01-01 00:00:00', 'Ninguno'),
(6, 'Maria', 'Perez', 'Hernandez', 'Femenino', 'maria.perez@example.com', '1234567891', '0987654322', 'Avenida Siempreviva 742', 'Norte', 'CDMX', 'CDMX', '1992-02-02 00:00:00', 'Ninguno'),
(7, 'Luis', 'Martinez', 'Sanchez', 'Masculino', 'luis.martinez@example.com', '1234567892', '0987654323', 'Calle Verdadera 456', 'Sur', 'CDMX', 'CDMX', '1988-03-03 00:00:00', 'Ninguno'),
(8, 'Ana', 'Gonzalez', 'Diaz', 'Femenino', 'ana.gonzalez@example.com', '1234567893', '0987654324', 'Avenida Principal 789', 'Este', 'CDMX', 'CDMX', '1994-04-04 00:00:00', 'Ninguno');

-- Datos de ejemplo para la tabla Uni_Profesor
INSERT INTO Universidad.Uni_Profesor (Cve_Profesor, Especializacion, materia_impar, nivel_acade, titulo_acade, fecha_ingreso, User_User_id, Contacto_id_Contacto) VALUES
('P005', 'Computer Science', 'CS101', 'Doctorado', 'PhD', '2020-01-01', 6, 5),
('P006', 'Mathematics', 'MATH202', 'Doctorado', 'PhD', '2021-01-01', 6, 6),
('P007', 'Physics', 'PHYS303', 'Doctorado', 'PhD', '2022-01-01', 6, 7),
('P008', 'Chemistry', 'CHEM404', 'Doctorado', 'PhD', '2023-01-01', 6, 8);

-- Datos de ejemplo para la tabla Uni_Grupos
INSERT INTO Universidad.Uni_Grupos (Cve_grupo, Uni_Carreras_id_carrrera, Uni_Profesor_Cve_Profesor) VALUES
('G05', 5, 'P005'),
('G06', 6, 'P006'),
('G07', 7, 'P007'),
('G08', 8, 'P008');

-- Datos de ejemplo para la tabla Uni_Materias
INSERT INTO Universidad.Uni_Materias (id_materia, nombre_Materia, Cred_Materia, Requisitos_Previos, Uni_Grupos_Cve_grupo) VALUES
('M005', 'Algorithms', '6', 'None', 'G05'),
('M006', 'Calculus', '6', 'None', 'G06'),
('M007', 'Mechanics', '6', 'None', 'G07'),
('M008', 'Organic Chemistry', '6', 'None', 'G08');

-- Datos de ejemplo para la tabla Uni_Acreditacion_Materia
INSERT INTO Universidad.Uni_Acreditacion_Materia (idi_Acreditacion_Mat, Tipo_de_Acreditacion, Estado_actual) VALUES
(5, 'Examen', 'Aprobado'),
(6, 'Proyecto', 'Pendiente'),
(7, 'Tesis', 'Reprobado'),
(8, 'Trabajo', 'Aprobado');

-- Datos de ejemplo para la tabla Uni_Calficacion
INSERT INTO Universidad.Uni_Calficacion (id_calficacion, fecha_evaluacion, Uni_Materias_id_materia, Uni_Acreditacion_Materia_idi_Acreditacion_Mat) VALUES
(5, '2024-05-05', 'M005', 5),
(6, '2024-05-06', 'M006', 6),
(7, '2024-05-07', 'M007', 7),
(8, '2024-05-08', 'M008', 8);

-- Datos de ejemplo para la tabla Uni_Alumnos
INSERT INTO Universidad.Uni_Alumnos (Matricula, Esta_Civil, User_User_id, Contacto_id_Contacto, Uni_Calficacion_id_calficacion) VALUES
('A005', 'Soltero', 5, 6, 5),
('A006', 'Casado', 6, 8, 6),
('A007', 'Soltero', 7, 5, 7),
('A008', 'Casado', 8, 7, 8);

-- Datos de ejemplo para la tabla Uni_Egresados
INSERT INTO Universidad.Uni_Egresados (Matricula, id_carrera, año_grad, Uni_Carreras_id_carrrera) VALUES
(5, NULL, '2023', 5),
(6, NULL, '2023', 6),
(7, NULL, '2023', 7),
(8, NULL, '2023', 8);

-- Datos de ejemplo para la tabla Uni_Kardex
INSERT INTO Universidad.Uni_Kardex (id_kardex, Matricula, Historico, Uni_Acreditacion_Materia_idi_Acreditacion_Mat, Uni_Materias_id_materia, Uni_Egresados_idUni_Egresados, Uni_Alumnos_Matricula, Uni_Calficacion_id_calficacion) VALUES
(5, 'A005', 'Historico1', 5, 'M005', 5, 'A005', 5),
(6, 'A006', 'Historico2', 6, 'M006', 6, 'A006', 6),
(7, 'A007', 'Historico3', 7, 'M007', 7, 'A007', 7),
(8, 'A008', 'Historico4', 8, 'M008', 8, 'A008', 8);

-- Datos de ejemplo para la tabla Uni_semestre
INSERT INTO Universidad.Uni_semestre (id_semestre, semestre, creditos, Uni_Carreras_id_carrrera) VALUES
(5, 'Primer Semestre', '30', 5),
(6, 'Segundo Semestre', '30', 6),
(7, 'Tercer Semestre', '30', 7),
(8, 'Cuarto Semestre', '30', 8);

-- Datos de ejemplo para la tabla Uni_Alumnos_has_Uni_semestre
INSERT INTO Universidad.Uni_Alumnos_has_Uni_semestre (Uni_Alumnos_Matricula, Uni_semestre_id_semestre) VALUES
('A005', 5),
('A006', 6),
('A007', 7),
('A008', 8);

-- Datos de ejemplo para la tabla Uni_Alumnos_has_Uni_Carreras
INSERT INTO Universidad.Uni_Alumnos_has_Uni_Carreras (Uni_Alumnos_Matricula, Uni_Carreras_id_carrrera) VALUES
('A005', 5),
('A006', 6),
('A007', 7),
('A008', 8);

-- Datos de ejemplo para la tabla Bitacora
INSERT INTO Universidad.Bitacora (idBitacora, Cambio_act, Cambio_anterior, Fecha_hora, User) VALUES
(5, 'Cambio5', 'Anterior5', '2024-05-05 12:00:00', 'admin'),
(6, 'Cambio6', 'Anterior6', '2024-05-06 12:00:00', 'admin'),
(7, 'Cambio7', 'Anterior7', '2024-05-07 12:00:00', 'admin'),
(8, 'Cambio8', 'Anterior8', '2024-05-08 12:00:00', 'admin');
