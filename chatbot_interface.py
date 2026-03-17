from llm_engine import generate_insights


def chatbot_query(query, client_data):
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Query must be a non-empty string.")

    if not isinstance(client_data, dict):
        raise ValueError("client_data must be a dictionary.")

    context = generate_insights(client_data)

    return (
        f"User Query: {query.strip()}\n\n"
        "AI Response:\n"
        f"Based on the API analytics for this client, {context}"
    )
