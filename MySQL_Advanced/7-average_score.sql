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
  INSERT INTO users (user_id, average_score)
  VALUES (user_id, average_score)
  ON DUPLICATE KEY UPDATE average_score = average_score;
END ;
DELIMITER ;