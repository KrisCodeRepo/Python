from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Personalized AI Learning Plan (16 Weeks)', ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True, align='L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

content = [
    {
        "title": "Weeks 1–2: Python Basics & AI Fundamentals",
        "body": (
            "Objective: Transition from Java to Python and grasp foundational AI concepts.\n\n"
            "Topics:\n- Python syntax and libraries (NumPy, pandas, matplotlib)\n"
            "- Introduction to AI, Machine Learning, and Deep Learning\n\n"
            "Resources:\n- Google's Python Class (Free): https://developers.google.com/edu/python\n"
            "- Crash Course AI (YouTube): https://www.youtube.com/playlist?list=PL8dPuuaLjXtOfse2ncvffeelTrqvhrz8H\n"
        )
    },
    {
        "title": "Weeks 3–6: Core Machine Learning",
        "body": (
            "Objective: Understand and implement core ML algorithms.\n\n"
            "Topics:\n- Supervised Learning: Linear Regression, Logistic Regression, Decision Trees, SVM\n"
            "- Unsupervised Learning: K-Means Clustering, PCA\n"
            "- Model Evaluation: Accuracy, Precision, Recall, F1 Score\n\n"
            "Resources:\n- Andrew Ng's Machine Learning (Coursera): https://www.coursera.org/learn/machine-learning\n"
            "- Kaggle Intro to ML: https://www.kaggle.com/learn/intro-to-machine-learning\n"
        )
    },
    {
        "title": "Weeks 7–11: Deep Learning",
        "body": (
            "Objective: Dive into neural networks and deep learning techniques.\n\n"
            "Topics:\n- Neural Networks and Backpropagation\n- CNNs\n- RNNs and LSTMs\n\n"
            "Resources:\n- DeepLearning.AI (Coursera): https://www.coursera.org/specializations/deep-learning\n"
            "- fast.ai Course: https://course.fast.ai/\n"
        )
    },
    {
        "title": "Weeks 12–16: Projects & Specialization",
        "body": (
            "Objective: Apply knowledge through projects and explore areas of interest.\n\n"
            "Projects:\n- Image Classification, Sentiment Analysis, Chatbot Development\n\n"
            "Specializations:\n- NLP, Computer Vision, Generative AI\n\n"
            "Resources:\n- Hugging Face Transformers: https://huggingface.co/learn\n"
            "- Stanford CS231n: http://cs231n.stanford.edu/\n"
        )
    },
    {
        "title": "Notion Template for Tracking Progress",
        "body": (
            "Use this Notion template to organize and monitor your learning:\n"
            "- Learning Hub + by Sam Stoof: https://notis.ai/notion-copilot/templates/learning-hub-plis\n"
        )
    }
]

for section in content:
    pdf.chapter_title(section["title"])
    pdf.chapter_body(section["body"])

pdf.output("AI_Learning_Plan.pdf")
