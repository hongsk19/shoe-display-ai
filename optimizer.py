
def optimize_display(df, max_shelf_space=50):
    total_priority = df['priority'].sum()
    df['display_qty'] = (df['priority'] / total_priority * max_shelf_space).round().astype(int)
    
    zones = ['앞쪽', '중간', '뒤쪽']
    repeated_zones = (zones * ((len(df) // len(zones)) + 1))[:len(df)]  # ✅ 정확히 자르기
    df['recommended_zone'] = repeated_zones

    return df
