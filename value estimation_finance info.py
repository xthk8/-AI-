import pandas as pd

# CSV 파일 읽기
data = pd.read_csv("C:/Users/USER/Desktop/DBI2023/it산업기업 재무정보.csv")

def calculate_score(row):
    score = 0

    # 매출총이익, 영업이익, 당기순이익에 따른 점수 계산
    if row['accNm'] == '매출총이익' and row['acctAmt'] > 0:
        score += 10
    if row['accNm'] == '영업이익' and row['acctAmt'] > 0:
        score += 10
    if row['accNm'] == '당기순이익(손실)' and row['acctAmt'] > 0:
        score += 10

    # 성장성지표 내 항목에 따른 점수 계산
    if row['stNm'] == '성장성지표':
        if row['accNm'] == '총자산 증가율' and row['acctAmt'] > 0:
            score += 6
        if row['accNm'] == '유형자산 증가율' and row['acctAmt'] > 0:
            score += 4
        if row['accNm'] == '매출 증가율' and row['acctAmt'] > 0:
            score += 8
        if row['accNm'] == '총자산' and row['acctAmt'] > 0:
            score += 4
        if row['accNm'] == '자기자본' and row['acctAmt'] > 0:
            score += 4
        if row['accNm'] == '차입금' and row['acctAmt'] > 0:
            score -= 4

    # 안정성지표 내 항목에 따른 점수 계산
    if row['stNm'] == '안정성지표' and row['accNm'] == '유동비율':
        if row['acctAmt'] >= 100:
            score += 20
        else:
            score -= 20
    
    return score

# 각 행에 대해 점수 계산
data['score_v4'] = data.apply(calculate_score, axis=1)

# 기업별로 점수 합계 계산
company_scores_v4 = data.groupby('BusinessNum')['score_v4'].sum().reset_index().sort_values(by='score_v4', ascending=False)

company_scores_v4.head()
