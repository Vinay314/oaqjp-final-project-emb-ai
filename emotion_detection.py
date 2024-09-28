import requests
import json

# URL and headers for the emotion detection API
url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {
    'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
    'Content-Type': 'application/json'
}

# Function to detect emotions in a given text
def detect_emotion(text):
    # Input JSON for the API request
    input_json = {
        "raw_document": {
            "text": text
        }
    }

    try:
        # Sending POST request to the API
        response = requests.post(url, json=input_json, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            #print("API Response:", json.dumps(result, indent=2))  # Print formatted JSON response for debugging
            return result
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to extract emotions and determine the dominant emotion
# Function to extract emotions and determine the dominant emotion
def extract_emotions(emotion_response):
    # Print the entire response structure for debugging
    #print("Emotion response structure:", json.dumps(emotion_response, indent=2))

    # Extract the first prediction (there could be multiple predictions)
    if 'emotionPredictions' in emotion_response and emotion_response['emotionPredictions']:
        emotions_data = emotion_response['emotionPredictions'][0]['emotion']
    else:
        print("No emotion predictions found.")
        return {}

    # Extract the required emotions
    emotions = {
        'anger': emotions_data.get('anger', 0),
        'disgust': emotions_data.get('disgust', 0),
        'fear': emotions_data.get('fear', 0),
        'joy': emotions_data.get('joy', 0),
        'sadness': emotions_data.get('sadness', 0)
    }
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    # Add the dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    return emotions


# Function to handle the user interaction and detect emotions
def emotion_detector():
    # Get text input from the user
    text_to_analyze = input("Enter the text you want to analyze for emotions: ")

    # Detect emotion in the text
    emotion_response = detect_emotion(text_to_analyze)
    
    if emotion_response:
        # Extract and print the required emotions and the dominant emotion
        emotions = extract_emotions(emotion_response)
        print("Detected emotions and dominant emotion:", emotions)
    else:
        print("Failed to detect emotions.")

# Run the emotion_detector function if the script is executed directly
if __name__ == '__main__':
    emotion_detector()
