from youtubesearchpython import Video, ResultMode
from colors import colorOf, dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import pickle
import warnings
warnings.filterwarnings("ignore")

def predictCategoryFor(url):
    try:

        video = Video.getInfo(url, mode = ResultMode.json)

        text = [video["title"] + " " + video["description"]]
        
        categories = sorted(list(dataset.keys()))

        # education_model = pickle.load(open("./models/educated_model.pkl", "rb"))
        # education_prediction = education_model.predict(text)[0]
        
        education_classifier = pickle.load(open("./models/ludwig_edu.pkl", "rb"))
        text_to_predict = pd.DataFrame({
            "text": [
                text,
            ]
        })
        edu_pred, _ = education_classifier.predict(text_to_predict)
        edu_pred = list(edu_pred.category_predictions)[0]
        education_prediction = edu_pred

        if education_prediction == "Education":
            
            category_classifier = pickle.load(open("./models/ludwig_cat_final.pkl", "rb"))
            pred, _ = category_classifier.predict(text_to_predict)
            pred = list(pred.category_predictions)[0]
            category_prediction = pred
            
            sub_cat_clf = pickle.load(open(f"./models/{category_prediction.lower().replace(' ', '_')}_model.pkl", "rb"))
            sub_cat_pred = sub_cat_clf.predict_proba(text)[0]
            sub_cat_pred *= 100
            subs = sorted(dataset[category_prediction])

            return ("Educational", category_prediction, subs, sub_cat_pred)
        
        else:

            return ("Non Educational", "", [], [])
    
    except:
        return ("There must be an error in getting the title and description of the video.", "", [], [])


