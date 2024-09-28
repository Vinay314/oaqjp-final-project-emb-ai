from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import detect_emotion, extract_emotions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    # Get the statement from the form submission
    statement = request.form.get('statement')

    # Check if the statement is empty
    if not statement.strip():  # Check for blank input
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    # Detect emotions in the given statement
    emotion_response = detect_emotion(statement)
    
    if emotion_response:
        # Extract emotions
        emotions = extract_emotions(emotion_response)

        # Check if dominant emotion is None
        if emotions['dominant_emotion'] is None:
            return jsonify({'output': 'Invalid text! Please try again!'}), 400
        
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
