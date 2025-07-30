import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Based on the status code 200 return the normal result
    # or return None. Except for empty input, the watson EmotionPredict
    # always a result and mostly it is "joy" even on random characters.
    # return code 400 could not be provoked.
    # I assume that today, 2y after release of the course the function behind the url
    # is fake and reacts only on the given word patterns, see the test suite.
    if response.status_code == 200: 
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': max(emotions, key=emotions.get)
        }
    else:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return result

