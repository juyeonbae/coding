SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY -- 결과로 보여줄 것
FROM ITEM_TREE T                       -- 업그레이드 관계
JOIN ITEM_INFO P                       -- 부모 아이템 정보
  ON T.PARENT_ITEM_ID = P.ITEM_ID
JOIN ITEM_INFO I                       -- 자식 아이템 정보
  ON T.ITEM_ID = I.ITEM_ID
WHERE P.RARITY = 'RARE'                -- 부모가 RARE일 때만
ORDER BY I.ITEM_ID DESC;               -- 결과는 ID 내림차순
