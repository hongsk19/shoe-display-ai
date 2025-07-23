
def optimize_display(df, max_shelf_space=50):
    # 1. 진열 수량 계산
    total_priority = df['priority'].sum()
    df['display_qty'] = (df['priority'] / total_priority * max_shelf_space).round().astype(int)

    # 2. 추천 위치 자동 생성 (길이 정확히 맞춤)
    zones = ['앞쪽', '중간', '뒤쪽']
    recommended_zone = [zones[i % len(zones)] for i in range(len(df))]  # ✅ 오류 없이 리스트 길이 맞춤
    df['recommended_zone'] = recommended_zone

    return df
