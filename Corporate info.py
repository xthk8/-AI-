import pandas as pd

it_ind = pd.read_csv("C:/Users/USER/Desktop/DBI2023/IT산업.csv")
finance_extract = pd.read_csv("C:/Users/USER/Desktop/DBI2023/재무재표 데이터 추출.csv")
patent_info = pd.read_csv("C:/Users/USER/Desktop/DBI2023/DBI2023-Track1-학습데이터셋_v3/특허정보상세_train.csv")
rnd_success = pd.read_csv("C:/Users/USER/Desktop/DBI2023/DBI2023-Track1-학습데이터셋_v3/국가R&D성과_train.csv")
rnd_work = pd.read_csv("C:/Users/USER/Desktop/DBI2023/DBI2023-Track1-학습데이터셋_v3/국가R&D과제_train.csv")

# BusinessNum을 기준으로 두 데이터프레임을 병합(merge)
it_finance = finance_extract[finance_extract['BusinessNum'].isin(it_ind['BusinessNum'])]
it_patent = patent_info[patent_info['BusinessNum'].isin(it_ind['BusinessNum'])]
it_rnd = rnd_success[rnd_success['BusinessNum'].isin(it_ind['BusinessNum'])]
it_rnd_work = rnd_work[rnd_work['BusinessNum'].isin(it_ind['BusinessNum'])]

print(it_finance)

# it_finance 결과 csv 파일로 export
it_finance.to_csv('it산업기업 재무정보.csv', index=False, encoding='utf-8-sig')
it_patent.to_csv('it산업기업 특허정보.csv', index=False, encoding='utf-8-sig')
it_rnd.to_csv('it산업기업 연구개발.csv', index=False, encoding='utf-8-sig')
it_rnd_work.to_csv('it산업기업 연구개발 과제.csv', index=False, encoding='utf-8-sig')