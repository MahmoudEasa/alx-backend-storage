-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE total_score INT;
	DECLARE total_count INT DEFAULT 0;

	SELECT SUM(score), COUNT(*) INTO total_score, total_count
		FROM corrections
		WHERE corrections.user_id = user_id;

	IF total_count > 0 THEN
		UPDATE users SET average_score = total_score / total_count
		WHERE users.id = user_id;
	END IF;
END$$
DELIMITER ;

