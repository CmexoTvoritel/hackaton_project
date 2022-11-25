
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
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    mail VARCHAR(100) NOT NULL,
    name VARCHAR(60) NOT NULL,
    surname VARCHAR(60) NOT NULL,
    patronymic VARCHAR(60) NOT NULL
);
