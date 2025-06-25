import streamlit as st
from google_search import get_company_name, get_hr_profiles
from message_generator import generate_cold_message

st.set_page_config(page_title="ReachHR",layout="centered")
st.title("🚀 ReachHR")
st.caption("Find HRs and recruiters, get company links, and generate custom LinkedIn messages using AI — perfect for internships, referrals, or job outreach.")

st.markdown("---")

company=st.text_input("🏢 Company Name", placeholder="e.g. Adobe")
location=st.text_input("📍 Location", placeholder="e.g. Bengaluru")


if st.button("🔍 Find HR Profiles"):
    if company.strip() and location.strip():
        st.subheader("🌐 Company Website")
        website = get_company_name(company)
        print(website)
        st.write(website)

        st.subheader("👥 HRs / Recruiters")
        profiles = get_hr_profiles(company, location)
        
        if profiles:
            for person in profiles:
                st.markdown(f"- **{person['name']}** — [{person['link']}]({person['link']})  \n  _{person['snippet']}_")
        else:
            st.warning("No HR profiles found.")
    else:
        st.warning("Please fill both Company Name and Location.")

st.markdown("---")

st.subheader("✍️ Cold Message Generator")

user_goal=st.text_area(
    "🎯 What do you want to say?",
    placeholder="e.g. Provide detailed information about yourself and the role you want to apply for"
)

if st.button("✉️ Generate Cold Message"):
    message=generate_cold_message(company,user_goal)
    st.text_area("📩 Your Cold Message", value=message, height=250)
    