INSERT INTO person (name, email, phone, gender)
VALUES 
('Lucas Lima', 'lucas@example.com', '21999998888', 'male'),
('Letícia Souza', 'leticia@example.com', '21999997777', 'female');

SELECT * FROM person
WHERE name ILIKE '%l%';

UPDATE person
SET email = 'novoemail@example.com'
WHERE name = 'Lucas Lima';

DELETE FROM person
WHERE email = 'leticia@example.com';

SELECT 
    split_part(name, ' ', 1) AS first_name,
    COUNT(*) AS quantidade
FROM person
GROUP BY first_name
ORDER BY quantidade DESC;
