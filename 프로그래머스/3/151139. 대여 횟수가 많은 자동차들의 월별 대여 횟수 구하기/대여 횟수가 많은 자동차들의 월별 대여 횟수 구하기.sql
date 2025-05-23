-- 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상 
-- 월별 자동차 ID 별 총 대여 횟수

WITH FILTERED_HISTORY AS (
    SELECT *
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN DATE '2022-08-01' AND DATE '2022-10-31'
),
QUALIFIED_CAR AS (
    SELECT CAR_ID
    FROM FILTERED_HISTORY
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
)
SELECT
    EXTRACT(MONTH FROM H.START_DATE) AS MONTH,
    H.CAR_ID,
    COUNT(*) AS RECORDS
FROM FILTERED_HISTORY H
JOIN QUALIFIED_CAR Q ON H.CAR_ID = Q.CAR_ID
GROUP BY EXTRACT(MONTH FROM H.START_DATE), H.CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;
