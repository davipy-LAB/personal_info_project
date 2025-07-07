CREATE TABLE info_app_person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    gender VARCHAR(255)
)

INSERT INTO info_app_person (name, email, phone, gender)
VALUES 
('Lucas Lima', 'lucas@example.com', '21999998888', 'male'),
('Letícia Souza', 'leticia@example.com', '21999997777', 'female');

SELECT * FROM info_app_person
WHERE name ILIKE '%l%';

UPDATE info_app_person
SET email = 'novoemail@example.com'
WHERE name = 'Lucas Lima';

DELETE FROM info_app_person
WHERE email = 'leticia@example.com';

SELECT 
    split_part(name, ' ', 1) AS first_name,
    COUNT(*) AS quantidade
FROM info_app_person
GROUP BY first_name
ORDER BY quantidade DESC;

SELECT p.name, c.message
FROM info_app_contactlog c
JOIN info_app_person p ON c.person_id = p.id
WHERE p.gender = 'female';

SELECT p.name, COUNT(c.id) as total_logs
FROM info_app_contactlog c
JOIN info_app_person p ON c.person_id = p.id
GROUP BY p.name
ORDER BY total_logs DESC;
