"""Server for emotion detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def server_emotion_detection():
    """Module to return emotion analysis"""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid Text! Please try again!"

    output = f"For the given statement, the system response is 'anger': {anger}, "
    output2 = f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    output3 = f"The dominant emotion is {dominant_emotion}."

    return output + output2 + output3

@app.route("/")
def render_index_page():
    """Runs server"""

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
