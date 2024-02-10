-- https://school.programmers.co.kr/learn/courses/30/lessons/59413

-- 입양 시각 구하기(2)
-- 제출 내역
-- 문제 설명
-- ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

-- NAME	TYPE	NULLABLE
-- ANIMAL_ID	VARCHAR(N)	FALSE
-- ANIMAL_TYPE	VARCHAR(N)	FALSE
-- DATETIME	DATETIME	FALSE
-- NAME	VARCHAR(N)	TRUE
-- SEX_UPON_OUTCOME	VARCHAR(N)	FALSE
-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

-- 예시
-- SQL문을 실행하면 다음과 같이 나와야 합니다.

-- HOUR	COUNT
-- 0	0
-- 1	0
-- 2	0
-- 3	0
-- 4	0
-- 5	0
-- 6	0
-- 7	3
-- 8	1
-- 9	1
-- 10	2
-- 11	13
-- 12	10
-- 13	14
-- 14	9
-- 15	7
-- 16	10
-- 17	12
-- 18	16
-- 19	2
-- 20	0
-- 21	0
-- 22	0
-- 23	0

-- 코드를 입력하세요
SELECT hours.HOUR, COUNT(animal_counts.HOUR) AS COUNT
FROM (
    SELECT 0 AS HOUR UNION ALL
    SELECT 1 UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10 UNION ALL
    SELECT 11 UNION ALL
    SELECT 12 UNION ALL
    SELECT 13 UNION ALL
    SELECT 14 UNION ALL
    SELECT 15 UNION ALL
    SELECT 16 UNION ALL
    SELECT 17 UNION ALL
    SELECT 18 UNION ALL
    SELECT 19 UNION ALL
    SELECT 20 UNION ALL
    SELECT 21 UNION ALL
    SELECT 22 UNION ALL
    SELECT 23
) AS hours
LEFT JOIN (
    SELECT HOUR(DATETIME) AS HOUR
    FROM ANIMAL_OUTS
) AS animal_counts ON hours.HOUR = animal_counts.HOUR
GROUP BY hours.HOUR
ORDER BY hours.HOUR;
