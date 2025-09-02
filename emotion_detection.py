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
    formatted_response = json.loads(response.text)

    print(type(formatted_response))
    anger = formatted_response["emotionPredictions"]["anger"]
    disgust = formatted_response['emotionPredictions']['disgust']
    fear = formatted_response['emotionPredictions']['fear']
    joy = formatted_response['emotionPredictions']['joy']
    sadness = formatted_response['emotionPredictions']['sadness']

    return {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}

  



