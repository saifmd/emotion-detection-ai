import requests, json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    json_response = json.loads(response.text)
    overall_emotion = json_response["emotionPredictions"][0]["emotion"]
    anger_score = overall_emotion['anger']
    disgust_score = overall_emotion['disgust']
    fear_score = overall_emotion['fear']
    joy_score = overall_emotion['joy']
    sadness_score = overall_emotion['sadness']
    dominant_emotion = max(overall_emotion, key=overall_emotion.get)
    formatted_response = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
    return formatted_response
