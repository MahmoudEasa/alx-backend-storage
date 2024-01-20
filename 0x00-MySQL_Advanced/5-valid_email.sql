-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
DROP TRIGGER IF EXISTS validate_email;

DELIMITER $$ ;
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
IF OLD.email != NEW.email THEN
SET NEW.valid_email = 0;
END IF$$
DELIMITER ; $$
