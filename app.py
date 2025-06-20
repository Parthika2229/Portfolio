import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Parthika Battala | Portfolio", layout="wide")

# Background and CSS styles
st.markdown("""
    <style>
    .stApp {
        background-color: #C5B4D8; /* Light purple for data portfolio feel */
        font-family: 'Segoe UI', sans-serif;
        padding: 0 2rem;
        color: #1e1e2f;
    }
    .main-header {
        font-size: 40px;
        font-weight: 700;
        color: #1e1e2f;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 20px;
        color: #3d3d5c;
        margin-top: -10px;
        font-weight: 500;
    }
    h2 {
        color: #2e4053;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("Portfolio Menu")
page = st.sidebar.radio("Navigate to:", ["About Me", "Skills", "Projects", "Education", "Contact"])

# Page Header
st.markdown("<div class='main-header'>Hello, I'm Parthika Battala</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Data Analytics | Python | Power BI | Machine Learning | Insight-Driven Decisions</div>", unsafe_allow_html=True)
st.markdown("---")

# Display content based on selection
if page == "About Me":
    st.header("About Me")
    st.write("""
        I am an aspiring Data Analyst with a strong foundation in analytical modeling, data pipeline optimization, and dashboard development.
        Experienced in Python, SQL, Power BI, and Tableau to drive insight generation and process efficiency. Proven ability to deliver
        data-driven solutions across domains including financial reporting, healthcare imaging, and cybersecurity.
        Currently pursuing a Master’s in Data Science, with a focus on advanced analytics, machine learning, and real-world AI applications.
    """)

elif page == "Skills":
    st.header("Skills")
    st.markdown("""
        **Languages & Programming**  
        Python, SQL, C  
        
        **Data Analysis & Integration**  
        Jupyter Notebooks, ETL (Extract, Transform, Load), Data Cleaning, Data Wrangling  
        
        **Data Visualization**  
        Tableau, Microsoft Excel, Power BI  
        
        **Machine Learning**  
        Regression, Decision Trees, Random Forest, Clustering, Model Evaluation, Feature Engineering, Data Preprocessing, PCA  
        
        **Tools & Services**  
        Git, Microsoft Office, Jupyter, RStudio, VS Code, JIRA, Project Management, Hadoop  
        
        **Techniques & Concepts**  
        EDA, KPI Monitoring, Feature Optimization, Anomaly Detection, Dashboarding, Reporting Automation
    """)

elif page == "Projects":
    st.header("Projects")
    st.markdown("""
        **AI-Powered Pneumonia Detection with Explainable Deep Learning**  
        Tools: Python, PyTorch, TensorFlow, Grad-CAM  
        - Built a deep learning solution classifying pneumonia from X-rays using ResNet18, EfficientNet-B0, and DenseNet121.  
        - Applied Grad-CAM for interpretability. Achieved 88.3% accuracy and 0.89 F1-score.  

        **Sales Analysis Dashboard**  
        Tools: Power BI, Excel  
        - Designed a Power BI dashboard that uncovered KPIs and improved insight-driven decisions by 20%.  

        **Employee Performance Report**  
        Tools: Tableau  
        - Analyzed employee metrics and improved operational insights by 25%.  

        **Detection of Malicious Web Attacks**  
        Tools: Python, scikit-learn  
        - Developed a machine learning model to detect malicious URLs with a 95% detection rate.
    """)

elif page == "Education":
    st.header("Education")
    st.markdown("""
        **Master’s in Data Science**  
        Lewis University, Romeoville, IL (Aug 2023 – May 2025) | GPA: 3.75/4.00  
        Coursework: Relational Databases, Data Mining, Cloud Analytics, Predictive Analytics, Big Data, Machine Learning, Data Visualization  

        **B.Tech in Electronics and Communication**  
        Anurag Group of Institutions, Hyderabad (Aug 2019 – May 2023) | CGPA: 8.7/10  
        Coursework: Python, DBMS, IoT, Software Engineering, Embedded Systems
    """)

elif page == "Contact":
    st.header("Contact")
    st.markdown("""
        - Email: [parthikabattala@gmail.com](mailto:parthikabattala@gmail.com)  
        - GitHub: [github.com/Parthika2229](https://github.com/Parthika2229)  
        - LinkedIn: [linkedin.com/in/parthikabattala](https://www.linkedin.com/in/parthikabattala/)
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 Parthika Battala • Built with Streamlit", unsafe_allow_html=True)
