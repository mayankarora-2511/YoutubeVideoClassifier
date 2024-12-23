from youtubesearchpython import Transcript, Video, ResultMode
import pickle
from stqdm import stqdm
import pandas as pd

def eduContentPrediction(url):
    segments = Transcript.get(url)["segments"]
    E = 0
    NonE = 0
    # education_model = pickle.load(open("./models/educated_model.pkl", "rb"))
    
    education_classifier = pickle.load(open("./models/ludwig_edu.pkl", "rb"))

    timer = stqdm(segments)

    for segment in timer:
        timer.set_description("☕️ Have a coffee, while we apply our model on the video transcript.  ")
        text_to_predict = pd.DataFrame({
            "text": [
                str(segment["text"]),
            ]
        })
        edu_pred, _ = education_classifier.predict(text_to_predict)
        text_prediction = list(edu_pred.category_predictions)[0]
        # text_prediction = education_model.predict(text)[0]
        if text_prediction == "Education":
            E += 1
        else:
            NonE += 1

    return "The {:.2f}% portion of this video is educational.".format(E*100/(E+NonE))