# HARM - AI-powered YouTube Video Classifier

HARM, a ThinkBeyondExams intern team, aims to expand the world of AI with a tool that classifies YouTube videos into educational and non-educational categories. If a video is educational, it further classifies it into specific subjects based on thumbnails and titles.

## Problem Statement (Theme: YouTube video classification)
A) Given a YouTube video:
1. Determine if it is an educational video or not.
2. Determine which category or subcategory of BeyondExams it would belong to.

B) Accuracy: 90% on a custom dataset that will be provided after proof of concept.
C) Should be able to run in near-real-time on a server.

## Tech Stack and Tools
```
bash
scikit-learn
bokeh
chime
matplotlib
nltk
numpy
pandas
Pillow
pytube
requests
scikit_image
stqdm
streamlit
streamlit_player
toml
youtube_search_python
scrapetube
youtube-dl
tensorflow
keras
ludwig
```

## Implementation
- Built a web application that takes a YouTube video URL as input and classifies the video.
- Created a dataset generation script to generate required datasets.
- Developed model scripts to run on the generated datasets.
- Focused on enhancing the user experience and marketing the website for broader reach.

## Live Demo and Video Demo
[Demo Link](https://huggingface.co/spaces/HarshulNanda/HARM_ML_web_app)  
[Video Demo Link](https://www.youtube.com/watch?v=P49BkpF17ts)  
[Twilio Demo Link](https://drive.google.com/file/d/1_QmGaWxVaXT2-Hu81Jb2g7Hk4PX9g_Le/view?usp=share_link)

## Ideation Stage Evaluation Feedback
- Updated the README.md file as per guidelines.
- Edited a new demo video for the project.

## Challenges Faced
- No significant problems encountered so far; everything is progressing as planned.

## Twilio Integration
- Users can get channel statistics (custom number of top videos) by entering any video link from the channel. The statistics include title, description, original category, educational status, and predicted category. If dataset generation takes time, users will be notified via Twilio.

## Project Members and Contributions
1. [**Harshul Nanda**](https://www.linkedin.com/in/harshulnanda/) - Web hosting, Image and Text Dataset Generation
2. [**Abhijeet Saroha**](https://www.linkedin.com/in/abhijeet-saroha-a19031229/) - Streamlit and Web Development
3. [**Rishabh Sagar**](https://www.linkedin.com/in/rishabh-sagar-1b0b74229/) - Image processing and Image classification model
4. [**Mayank Arora**](https://www.linkedin.com/in/mayank-arora-24713322a/) - Textual data processing and Text classification model

## Unique Features
- Predicts if a YouTube video is educational or non-educational based on the URL.
- Provides category and sub-category predictions for educational videos, with probability percentage bar graphs.
- Offers channel statistics in a downloadable dataframe format.
- Allows users to search for videos and get predictions for each video based on search keywords.
- Analyzes and predicts the category for videos in a YouTube playlist.
- Determines the percentage of educational content in a video based on subtitles.

## How to Run the Project
1. Clone the repository:
```
git clone https://github.com/repository_invitations/195771281/accept
```
2. Navigate to the project directory:
```
cd HARM---AI-powered-YouTube-Video-Classifier
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Run the Streamlit app:
```
streamlit run app.py
```
5. Access the web app in your browser at http://localhost:8501.

For more detailed instructions, refer to the documentation in the repository.

## Contact
For any queries or support, please reach out to the project members through their LinkedIn profiles listed above.
