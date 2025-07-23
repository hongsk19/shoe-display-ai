
def optimize_display(df, max_shelf_space=50):
    total_priority = df['priority'].sum()
    df['display_qty'] = (df['priority'] / total_priority * max_shelf_space).round().astype(int)

    # 🔧 추천 위치 자동 분배: 길이 정확히 맞춤
    zones = ['앞쪽', '중간', '뒤쪽']
    repeated_zones = [zones[i % len(zones)] for i in range(len(df))]  # ✅ 정확한 길이 보장
    df['recommended_zone'] = repeated_zones

    return df
