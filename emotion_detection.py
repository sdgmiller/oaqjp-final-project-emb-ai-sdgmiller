import requests
import json


def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = dict(json.loads(response.text))

    emotions = {}
    
    anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    emotions["anger"]=anger

    disgust = formatted_response['emotionPredictions'][0]["emotion"]['disgust']
    emotions["digust"]=disgust

    fear = formatted_response['emotionPredictions'][0]["emotion"]['fear']
    emotions["fear"]=fear

    joy = formatted_response['emotionPredictions'][0]["emotion"]['joy']
    emotions["joy"]=joy

    sadness = formatted_response['emotionPredictions'][0]["emotion"]['sadness']
    emotions["sadness"]=sadness

    sorted_emotions = sorted(emotions, key=emotions.get)

    dominant_emotion = sorted_emotions[-1]

    return {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness,'dominant_emotion':dominant_emotion}
    

  



