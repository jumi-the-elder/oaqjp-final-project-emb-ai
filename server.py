''' This function will run the emotion detector function as web app
'''
# import the needed stuff from Flask and the emotion detector
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_d():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows predominant emotion.
    '''
    # Get the text from the request 
    text_to_analyse = request.args.get('text', '')  
    # Call the emotion detector function with the text 
    result = emotion_detector(text_to_analyse)
    #return the result of the analysis
    return("For the given statement, the system response is ", result)
    

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="127.0.0.1", port=5000)
