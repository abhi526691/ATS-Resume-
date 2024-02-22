# from BaseATS import BaseATS
import json
import streamlit as st
from streamlt import FileUpload
from textExtract import extractText
from prompts import prompts
from generator import openaiFunc
from helperFunction import *


class promptBased(FileUpload):
    job_description = ""
    resume = ""

    def __init__(self, buttonType, job_description, resume):
        self.job_description = job_description
        self.resume = extractText().extract_txt(resume)
        self.buttonType = buttonType
        self.prompts = prompts(self.resume, self.job_description)

        if self.buttonType == 'generate_dynamic_feedback':
            self.dynamic_feedback()
        elif self.buttonType == 'generate_cover_letter':
            self.cover_letter()
        elif self.buttonType == 'generate_interview_question':
            self.interview_question()
        elif self.buttonType == 'career_path_suggestion':
            self.career_path_suggestion()
        elif self.buttonType == 'generate_email_template':
            self.email_template()
        elif self.buttonType == 'generate_linkedin_message_template':
            self.linkedin_message_template()

    def dynamic_feedback(self):
        dyn_feedback = self.prompts.define_dynamic_feedback_prompt()
        output = openaiFunc().qna(dyn_feedback)
        try:
            if output:
                if isinstance(output, list):
                    json_str = "\n".join(output).strip() + '"}'
                    data_dict = json.loads(json_str)
                    format_and_display_output(data_dict)
                else:
                    st.write(output)
            else:
                st.error("No match found.", icon="")
        except:
            st.write(output)

    def cover_letter(self):
        cov_letter = self.prompts.define_cover_letter_prompt()
        output = openaiFunc().qna(cov_letter)
        if isinstance(output, list):
            st.markdown(f"Cover Letter:\n ")
            for i in output:
                st.write(i)
        else:
            st.markdown(f"**Cover Letter:**\n{output}")

    def interview_question(self):
        int_quest = self.prompts.define_interview_question_prompt()
        output = openaiFunc().qna(int_quest)
        if isinstance(output, list):
            for i in output:
                st.write(i)
        else:
            st.markdown(f"{output}")

    def career_path_suggestion(self):
        career_path = self.prompts.define_career_path_suggestion_prompt()
        output = openaiFunc().qna(career_path)
        if isinstance(output, list):
            for i in output:
                st.write(i)
        else:
            st.markdown(f"{output}")

    def email_template(self):
        email_temp = self.prompts.define_email_template_prompt()
        output = openaiFunc().qna(email_temp)
        if isinstance(output, list):
            for i in output:
                st.write(i)
        else:
            st.markdown(f"{output}")

    def linkedin_message_template(self):
        linkedin_temp = self.prompts.define_linkedin_message_prompt()
        output = openaiFunc().qna(linkedin_temp)
        if isinstance(output, list):
            for i in output:
                st.write(i)
        else:
            st.markdown(f"{output}")
