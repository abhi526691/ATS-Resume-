import streamlit as st


class FileUpload():
    job_description = ""
    resume = ""

    def __init__(self):
        self.actions = {
            "Generate Dynamic Feedback": None,
            "Generate Cover Letter": None,
            "Generate Interview Question": None,
            "Career Path Suggestion": None,
            "Generate email Template": None,
            "Generate linkedin Message Template": None,
        }
        self.input_file()

    def create_button(self, label):
        self.actions[label] = st.button(label)
        return self.actions[label]

    def input_file(self):
        self.job_description = st.text_area(
            "Job Description:", placeholder="Enter the job description:")
        self.resume = st.file_uploader("Upload Your Resume ", type='pdf')

        # Create buttons and store their states
        for action in self.actions.keys():
            self.create_button(action)

    def button_click_event(self):
        for action, clicked in self.actions.items():
            if clicked:
                if self.job_description and self.resume:
                    # super().__init__(job_description=self.job_description, resume=self.resume)
                    for action, clicked in self.actions.items():
                        if clicked:
                            return action.lower().replace(" ", "_")

                elif self.job_description and not self.resume:
                    st.error("Resume not uploaded", icon="🚨")
                elif not self.job_description and self.resume:
                    st.error("Job Description not uploaded", icon="🚨")
                else:
                    st.error("Job Description and Resume not uploaded", icon="🚨")
