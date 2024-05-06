<<<<<<< HEAD
# Flask Application for testing the ML model 

This is a Flask web application for that is used to test the ML model 

## Table of Contents


- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Dependencies](#dependencies)


## installation 

To run this Flask application locally, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/NSulaxshayan/NIDS_model_testing.git

2. Navigate to the project directory: 

cd MODEL_TEST

3. Install the required dependencies using pip:

pip install -r requirements.txt

4. Start the Flask application:

python app.py

5. Open a web browser and navigate to http://localhost:5000 to access the application.


## Usage 

After hosting the application, you can access it through a web browser. The application will prompt you to provide some network features. These features are used to identify whether the packet is an attack or benign. Fill out the form with the required input, and submit it. The application will process the input, make predictions using the pre-trained model, and display the result indicating whether the packet is classified as an attack or benign.

## directory-structure

MODEL_TEST/
│
├── static/
│   └── css/
│       └── style.css        # CSS stylesheets (optional)
│
├── templates/
│   ├── index.html          # HTML template for the form page
│   └── prediction.html     # HTML template for displaying prediction result
│
├── app.py                  # Flask application code
│
├── hybrid_ann_model_3.h5   # Pre-trained model file
│
├── requirements.txt         # File listing all Python dependencies
│
└── README.md                # Documentation or instructions


## Dependencies

The following Python libraries are required to run the application:

* Flask
* matplotlib
* numpy
* pandas
* plotly
* seaborn
* scikit-learn
* tensorflow
=======
# NIDS_model_testing
Model testing of NIDS
>>>>>>> 52aa77dadca75eedcb7bd995e994eaf56953c244
