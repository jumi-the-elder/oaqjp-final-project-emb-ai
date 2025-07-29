from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Example stub for your emotion detection function
def emotion_detector(text):
    # Placeholder logic — replace with actual model or algorithm
    emotions = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }
    return emotions.get(text, "unknown")

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        statement = "I am glad this happened"
        self.assertEqual(emotion_detector(statement), "joy")

    def test_anger(self):
        statement = "I am really mad about this"
        self.assertEqual(emotion_detector(statement), "anger")

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        self.assertEqual(emotion_detector(statement), "disgust")

    def test_sadness(self):
        statement = "I am so sad about this"
        self.assertEqual(emotion_detector(statement), "sadness")

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        self.assertEqual(emotion_detector(statement), "fear")

if __name__ == "__main__":
    unittest.main()