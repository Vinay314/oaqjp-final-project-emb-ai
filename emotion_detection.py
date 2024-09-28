import requests

# URL and headers for the emotion detection API
url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {
    'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
    'Content-Type': 'application/json'
}

# Function to detect emotions in a given text
def emotion_detector(text):
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
            return result
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Get text input from the user
    text_to_analyze = input("Enter the text you want to analyze for emotions: ")

    # Detect emotion in the text
    emotions = emotion_detector(text_to_analyze)
    
    # Print the result
    if emotions:
        print("Detected emotions:", emotions)

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
