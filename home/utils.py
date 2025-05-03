from google.cloud import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

def detect_intent_texts(project_id, session_id, texts, language_code='id'):
    """Mengirim teks ke Dialogflow dan mendapatkan respons"""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=texts, language_code=language_code)
    query_input = dialogflow.QueryInput(text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except InvalidArgument:
        raise ValueError("Invalid Argument Exception")
