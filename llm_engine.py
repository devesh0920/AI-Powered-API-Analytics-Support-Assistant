from openai import OpenAI

client = OpenAI()

def generate_insights(client_data):
    prompt = f"""
    Analyze this API usage:
    Error Rate: {client_data['error_flag']}
    Avg Response Time: {client_data['response_time']}
    
    Give root cause and recommendations.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content