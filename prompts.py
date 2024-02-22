class prompts:
    resume = ""
    job_description = ""

    def __init__(self, resume, job_description):
        self.resume = resume
        self.job_description = job_description

    def generic_prompt(self):
        return f"""
                Hey, act like a skilled or very experienced ATS (Application Tracking System)
        with a deep understanding of the tech field, software engineering, data science,
        data analyst, and big data engineer. Your task is to evaluate the resume based
        on the given job description. You must consider the job market is very competitive
        and you should provide the best assistance based on resume.
        """

    def define_dynamic_feedback_prompt(self):
        """
        Defines the text prompt for generating feedback on a resume based on a job description.

        Returns:
            str: The formatted prompt string.
        """

        return f"""{self.generic_prompt()}. Assign the
        percentage Matching based on the JD and the missing keywords with high accuracy.
        Also, give some suggestions based on the job description:

        resume: {self.resume}
        Job description: {self.job_description}

        I want the response in dictionary format having the structure:

        {{
            "JD Match": "{{}}",
            "MissingKeywords": [],
            "Profile Summary": "",
            "Suggestion": ""
        }}
        """

    def define_cover_letter_prompt(self):
        """
        Defines the text prompt for generating cover letter on a resume based on a job description.

        Returns:
            str: The formatted prompt string.
        """
        return f"""
        {self.generic_prompt()}. Similar to the profile summary, use the extracted keywords and skills
        to suggest cover letter content tailored to the specific job description.
        Below is the resume and job description.
        resume : {self.resume}
        Job Description: {self.job_description}
        """

    def define_interview_question_prompt(self):
        """
        Define the prompt to generate interview questions based on the job description.

        Returns:
            str: Formatted prompt string.
        """
        return f"""
        {self.generic_prompt()}. Generate some interview question based on the {self.job_description}.
        Don't include any extra information as I only need questions
        """

    def define_career_path_suggestion_prompt(self):
        """
        Define the prompt to Analyze the user's resume and job interests to 
        suggest potential career paths or related job opportunities.

        Returns:
            str: Formatted prompt string.
        """
        return f"""
        {self.generic_prompt()}that are relevant to your current role and future goals.
        Please Analyze the user's resume and job interests to suggest potential career paths or related job opportunities.
        """

    def define_email_template_prompt(self):
        """
        Define the prompt to generate email to send to recuiter based on resume and job description.

        Returns:
            str: Formatted prompt string.
        """
        return f"""
        Here is the job description and resume.
        Resume: {self.resume}
        Job Description: {self.job_description}

        Based on the given job description and resume can you frame a email to sent to the recuiter.
        I want the message to be strictly under 500 words.
        """

    def define_linkedin_message_prompt(self):
        """
        Define the prompt to generate message to send to recuiter on linkedin based on resume and job description.

        Returns:
            str: Formatted prompt string.
        """
        return f"""
        Here is the job description and resume.
        Resume: {self.resume}
        Job Description: {self.job_description}

        Based on the given job description and resume can you frame a message to sent to the recuiter in linkedin.
        I want the message to be strictly under 200 characters.
        """
