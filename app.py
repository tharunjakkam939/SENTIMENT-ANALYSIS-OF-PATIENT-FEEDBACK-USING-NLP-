from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from datetime import datetime
import json
import os

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

app = Flask(__name__)

class PatientFeedbackAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.feedback_history = []
        
    def preprocess_text(self, text):
        """Clean and preprocess the text"""
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and len(token) > 2]
        return ' '.join(tokens)
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of the given text"""
        # Get VADER sentiment scores
        scores = self.analyzer.polarity_scores(text)
        
        # Determine overall sentiment
        if scores['compound'] >= 0.05:
            sentiment = 'Positive'
            color = '#4CAF50'
        elif scores['compound'] <= -0.05:
            sentiment = 'Negative'
            color = '#F44336'
        else:
            sentiment = 'Neutral'
            color = '#FF9800'
        
        # Extract key phrases (simple keyword extraction)
        processed_text = self.preprocess_text(text)
        key_phrases = self.extract_key_phrases(processed_text)
        
        analysis_result = {
            'sentiment': sentiment,
            'confidence': abs(scores['compound']),
            'scores': {
                'positive': scores['pos'],
                'negative': scores['neg'],
                'neutral': scores['neu'],
                'compound': scores['compound']
            },
            'color': color,
            'key_phrases': key_phrases,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return analysis_result
    
    def extract_key_phrases(self, text):
        """Extract key phrases from preprocessed text"""
        words = text.split()
        # Simple frequency-based key phrase extraction
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Get top 5 most frequent words as key phrases
        key_phrases = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        return [phrase[0] for phrase in key_phrases if phrase[1] > 1]
    
    def add_to_history(self, feedback, analysis):
        """Add feedback and analysis to history"""
        entry = {
            'id': len(self.feedback_history) + 1,
            'feedback': feedback,
            'analysis': analysis,
            'timestamp': analysis['timestamp']
        }
        self.feedback_history.append(entry)
        
        # Keep only last 50 entries
        if len(self.feedback_history) > 50:
            self.feedback_history = self.feedback_history[-50:]
    
    def get_statistics(self):
        """Get overall statistics"""
        if not self.feedback_history:
            return {
                'total_feedback': 0,
                'positive_count': 0,
                'negative_count': 0,
                'neutral_count': 0,
                'avg_confidence': 0
            }
        
        total = len(self.feedback_history)
        positive = sum(1 for entry in self.feedback_history if entry['analysis']['sentiment'] == 'Positive')
        negative = sum(1 for entry in self.feedback_history if entry['analysis']['sentiment'] == 'Negative')
        neutral = sum(1 for entry in self.feedback_history if entry['analysis']['sentiment'] == 'Neutral')
        avg_confidence = sum(entry['analysis']['confidence'] for entry in self.feedback_history) / total
        
        return {
            'total_feedback': total,
            'positive_count': positive,
            'negative_count': negative,
            'neutral_count': neutral,
            'positive_percentage': round((positive / total) * 100, 1),
            'negative_percentage': round((negative / total) * 100, 1),
            'neutral_percentage': round((neutral / total) * 100, 1),
            'avg_confidence': round(avg_confidence, 3)
        }

# Initialize the analyzer
analyzer = PatientFeedbackAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_feedback():
    try:
        data = request.get_json()
        feedback = data.get('feedback', '').strip()
        
        if not feedback:
            return jsonify({'error': 'Please provide feedback text'}), 400
        
        # Analyze sentiment
        analysis = analyzer.analyze_sentiment(feedback)
        
        # Add to history
        analyzer.add_to_history(feedback, analysis)
        
        return jsonify({
            'success': True,
            'analysis': analysis
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def get_history():
    try:
        return jsonify({
            'success': True,
            'history': analyzer.feedback_history,
            'statistics': analyzer.get_statistics()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/statistics')
def get_statistics():
    try:
        return jsonify({
            'success': True,
            'statistics': analyzer.get_statistics()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
