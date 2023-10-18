-- task six
-- procedure to add correction for student project
DELIMITER //
CREATE PROCEDURE AddBonus(
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
DECLARE project_id INT;
  -- Check if the project_name already exists in the projects table
  SELECT id INTO project_id FROM projects WHERE name = project_name;
  
  -- If the project_name doesn't exist, create a new project
  IF project_id IS NULL THEN
      INSERT INTO projects (name) VALUES (project_name);
      SET project_id = LAST_INSERT_ID();
  END IF;
  
  -- Add a new correction for the student
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END; 

DELIMITER ;