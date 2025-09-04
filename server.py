"""Executing this function initiates the application of emotion
detector to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detection():
    """A function that gets text_to_analyze and gives backthe emotin score"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text, Please try again"

    # extrant other emotions and values
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    dominant_emotion = response["dominant_emotion"]

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render to Html page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
