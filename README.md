# AI-Notes-Summarizer

# 📚 AI Notes Summarizer

## About the Project

AI Notes Summarizer is a beginner-friendly deep learning
project that converts long study notes into short,
readable summaries.

It uses a pretrained Transformer language model to identify
important information and generate a concise version of
the original text.

The project is designed to help students revise their
study materials more efficiently.

## Features

- Summarizes long study notes using AI
- Offers short, medium, and long summary options
- Displays original and summarized word counts
- Calculates the percentage of word reduction
- Allows users to download the generated summary
- Provides a simple and user-friendly interface

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- DistilBART pretrained language model

## How It Works

1. The user enters study notes into the application.
2. The text is passed to a pretrained AI model.
3. The model generates a shorter version of the notes.
4. The summary and word statistics are displayed.
5. The user can download the summary as a text file.

## Project Structure

    AI-Notes-Summarizer/
    ├── app.py
    ├── requirements.txt
    ├── sample_notes.txt
    ├── README.md
    └── .gitignore

## Installation and Setup

### Step 1: Install Python

Install Python 3.10 or a compatible version supported
by the selected package releases.

### Step 2: Clone the Repository

    git clone https://github.com/YOUR-USERNAME/AI-Notes-Summarizer.git

Replace YOUR-USERNAME with your GitHub username.

### Step 3: Open the Project Folder

    cd AI-Notes-Summarizer

### Step 4: Install Dependencies

    python -m pip install -r requirements.txt

### Step 5: Run the Application

    python -m streamlit run app.py

The application will open in your browser.

The first run requires an internet connection to download
the pretrained model. Model loading may take some time.

## Deep Learning Concept

This project uses a pretrained DistilBART Transformer
model for abstractive text summarization.

The model processes the input text and generates a
shorter version that preserves its key information.

The project uses transfer learning through a pretrained
model rather than training a neural network from scratch.

## Limitations

- The generated summary may omit important details.
- The pretrained model may occasionally produce incorrect
  or misleading information.
- Long inputs may be truncated by the model.
- An internet connection is needed to download the model
  on the first run.

Always review AI-generated summaries before using them
for exams or important academic work.

## Future Improvements

- Support uploading PDF and DOCX files
- Add multiple language support
- Improve summary quality and customization
- Deploy the application online
- Add screenshots and a live demo link

## Author

NAYLA IRFAN
B.Tech CSE Student

## License

This project is intended for educational and learning
purposes.
