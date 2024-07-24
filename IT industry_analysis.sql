-- IT 산업직군 기업 선별
SELECT DISTINCT(BusinessNum), 기업명, indNm
FROM cmp_info
WHERE indNm REGEXP '컴퓨터|프로그래밍|시스템|소프트웨어|데이터베이스|IT';
-- CSV 파일로 export (it_ind)
SELECT * INTO OUTFILE '/path/to/output.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM cmp_info;

-- IT 산업직군 재무정보
SELECT A.*
FROM finance_extract A, it_ind B
WHERE B.BusinessNum = A.﻿BusinessNum
GROUP BY A.BusinessNum;

-- IT 기업별 재무 & rnd성과 & 특허정보 import 완료

-- IT 기업별 R&D 과제, 성과의 각 개수와 성과백분율, 특허개수
SELECT 
    w.BusinessNum,
    w.work_count,
    s.success_count,
    p.patent_count,
    (s.success_count / w.work_count) * 100 as success_ratio
FROM
    (SELECT BusinessNum, COUNT(*) as work_count
     FROM it_rnd_work
     WHERE BusinessNum IS NOT NULL
     GROUP BY BusinessNum) as w
LEFT JOIN
    (SELECT BusinessNum, COUNT(*) as success_count
     FROM it_rnd_success
     WHERE BusinessNum IS NOT NULL
     GROUP BY BusinessNum) as s
ON w.BusinessNum = s.BusinessNum
LEFT JOIN
    (SELECT BusinessNum, COUNT(*) as patent_count
     FROM it_patent
     WHERE patentTitle IS NOT NULL
     GROUP BY BusinessNum) as p
ON w.BusinessNum = p.BusinessNum;

-- 신용등급
select criGrd from credit_level where BusinessNum = 1078806835;


