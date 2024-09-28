import unittest
from EmotionDetection.emotion_detection import extract_emotions, detect_emotion

class TestEmotionDetection(unittest.TestCase):
    
    def setUp(self):
        """Set up test data"""
        # Create a list of test cases with statements and expected dominant emotions
        self.test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

    def test_emotion_detection(self):
        """Test the emotion detection functionality"""
        for statement, expected_dominant in self.test_cases:
            with self.subTest(statement=statement):
                # Call the detect_emotion function and simulate a response
                emotion_response = detect_emotion(statement)
                # Extract emotions using the existing function
                emotions = extract_emotions(emotion_response)
                # Check if the dominant emotion matches the expected dominant emotion
                self.assertEqual(emotions['dominant_emotion'], expected_dominant, 
                                 f"Failed for statement: {statement}. Expected: {expected_dominant}, Got: {emotions['dominant_emotion']}")

if __name__ == '__main__':
    unittest.main()
