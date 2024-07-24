import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

def fetch_lotto_data(start_draw=1, end_draw=None):
    base_url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    data = []

    # 최신 회차 번호 가져오기
    response = requests.get("https://www.dhlottery.co.kr/common.do?method=main")
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_draw = int(soup.select_one('strong.win_num').text.strip())

    # end_draw가 지정되지 않았다면 최신 회차를 사용
    if end_draw is None:
        end_draw = latest_draw
    
    # start_draw가 1보다 작으면 1로 설정
    start_draw = max(1, start_draw)
    
    # end_draw가 최신 회차보다 크면 최신 회차로 설정
    end_draw = min(end_draw, latest_draw)

    print(f"{start_draw}회차부터 {end_draw}회차까지의 데이터를 가져옵니다.")

    for draw in range(start_draw, end_draw + 1):
        url = base_url + str(draw)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        numbers = soup.select('span.ball_645')
        if not numbers:
            print(f"회차 {draw}의 데이터를 찾을 수 없습니다.")
            continue

        draw_numbers = [int(num.text) for num in numbers]
        data.append([draw] + draw_numbers)
        
        print(f"회차 {draw} 데이터 추출 완료")
        time.sleep(1)  # 서버 부하를 줄이기 위한 대기 시간

    columns = ['회차', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'bonus']
    df = pd.DataFrame(data, columns=columns)
    return df

# 사용 예시:
# 1. 최근 100회차 데이터 가져오기
lotto_df = fetch_lotto_data(start_draw=None, end_draw=None)

# 2. 특정 범위의 회차 데이터 가져오기 (예: 800회차부터 900회차까지)
# lotto_df = fetch_lotto_data(start_draw=800, end_draw=900)

print(lotto_df.head())

# CSV 파일로 저장
lotto_df.to_csv('lotto_data.csv', index=False)
print("데이터가 lotto_data.csv 파일로 저장되었습니다.")