ALTER TABLE class
ADD CONSTRAINT fk_teacher_class
FOREIGN KEY (TeacherId) REFERENCES teacher(Id)

/*ALTER TABLE student
ADD CONSTRAINT fk_student_class
FOREIGN KEY (ClassId) REFERENCES class(Id)*/

/*ALTER TABLE classlesson
ADD CONSTRAINT fk_classlesson_class
FOREIGN KEY (ClassId) REFERENCES class(Id)

ALTER TABLE classlesson
ADD CONSTRAINT fk_classlesson_lesson
FOREIGN KEY (LessonId) REFERENCES lesson(Id)

ALTER TABLE classlesson
ADD CONSTRAINT fk_classlesson_teacher
FOREIGN KEY (TeacherId) REFERENCES teacher(Id)*/