SELECT c.ID
FROM ECOLI_DATA AS c
JOIN ECOLI_DATA AS p ON c.PARENT_ID = p.ID      -- c: 자식, p: 부모
JOIN ECOLI_DATA AS gp ON p.PARENT_ID = gp.ID    -- gp: 조부모
WHERE gp.PARENT_ID IS NULL                      -- 조부모가 1세대여야 함
ORDER BY c.ID;