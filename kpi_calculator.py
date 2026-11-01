"""Calculates key sales KPIs from cleaned CRM data."""
def calculate_kpis(df):
    total_leads = len(df)
    closed_won = df[df['deal_stage'] == 'Closed Won']
    conversion_rate = len(closed_won) / total_leads if total_leads else 0

    avg_deal_size = closed_won['deal_size'].mean() if not closed_won.empty else 0

    # Deal velocity: average days from created to closed, for won deals only
    velocity_days = (closed_won['closed_date'] - closed_won['created_date']).dt.days
    avg_velocity = velocity_days.mean() if not closed_won.empty else 0

    return {
        'Total Leads': total_leads,
        'Conversion Rate': round(conversion_rate, 2),
        'Average Deal Size': round(avg_deal_size, 2),
        'Average Deal Velocity (days)': int(avg_velocity)
    }
