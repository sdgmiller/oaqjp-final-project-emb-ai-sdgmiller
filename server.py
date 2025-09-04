'''Web app that analyzes input text to determine the dominant emotion being expressed'''

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__,template_folder='templates')

@app.route("/emotionDetector")
def sent_analyzer():
    '''Queries the emotion detection REST API.'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is not None:
        return f"For the given  statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and \
        'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

    return "Invalid text! Please try again!"



@app.route("/")
def render_index_page():
    '''Renders the interface for the web app.'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
