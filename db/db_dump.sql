
-- Таблица: Users
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    tg_id BIGINT NOT NULL,
    mail VARCHAR(100) NOT NULL,
    name VARCHAR(60) NOT NULL,
    surname VARCHAR(60) NOT NULL,
    patronymic VARCHAR(60) NOT NULL,
    group_name VARCHAR(10) NOT NULL
);

-- Таблица: Teachers
CREATE TABLE IF NOT EXISTS Teachers (
    id SERIAL PRIMARY KEY,
    mail VARCHAR(100) NOT NULL,
    name VARCHAR(60) NOT NULL,
    surname VARCHAR(60) NOT NULL,
    patronymic VARCHAR(60) NOT NULL
);

-- Таблица: Lectures
CREATE TABLE IF NOT EXISTS Lectures (
    id SERIAL PRIMARY KEY,
    teacher_id BIGINT UNIQUE,
    group_names VARCHAR(10)[],
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id) ON DELETE CASCADE
);

-- Таблица: Questions_lecture
CREATE TABLE IF NOT EXISTS Lecture_questions (
    id SERIAL PRIMARY KEY,
    lecture_id BIGINT,
    q_text VARCHAR(512),
    answers VARCHAR(50)[],
    FOREIGN KEY (lecture_id) REFERENCES Lectures(id) ON DELETE CASCADE
);

-- Таблица: Student_answers
CREATE TABLE IF NOT EXISTS Student_answers (
    id SERIAL PRIMARY KEY,
    q_id BIGINT,
    student_id BIGINT,
    answer BOOLEAN NOT NULL,
    FOREIGN KEY (q_id) REFERENCES Lecture_questions(id) ON DELETE CASCADE
);