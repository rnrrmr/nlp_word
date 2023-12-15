# nlp_word_screening

🥯 이력서 데이터셋을 사용하여 머신러닝 파이프라인을 구축하고 실행

🎱 데이터셋 : Kaggle [UpdatedResumeDataSet](https://www.kaggle.com/datasets/dhainjeamita/updatedresumedataset?resource=download) 활용

🧰 라이브러리 : 
* numpy : 효율적인 수치 계산 및 배열 조작
* pandas : 데이터셋을 효과적으로 다루기 위해 사용
* matplotlib : 데이터 분포를 시각화
* sklearn(scikit-learn) : Naive bayes, k-최근접 이웃 classifier 및 기타 머신러닝 모델을 사용하여 이력서 분류를 수행
* seaborn(matplotlib 기반) : 데이터 분포를 시각화
* nltk : 자연어 처리를 위한 라이브러리, 텍스트 데이터를 다루고 분석. 텍스트 데이터의 전처리를 위해 사용
* wordcloud : 텍스트 데이터에서 단어 빈도를 시각적으로 나타냄. 이력서의 단어 빈도를 시각화
* scipy : 과학 및 공학 계산. 희소 행렬을 다루기 위한 hstack 함수를 사용



---

1. 데이터 로딩 및 이해:
  - pandas를 사용하여 'UpdatedResumeDataSet.csv' 파일을 읽고, 데이터프레임에 저장
  - 'cleaned_resume'이라는 새 열을 추가하고 초기값은 빈 문자열로 설정
  - 처음 5개 행을 출력하여 데이터를 확인

  
2. 이력서 카테고리 분석:
- 고유한 이력서 카테고리를 출력하고, 해당 카테고리의 수를 출력
- 각 카테고리별로 데이터의 수를 시각화


3. 텍스트 데이터 전처리:
- 정규표현식을 사용하여 이력서 텍스트를 정제하는 cleanResume 함수를 정의
- NLTK를 사용하여 사용하지 않는 용어 및 구두점을 제거하고, 단어 빈도를 계산하여 가장 빈도가 높은 단어 50개를 출력
- WordCloud를 사용하여 이력서에서 가장 빈도가 높은 단어들을 시각화


4. 머신러닝 모델 학습 및 평가:
- LabelEncoder를 사용하여 이력서 카테고리를 숫자로 인코딩
- TF-IDF (Term Frequency-Inverse Document Frequency)를 사용하여 텍스트 데이터를 벡터화
- K-최근접 이웃 (KNeighborsClassifier) 분류기를 사용하여 모델을 학습하고 평가
- 학습 세트와 테스트 세트에서의 정확도를 출력하고, 분류 보고서를 통해 모델의 성능을 분석

5. 텍스트 데이터 전처리 후 새로운 csv 파일로 생성 및 저장

---

   
데이터의 이해, 텍스트 전처리, 시각화, 머신러닝 모델 학습 및 평가를 포함한 단계를 수행하여 이력서 데이터에 대한 분석 및 분류를 진행


---

# vader를 이용한 문장 감정 평가

🥯 Vader를 사용하여 문장의 긍정, 중립, 부정을 판단

1. 여러가지 문장을 준비
2. 감정 평가할 문장을 SentimentIntensityAnalyzer().polarity_scores()로 호출
3. 종합점수로 문장을 평가
   - 강한부정 : -2
   - 약한부정 : -1
   - 중립     : 0
   - 약한긍정 : 1
   - 강한긍정 : 2
4. BeautifulSoup을 이용해 뉴스기사 스크랩
5. 뉴스의 헤더라인을 vader를 이용해 평

 


