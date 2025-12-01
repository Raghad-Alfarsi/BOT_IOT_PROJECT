BOT-IoT Intrusion Detection System (IDS)

Project Summary

This project builds an Intrusion Detection System to classify network traffic as normal or malicious using the BOT-IoT dataset. The system focuses on detecting cyberattacks in IoT environments and provides real-time prediction.

⸻

What the Project Does
	•	Reads and analyzes network traffic.
	•	Cleans and preprocesses the dataset.
	•	Trains a machine learning model.
	•	Predicts whether the traffic is malicious.
	•	Includes a simple Streamlit dashboard for real-time testing.

⸻

Model Used

Logistic Regression

This model was selected because:
	•	It works well with large datasets.
	•	It is fast and reliable.
	•	It produces strong results after preprocessing.

Model Performance
	•	Accuracy: 0.99998
	•	Very low error rate
	•	Performs well in attack detection

⸻

Dataset

The dataset is the BOT-IoT dataset from Kaggle.
It contains:
	•	Packet details
	•	Traffic statistics
	•	Attack labels and categories

⸻

Data Preprocessing

Steps applied:
	1.	Dropped non-useful columns.
	2.	Encoded categorical features.
	3.	Scaled numerical values.
	4.	Fixed imbalance using oversampling.

⸻

Evaluation

The model was evaluated using:
	•	Accuracy Score
	•	Confusion Matrix
	•	Classification Report

The results show that the model can detect malicious traffic with high accuracy.

⸻

Streamlit Dashboard

The Streamlit app allows the user to enter traffic features and receive a prediction:
	•	Normal
	•	Malicious

To run:
streamlit run app.py

Project Files: 
BOT_IOT_PROJECT/
│
├── app.py
├── model.pkl
├── notebook.ipynb
├── Report.pdf
├── Presentation.pdf
└── README.md
Tools Used
	•	Python
	•	Pandas
	•	NumPy
	•	Scikit-Learn
	•	Streamlit

  Conclusion
The IDS model achieved excellent accuracy and proves that Logistic Regression can be successful in detecting abnormal IoT traffic in real-time.
⸻

Author

Raghad Alfarsi
