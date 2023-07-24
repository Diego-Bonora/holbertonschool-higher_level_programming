-- lists all the scores and the number of times it apears

SELECT score,COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;