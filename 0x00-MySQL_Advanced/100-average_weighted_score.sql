-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	SET @average = (SELECT SUM(C.score * P.weight) / SUM(P.weight)
	       	FROM corrections AS C JOIN projects AS P
		ON C.project_id = P.id
		WHERE C.user_id = user_id);
	UPDATE users SET average_score = @average WHERE users.id = user_id;
END$$
DELIMITER ;

