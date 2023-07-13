-- add bonus

DROP PROCEDURE IF EXISTS addbonus;

DELIMITER &&

CREATE PROCEDURE addbonus(
	IN user_id INT, 
	IN project_name VARCHAR(255),
	IN score  INT
) 
COMMENT "add bonus"
LANGUAGE SQL

BEGIN
	DECLARE project_id INT DEFAULT NULL;
	SELECT id INTO project_id FROM projects WHERE name = project_name;

	if project_id = NULL THEN
		INSERT INTO projects(name) VALUES(project_name);
		SET project_id = LAST_INSERTED_ID();
	END IF;

	INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, project_id, score);
	
END;
&&

DELIMITER ;
