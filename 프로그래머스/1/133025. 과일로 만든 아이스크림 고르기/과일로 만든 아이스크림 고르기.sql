SELECT F.FLAVOR
FROM FIRST_HALF AS F
JOIN ICECREAM_INFO AS I
ON F.FLAVOR = I.FLAVOR
WHERE I.INGREDIENT_TYPE = 'fruit_based' AND F.TOTAL_ORDER > 3000
ORDER BY F.TOTAL_ORDER DESC;
