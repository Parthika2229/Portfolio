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
page = st.sidebar.radio("Navigate to:", ["About Me", "Skills", "Experience", "Projects", "Education", "Contact"])

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
    **Data Analysis & Visualization**  
    Power BI, Tableau, Excel (VLOOKUP, Pivot Tables), Matplotlib, Seaborn

    **Programming & Scripting**  
    Python (Pandas, NumPy, Scikit-learn, Regex), SQL (Joins, CTEs, Window Functions)

    **Machine Learning & Statistics**  
    Regression, Classification, A/B Testing, Hypothesis Testing, Clustering, Data Validation, Data Cleansing

    **Data Engineering & Tools**  
    ETL Pipeline Automation, Jupyter Notebooks, Git, Streamlit, Google Sheets, MS Power Query

    **Cloud Platforms**  
    AWS (S3, Athena, Redshift), Google BigQuery

    **Cybersecurity Concepts & Tools (Basic)**  
    Data Privacy, Google Cloud IAM, Basic Security Logging & Anomaly Monitoring
    """)

elif page == "Experience":
    st.header("Experience")

    st.subheader("Data Analyst Intern | Wayfair, Boston, USA")
    st.write("""
**Tools:** Python, SQL, Pandas, Google Cloud (BigQuery, Cloud Storage), Power BI, Excel, SciPy, Google Cloud IAM  
**Duration:** Apr 2024 – Oct 2024  
- Spearheaded automation of financial reporting pipelines and dashboards, reducing manual effort by 40% while enforcing secure data access protocols.  
- Analyzed key financial metrics and utilized anomaly detection techniques to identify irregular activities and improve data integrity.  
- Collaborated with finance and IT teams to develop forecasting models and predictive analytics solutions, maintaining compliance with internal security standards.  
""")

    st.subheader("Data Reporting Intern | Cognizant, Bengaluru, India")
    st.write("""
**Tools:** Power BI, Python, SQL, Excel  
**Duration:** May 2022 – Jun 2023  
- Spearheaded automation of healthcare KPI reporting using Power BI and Python, reducing manual data preparation time by 40%.  
- Developed and optimized SQL queries for clinical databases to ensure consistent and reliable reports.  
- Implemented data validation and cleansing using Python and Excel, cutting data errors by 30%.  
""")

    st.subheader("Data Insights Intern | ZettaMine Labs, Hyderabad, India")
    st.write("""
**Tools:** Excel, SQL, Power BI, Python  
**Duration:** Nov 2021 – May 2022  
- Designed dashboards to present key business metrics, improving decision-making speed.  
- Cleaned and analyzed large datasets, enhancing forecasting accuracy by 15%.  
- Automated data consolidation and reporting, reducing report generation time by 30%.  
""")

elif page == "Projects":
    st.header("Projects")

    st.subheader("AI-Powered Pneumonia Detection with Explainable Deep Learning")
    st.write("""
    **Tools:** Python, PyTorch, TensorFlow, Grad-CAM  
    - Developed a deep learning-based medical imaging solution to classify pneumonia from chest X-rays using pretrained CNN models including ResNet18, EfficientNet-B0, and DenseNet121.  
    - Preprocessed data from a public chest X-ray dataset, addressed class imbalance using weighted random sampling to improve recall and reduce false negatives.  
    - Implemented Grad-CAM to visualize activated regions in X-rays, enhancing transparency for clinical validation.  
    - Achieved 88.3% accuracy and 0.89 F1-score with ResNet18, suitable for diagnostic decision support systems.  
    """)

    st.subheader("Customer A/B Testing Dashboard")
    st.write("""
    **Tools:** Python, Streamlit, SciPy, Pandas  
    - Developed an interactive web app to allow marketing teams to upload experiment data and automatically run statistical tests (t-tests, chi-square).  
    - Created effect size summaries and visualizations for easy result interpretation by non-technical users.  
    - Improved campaign targeting accuracy by 15% and increased simulated conversion rates.  
    """)

    st.subheader("Social Media Sentiment Analyzer")
    st.write("""
    **Tools:** Python, NLTK, Scikit-learn, Power BI  
    - Built an NLP pipeline using VADER and Logistic Regression to classify Twitter sentiment with 85% accuracy.  
    - Designed Power BI dashboards to visualize sentiment shifts and common themes over time.  
    - Helped marketing teams enhance reputation management and customer feedback response.  
    """)

    st.subheader("Sales Analysis Dashboard")
    st.write("""
    **Tools:** Power BI, Excel  
    - Designed a Power BI dashboard that uncovered KPIs and improved insight-driven decisions by 20%.  
    """)

    st.subheader("Employee Performance Report")
    st.write("""
    **Tools:** Tableau  
    - Analyzed employee metrics and improved operational insights by 25%.  
    """)

    st.subheader("Detection of Malicious Web Attacks")
    st.write("""
    **Tools:** Python, scikit-learn  
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
