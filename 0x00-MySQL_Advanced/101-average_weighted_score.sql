-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	UPDATE users SET average_score = (SELECT SUM(C.score * P.weight) / SUM(P.weight)
                FROM corrections AS C JOIN projects AS P
                ON C.project_id = P.id
                WHERE C.user_id = users.id);
END$$
DELIMITER ;

