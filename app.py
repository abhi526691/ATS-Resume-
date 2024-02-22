import os
from streamlt import FileUpload
from prompt import promptBased


clicked_button = FileUpload()
button_value = clicked_button.button_click_event()
if button_value:
    promptBased(button_value, clicked_button.job_description,
                clicked_button.resume)

