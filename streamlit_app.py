import streamlit as st
import gspread

from oauth2client.service_account import ServiceAccountCredentials

def main():
    st.title("Simple Information Intake Form")

    # Creating the form
    with st.form(key='info_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')

    # Process the form data
    if submit_button:
        if name and email and message:
            st.success(f"Thank you, {name}. Your information has been submitted.")

            # Authenticate with Google Sheets and append the data
            add_data_to_google_sheet(name, email, message)
        else:
            st.error("Please fill in all fields.")

def add_data_to_google_sheet(name, email, message):
    # Google Sheets API setup
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret_79345116573-kbgj3a5sgufjq485gjglmtkmb8vo6u80.apps.googleusercontent.com.json', scope)
    client = gspread.authorize(creds)

    # Replace with your Google Sheet URL
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/17O2ZyHRjZO4uvIfixwL4SZMJieOfA-JQVe35D5FLGUk").sheet1
    sheet.append_row([name, email, message])

if __name__ == "__main__":
    main()
