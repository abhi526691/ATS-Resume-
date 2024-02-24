
https://github.com/abhi526691/ATS-Resume-/assets/53704940/6a5f546b-2781-4695-9632-8756c3ba4a64
# ATS Scanner Project

This project utilizes OpenAI and Streamlit to create an Advanced Talent Search (ATS) scanner. Users can upload their job descriptions and resumes, and the system provides dynamic feedback, generates cover letters, interview questions, career suggestions, email templates, and frames LinkedIn messages.

<iframe width="100%" height="100%" src="https://github.com/abhi526691/ATS-Resume-/assets/53704940/a0331326-e873-4ea6-86d4-54d51d7b4fd6" title="ATS RESUME" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Features

- **Dynamic Feedback:** Analyzes the resume and job description to give personalized feedback.
- **Cover Letter Generation:** Creates a tailored cover letter based on the job description.
- **Interview Questions:** Generates relevant interview questions for preparation.
- **Career Suggestions:** Offers career advice based on the user's resume and job interests.
- **Email Templates:** Provides templates for professional communication.
- **LinkedIn Messages:** Helps frame effective messages for LinkedIn networking.

## Getting Started

### Prerequisites

- Python 3.6 or later
- An OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhi526691/ATS-Resume-
   ```
2. Navigate to the project directory:
   ```bash
   cd ATS-Resume-
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Setup

1. Create an `.env` file in the project directory.
2. Generate an OpenAI API key by signing up or logging in at [OpenAI Platform](https://platform.openai.com/login/).
3. Save your API key in the `.env` file as follows:
   ```
   API_KEY=<your_api_key_here>
   ```

### Running the Application

Run the following command in your terminal:
```bash
streamlit run app.py
```

## Usage

After running the application, upload your resume and the job description. The system will analyze the inputs and provide you with dynamic feedback, suggestions, and templates.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgements
- OpenAI for the API that powers the core functionalities of this project.
- The Streamlit team for providing an easy way to create web applications for Python scripts.
