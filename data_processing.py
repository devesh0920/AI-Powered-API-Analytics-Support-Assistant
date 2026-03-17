import pandas as pd

def process_logs(data):
    df = pd.DataFrame(data)
    
    df['error_flag'] = df['status_code'].apply(lambda x: 1 if x != 200 else 0)
    
    summary = df.groupby('client_id').agg({
        'error_flag': 'mean',
        'response_time': 'mean'
    }).reset_index()
    
    return summary