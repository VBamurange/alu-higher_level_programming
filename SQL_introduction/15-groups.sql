-- number by score
SELECT score, COUNT(score) AS NUMBER FROM second_table GROUP BY score ORDER BY score DESC;
