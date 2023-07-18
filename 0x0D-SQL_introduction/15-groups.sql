-- Lists the number of records with the same score in the 'second_table' table
-- the result should display the score and the number of records with the label 'number'
SELECT score, COUNT(*) AS number
FROM second_table
WHERE label = 'number'
GROUP BY score
ORDER BY score DESC
