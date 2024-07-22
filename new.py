import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 데이터 로드 (예시 데이터, 실제로는 수집된 데이터를 사용해야 함)
data = pd.DataFrame({
    'rainfall': [100, 150, 200, 50, 300],
    'river_level': [2, 3, 4, 1, 5],
    'elevation': [10, 5, 3, 15, 2],
    'flood': [0, 1, 1, 0, 1]
})

# 특성과 목표 변수 분리
X = data[['rainfall', 'river_level', 'elevation']]
y = data['flood']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 생성 및 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 예측
predictions = model.predict(X_test)

# 정확도 평가
accuracy = accuracy_score(y_test, predictions)
print(f"모델 정확도: {accuracy}")

# 새로운 데이터에 대한 침수 예측
new_data = pd.DataFrame({
    'rainfall': [180],
    'river_level': [3.5],
    'elevation': [4]
})

prediction = model.predict(new_data)
print(f"침수 예측 결과: {'침수 위험' if prediction[0] == 1 else '안전'}")