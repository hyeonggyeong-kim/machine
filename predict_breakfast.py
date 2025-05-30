import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. 데이터 불러오기
df = pd.read_csv("breakfast_data_sample.csv")  # 파일 이름 바꿔도 OK

# 2. Label Encoding (문자형 → 숫자형)
label_cols = ['식단', '날씨', '요일']
encoders = {}
for col in label_cols:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

# 3. 입력 변수 / 타겟 변수 설정
X = df[['식단', '잔반량', '선호도', '날씨', '공휴일', '요일']]
y = df['식사준비량']

# 4. 학습 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 모델 학습
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. 예측 및 평가
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"[평가] 평균 절대 오차(MAE): {mae:.2f}")

# 7. 새로운 입력값으로 예측 (예시)
sample_input = {
    '식단': ['계란국'],
    '잔반량': [2.3],
    '선호도': [4.1],
    '날씨': ['맑음'],
    '공휴일': [0],
    '요일': ['화']
}
sample_df = pd.DataFrame(sample_input)

# 8. 입력값 인코딩 처리
for col in label_cols:
    sample_df[col] = encoders[col].transform(sample_df[col])

# 9. 예측 실행
predicted_quantity = model.predict(sample_df)[0]
print(f"[예측 결과] 예상 식사 준비량: {predicted_quantity:.1f} 인분")
