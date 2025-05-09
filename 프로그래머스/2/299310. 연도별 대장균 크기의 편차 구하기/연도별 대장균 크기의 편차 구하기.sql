-- 1. 연도별 최대 colony 크기를 미리 구해두는 CTE 정의
WITH MAX_SIZE_PER_YEAR AS (
    SELECT 
        YEAR(DIFFERENTIATION_DATE) AS YEAR,    -- 연도만 추출
        MAX(SIZE_OF_COLONY) AS MAX_SIZE        -- 해당 연도의 최대 colony size
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)        -- 연도별로 그룹화
)

-- 2. ECOLI_DATA와 위에서 만든 최대값 테이블을 JOIN해서 편차 계산
SELECT 
    YEAR(E.DIFFERENTIATION_DATE) AS YEAR,              -- 연도 추출
    (M.MAX_SIZE - E.SIZE_OF_COLONY) AS YEAR_DEV,       -- 최대 size - 현재 size = 편차
    E.ID                                                -- 대장균 개체 ID
FROM ECOLI_DATA E
JOIN MAX_SIZE_PER_YEAR M
    ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR           -- 연도 기준으로 조인

ORDER BY YEAR, YEAR_DEV;
