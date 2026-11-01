"""Generates simulated CRM data with realistic errors and duplicates."""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data(num_rows=100):
    np.random.seed(42)

    lead_ids = np.arange(1000, 1000 + num_rows)
    deal_stages = ['Qualified', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']
    sources = ['Web', 'Email', 'Phone', 'Referral', 'Ad']

    data = {
        'lead_id': np.random.choice(lead_ids, size=num_rows),
        'lead_source': np.random.choice(sources, size=num_rows),
        'deal_stage': np.random.choice(deal_stages, size=num_rows),
        'deal_size': np.random.randint(500, 15000, size=num_rows),
        'created_date': [datetime.now() - timedelta(days=int(np.random.randint(1, 90))) for _ in range(num_rows)],
    }

    df = pd.DataFrame(data)

    # Only closed deals have a closed_date, and it falls between created_date and today
    now = datetime.now()
    is_closed = df['deal_stage'].isin(['Closed Won', 'Closed Lost'])
    df['closed_date'] = [
        created + timedelta(days=int(np.random.randint(0, (now - created).days + 1))) if closed else pd.NaT
        for created, closed in zip(df['created_date'], is_closed)
    ]

    # Randomly insert some nulls
    for col in ['lead_source', 'deal_stage']:
        df.loc[df.sample(frac=0.1).index, col] = np.nan

    return df
