
def optimize_display(df, max_shelf_space=50):
    total_priority = df['priority'].sum()
    df['display_qty'] = (df['priority'] / total_priority * max_shelf_space).round().astype(int)
    df['recommended_zone'] = ['앞쪽', '중간', '뒤쪽'] * (len(df) // 3 + 1)
    return df
