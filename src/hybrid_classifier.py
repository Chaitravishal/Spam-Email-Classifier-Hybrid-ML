# -------------------------------------------
# HYBRID SPAM EMAIL CLASSIFIER (NB + SVM)
# -------------------------------------------

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# Download NLTK data if not installed
nltk.download('punkt')
nltk.download('stopwords')

# ---------------------------
# LOAD DATASET
# ---------------------------
df = pd.read_csv("data/completeSpamAssassin.csv", encoding='latin1')
df = df.rename(columns={'Label':'label', 'Body':'message'})
df = df[['label','message']].dropna()

# ---------------------------
# TEXT PREPROCESSING
# ---------------------------
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = str(text).lower()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalnum() and w not in stop_words]
    return " ".join(tokens)

df['clean_text'] = df['message'].apply(preprocess_text)

# ---------------------------
# FEATURE EXTRACTION
# ---------------------------
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['clean_text'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# TRAIN MODELS
# ---------------------------
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(X_train, y_train)

# ---------------------------
# HYBRID PREDICTION FUNCTION
# ---------------------------
def classify_email(text):
    processed = preprocess_text(text)
    vector = tfidf.transform([processed])
    
    nb_result = nb_model.predict(vector)[0]
    svm_result = svm_model.predict(vector)[0]
    hybrid_result = 1 if nb_result == 1 or svm_result == 1 else 0
    
    print("\n======================================")
    print(f"EMAIL:\n{text}")
    print("--------------------------------------")
    print(f"Naive Bayes → {'SPAM' if nb_result == 1 else 'NOT SPAM'}")
    print(f"SVM         → {'SPAM' if svm_result == 1 else 'NOT SPAM'}")
    print(f"Hybrid      → {'SPAM' if hybrid_result == 1 else 'NOT SPAM'}")
    print("======================================\n")

# ---------------------------
# TEST SAMPLE EMAILS
# ---------------------------
if __name__ == "__main__":
    sample_emails = [
        "Win a free iPhone now! Click here to claim.",
        "Dear student, your exam timetable is available on the portal.",
        "Limited offer! Buy sunglasses today!",
        "Hey, let's meet for lunch tomorrow.",
        "Your bank account has suspicious login attempts."
    ]

    for email in sample_emails:
        classify_email(email)
