
import pandas as pd

def optimize_display(df, max_shelf_space=50):
    # 1. priority가 존재하고 숫자인지 확인
    df['priority'] = pd.to_numeric(df['priority'], errors='coerce')  # 문자열 → NaN 처리
    df = df.dropna(subset=['priority'])  # NaN 제거

    # 2. 전체 priority 총합이 0이면 에러 방지
    total_priority = df['priority'].sum()
    if total_priority == 0:
        df['display_qty'] = 0
        df['recommended_zone'] = '중간'
        return df

    # 3. 진열 수량 계산
    df.loc[:, 'display_qty'] = (df['priority'] / total_priority * max_shelf_space).round().astype(int)

    # 4. 추천 위치 생성 (정확히 길이 맞춤)
    zones = ['앞쪽', '중간', '뒤쪽']
    df.loc[:, 'recommended_zone'] = [zones[i % len(zones)] for i in range(len(df))]

    return df
