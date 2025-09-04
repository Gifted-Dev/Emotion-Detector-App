"""This module peforms sentiment analysis based on emotions"""

import json
import requests


def emotion_detector(text_to_analyse):
    """This function takes in a text, and perfomrs sentiment analysis"""

    # Define the URL for the sentiment analysis API
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=5)

    if not response:
        return None

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # create a new dictionary
    results = {}

    # check status code and assign key:values
    if response.status_code == 200:
        results = formatted_response["emotionPredictions"][0]["emotion"]
    elif response.status_code == 400:
        result_keys = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotin"]
        results = {key: None for key in result_keys}

    # get the dominant_emotion
    dominant_emotion = max(results, key=results.get)

    # add the dominant_emotion to the dictionary
    results["dominant_emotion"] = dominant_emotion

    return results
