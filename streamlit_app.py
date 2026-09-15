import streamlit as st
import requests


st.set_page_config(
    page_title="JobFit",
    page_icon="💼",
    layout="centered"
)


st.title("💼 JobFit")
st.write("AI-powered Resume and Job Description Matcher")


resume_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)


if st.button("Analyze Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:

        files = {
            "resume": (
                resume_file.name,
                resume_file.getvalue(),
                "application/pdf"
            )
        }

        data = {
            "job_description": job_description
        }

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            files=files,
            data=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Analysis completed!")

            st.metric(
                "Match Score",
                f"{result['match_score']}%"
            )

            st.subheader("Matched Skills")

            if result["matched_skills"]:
                st.write(", ".join(result["matched_skills"]))
            else:
                st.write("No matching skills found.")

            st.subheader("Missing Skills")

            if result["missing_skills"]:
                st.write(", ".join(result["missing_skills"]))
            else:
                st.write("No missing skills!")

        else:
            st.error(
                f"API Error: {response.status_code}"
            )