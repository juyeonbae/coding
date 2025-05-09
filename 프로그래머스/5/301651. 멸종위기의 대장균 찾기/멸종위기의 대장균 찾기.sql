WITH RECURSIVE generation_tree AS (
    -- 1세대: PARENT_ID가 NULL
    SELECT ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 자식: 부모 ID 연결 + 세대 1씩 증가
    SELECT e.ID, g.GENERATION + 1
    FROM ECOLI_DATA e
    JOIN generation_tree g ON e.PARENT_ID = g.ID
),
-- 자식이 있는 개체를 모음
parent_ids AS (
    SELECT DISTINCT PARENT_ID AS ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NOT NULL
)
-- 세대와 자식 없는 개체만 선택해서 세대별로 카운트
SELECT COUNT(*) AS COUNT, g.GENERATION
FROM generation_tree g
LEFT JOIN parent_ids p ON g.ID = p.ID
WHERE p.ID IS NULL  -- 자식 없는 경우
GROUP BY g.GENERATION
ORDER BY g.GENERATION;
