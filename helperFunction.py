import streamlit as st


def format_and_display_output(final_output):
    """Formats and displays the parsed output in Streamlit."""

    st.subheader("Resume Score:")
    st.markdown(f'**{final_output["JD Match"]}**')

    st.subheader("Missing Keywords")
    st.markdown(f'**{", ".join(final_output["MissingKeywords"])}**')

    st.subheader("Profile Summary")
    st.markdown(f'**{final_output["Profile Summary"]}**')

    st.subheader("Suggestion")
    st.markdown(f'**{final_output["Suggestion"]}**')
