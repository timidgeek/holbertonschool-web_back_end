-- task seven
-- procedure that gets the average store for student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE average_score DECIMAL; 

  -- get average score for the user
  SELECT AVG(score) INTO average_score
  FROM corrections
  WHERE corrections.user_id = user_id;

  -- insert the average score for the user
  UPDATE users 
  SET average_score
  WHERE id = user_id;
END ;
DELIMITER ;