# Modelo de Datos

Para el desarrollo del sistema **Aprenzy** se propone el uso de un modelo de datos relacional, implementado en un sistema gestor de bases de datos que permita almacenar y administrar de forma segura la información académica y administrativa de la plataforma.

El modelo de datos está compuesto por las siguientes entidades principales:

## Entidad Usuario

Almacena la información general de las personas que interactúan con el sistema.

**Atributos:**

* id_usuario (clave primaria)
* nombre
* apellido
* correo_electronico
* contraseña
* rol
* fecha_registro
* estado

## Entidad Curso

Representa los cursos disponibles dentro de la plataforma.

**Atributos:**

* id_curso (clave primaria)
* nombre
* descripcion
* fecha_creacion
* estado

## Entidad Modulo

Permite organizar el contenido de un curso en secciones o unidades.

**Atributos:**

* id_modulo (clave primaria)
* titulo
* descripcion
* id_curso (clave foránea)

## Entidad Actividad

Contiene las actividades asignadas a los estudiantes dentro de un módulo.

**Atributos:**

* id_actividad (clave primaria)
* titulo
* descripcion
* fecha_limite
* id_modulo (clave foránea)

## Entidad Evaluacion

Almacena la información de las evaluaciones realizadas dentro de los cursos.

**Atributos:**

* id_evaluacion (clave primaria)
* titulo
* descripcion
* puntaje_maximo
* fecha_publicacion
* id_modulo (clave foránea)

## Entidad Resultado

Registra las calificaciones obtenidas por los estudiantes.

**Atributos:**

* id_resultado (clave primaria)
* calificacion
* fecha_realizacion
* id_usuario (clave foránea)
* id_evaluacion (clave foránea)

## Entidad Progreso

Permite realizar seguimiento al avance de los estudiantes en los cursos.

**Atributos:**

* id_progreso (clave primaria)
* porcentaje_avance
* fecha_actualizacion
* id_usuario (clave foránea)
* id_curso (clave foránea)

## Relaciones Principales

* Un usuario puede estar inscrito en varios cursos.
* Un curso puede contener múltiples módulos.
* Un módulo puede contener múltiples actividades y evaluaciones.
* Un estudiante puede presentar múltiples evaluaciones.
* Cada evaluación puede generar uno o varios resultados.
* El progreso permite medir el avance de un estudiante dentro de un curso.

Este modelo permite gestionar de manera estructurada la información académica, facilitando el seguimiento del aprendizaje, la administración de contenidos y el control del desempeño de los estudiantes dentro de la plataforma Aprenzy.
