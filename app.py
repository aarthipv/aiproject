from flask import Flask, render_template, request, jsonify
from models.grammar_model import correct_grammar
#from models.plagiarism_model import check_plagiarism_with_sbert  # Make sure this is the correct import
from models.suggestion_model import get_suggestions
from models.enhancement_model import enhance_content

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')  # Assuming you have an index.html in the templates folder


# Route for Grammar Correction
@app.route('/correct-grammar', methods=['POST'])
def correct_grammar_route():
    text = request.json.get('text')
    corrected_text = correct_grammar(text)
    return jsonify({'corrected_text': corrected_text})

# Route for Suggestions
@app.route('/get-suggestions', methods=['POST'])
def get_suggestions_route():
    text = request.json.get('text')
    suggestions = get_suggestions(text)
    return jsonify({'suggestions': suggestions})

# Route for Content Enhancement
@app.route('/enhance-content', methods=['POST'])
def enhance_content_route():
    text = request.json.get('text')
    enhanced_text = enhance_content(text)
    return jsonify({'enhanced_text': enhanced_text})


if __name__ == '__main__':
    app.run(debug=True)
