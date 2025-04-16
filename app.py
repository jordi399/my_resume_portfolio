from flask import Flask, render_template, request, redirect, url_for, flash, abort
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



projects = [
    {
        'title': 'Lead Scoring Model – Maruti Suzuki',
        'slug': 'lead-scoring',
        'description': 'Classify new car enquiries into purchase likelihood.',
        'tech': 'LightGBM, Python, Feature Engineering, Model Explainability',
        'image': 'lead_scoring.png',
        'details': '''
        Developed a lead scoring model to classify new car enquiries into high, medium, and low purchase intent. Used LightGBM on large binary and multi-category feature space. Helped prioritize dealership follow-ups and improve sales conversion rate.
        '''
    },
    {
        'title': 'Marketing Mix Modeling – Walmart Auto',
        'slug': 'mmm-walmart',
        'description': 'Optimize marketing spend across media for Walmart automotive.',
        'tech': 'Ridge Regression, Adstock, S-Curves, Python',
        'image': 'mmm_walmart_media.png',
        'details': '''
        Built a Marketing Mix Model to estimate channel-wise contribution to sales. Modeled ad saturation using S-curves and decay via adstock transformation. Helped marketing team reallocate budgets across paid media channels to maximize ROAs.
        '''
    },
    {
        'title': 'True Value Car Evaluation Model – Maruti Suzuki',
        'slug': 'true-value',
        'description': 'Identify Maruti customers likely to sell/exchange cars.',
        'tech': 'XGBoost, Python, CRM Integration',
        'image': 'true_value.jpg',
        'details': '''
        Created a classification model to predict which customers are likely to evaluate/sell their cars. Integrated into Maruti CRM to identify leads for True Value used car business, improving Customer Lifetime Value (CLV) of existing customers.
        '''
    },
    {
        'title': 'EV Customer Segmentation – Maruti Suzuki',
        'slug': 'ev-segmentation',
        'description': 'Identify target audience for upcoming electric vehicle launch.',
        'tech': 'KMeans, PCA, Customer Profiling',
        'image': 'ev_segmentation.jpg',
        'details': '''
        Used clustering to segment customers based on behavior and demographics. Helped marketing team identify the most suitable segments for Maruti's EV rollout strategy and tailor campaigns accordingly.
        '''
    }
]

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/projects/<slug>")
def project_detail(slug):
    project = next((p for p in projects if p["slug"] == slug), None)
    if project is None:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = MIMEText(f"Name: {name}\nEmail: {email}\n\n{message}")
        msg["Subject"] = "New Contact Message from Portfolio"
        msg["From"] = "pankajrawat399@gmail.com"
        msg["To"] = "pankajrawat399@gmail.com"

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login("pankajrawat399@gmail.com", "flxlkqessdmuqwos")
                server.send_message(msg)
            return render_template("contact.html", success=True)
        except Exception as e:
            print("Email error:", e)
            flash("Failed to send message. Please try again.", "danger")

    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)