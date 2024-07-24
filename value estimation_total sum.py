import pandas as pd

# 예시 데이터
data = pd.DataFrame({
    "it_rnd_work": [...],  # 국가 R&D 과제 데이터
    "it_rnd_success": [...],  # 국가 R&D 성과 데이터
    "it_rnd_success_ratio": [...],  # R&D 과제 대비 성과율 데이터
    "it_patent": [...],  # 특허 개수 데이터
    "it_credit": [...]   # 신용등급 데이터 (이미 점수화 되었다고 가정)
})

# 각 지표를 정규화
data['it_rnd_work_normalized'] = (data['it_rnd_work'] - data['it_rnd_work'].min()) / (data['it_rnd_work'].max() - data['it_rnd_work'].min())
data['it_rnd_success_normalized'] = (data['it_rnd_success'] - data['it_rnd_success'].min()) / (data['it_rnd_success'].max() - data['it_rnd_success'].min())
data['it_rnd_success_ratio_normalized'] = (data['it_rnd_success_ratio'] - data['it_rnd_success_ratio'].min()) / (data['it_rnd_success_ratio'].max() - data['it_rnd_success_ratio'].min())
data['it_patent_normalized'] = (data['it_patent'] - data['it_patent'].min()) / (data['it_patent'].max() - data['it_patent'].min())

# 점수 계산
data['score'] = (data['it_rnd_work_normalized'] * 0.10 +
                 data['it_rnd_success_normalized'] * 0.10 +
                 data['it_rnd_success_ratio_normalized'] * 0.20 +
                 data['it_patent_normalized'] * 0.20 +
                 data['it_credit'] * 0.20)
