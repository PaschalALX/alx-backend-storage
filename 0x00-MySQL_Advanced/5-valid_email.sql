-- Reset Email Validity when changed

DROP TRIGGER IF EXISTS reset_email_validity

DELIMITER &&

CREATE TRIGGER reset_email_validity
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email
	THEN SET NEW.valid_email = 0;
	END IF
END; 
&&

DELIMITER ;
