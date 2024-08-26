-- SQL script that creates a stored procedure AddBonus
DELIMETER
CREATE OR REPLACE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
DECLARE
    project_id INT;
BEGIN
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name) RETURNING id INTO project_id;
    END IF;

    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, project_id, score);

END;//
DELIMETER ;
