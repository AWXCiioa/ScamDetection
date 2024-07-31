from flask import Flask, render_template, request, session, jsonify
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import PyPDF2

app = Flask(__name__)
app.secret_key = 'thisismykey'

# Load the model
with open("soft_voting_classifier.pkl", 'rb') as file:
    sv_classifier = pickle.load(file)

# Load the TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'http\S+', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    cleaned_text = ' '.join(stemmed_words)
    return cleaned_text

def predict_fake_or_real(text):
    print("Original text:", text)
    cleaned_text = clean_text(text)
    print("Cleaned text:", cleaned_text)
    text_tfidf = tfidf_vectorizer.transform([cleaned_text])
    prediction = sv_classifier.predict(text_tfidf)
    print("Raw prediction:", prediction)
    if prediction[0] in ['spam', 'smishing']:
        numeric_prediction = 1
    else:
        numeric_prediction = 0
    print("Numeric prediction:", numeric_prediction)
    return numeric_prediction

@app.route('/')
def index():
    theme = session.get('theme', 'default')
    return render_template('index.html', theme=theme)

@app.route('/home')
def home():
    theme = session.get('theme', 'default')
    return render_template('index.html', theme=theme)

@app.route('/about')
def about():
    theme = session.get('theme', 'default')
    return render_template('about.html', theme=theme)

@app.route('/scam', methods=['POST'])
def detect_scam():
    if request.method == 'POST':
        if 'fileUpload' in request.files:
            file = request.files['fileUpload']
            if file.filename.endswith('.pdf'):
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                text = ''
                for page_num in range(num_pages):
                    text += pdf_reader.pages[page_num].extract_text()
            else:
                text = file.read().decode('utf-8')
            if not text:
                return jsonify({"message": "Please provide input text."})
            prediction = predict_fake_or_real(text)
            if prediction == 1:
                return jsonify({"message": "This message (article/news) is a Scam Text."})
            else:
                return jsonify({"message": "This message (article/news) is a Real Text."})

@app.route('/text', methods=['POST'])
def text():
    if request.method == 'POST':
        user_input = request.form['textInput']
        prediction = predict_fake_or_real(user_input)
        message = "This message (article/news) is a scam Text." if prediction == 1 else "This message (article/news) is a Real Text."
        print("Returning message:", message)
        return jsonify({"message": message})

@app.route('/apply_theme', methods=['POST'])
def apply_theme():
    selected_theme = request.form['theme']
    session['theme'] = selected_theme
    return jsonify(status='success')

if __name__ == '__main__':
    app.run(debug=True)
