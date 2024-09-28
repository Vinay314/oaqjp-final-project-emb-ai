from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import detect_emotion, extract_emotions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    # Get the statement from the form submission
    statement = request.form.get('statement')

    # Detect emotions in the given statement
    emotion_response = detect_emotion(statement)
    
    if emotion_response:
        # Extract emotions
        emotions = extract_emotions(emotion_response)
        
        # Format the output as requested
        output = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, "
            f"'joy': {emotions['joy']} and "
            f"'sadness': {emotions['sadness']}. "
            f"The dominant emotion is {emotions['dominant_emotion']}."
        )
        
        return jsonify({'output': output})
    else:
        return jsonify({'output': 'Failed to detect emotions.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
