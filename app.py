from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # Sample data to pass into the HTML template
    user_name = "Alex"
    skills_list = ["Python", "Flask", "HTML", "CSS", "SQL"]
    
    # Renders the index.html template and injects variables
    return render_template('index.html', name=user_name, skills=skills_list)

if __name__ == '__main__':
    # Runs the app locally on http://127.0.0.1:5000
    app.run(debug=True)
