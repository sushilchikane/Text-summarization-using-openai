import streamlit as st
from read_pdf_file import read_pdf
from openai_service_2 import get_response
from io import BytesIO
import os,json
from masking import mask_phi
from chompjs import parse_js_object

def main():
    st.title("Clinical Summary")

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=True)

    if uploaded_file:
        st.success("File uploaded successfully!")

        # Display file details
        # file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        # st.write(file_details)

        # Process button
        if st.button("Process"):
            # Read PDF content
            # pdf_content = read_pdf(uploaded_file)
            content = ''
            location = save_uploaded_file(uploaded_file)
            print(f"loc: {location}")
            for i in location:
                pdf_content = read_pdf(i)
                content+=pdf_content

            print(f"Length of total content: {len(content.split())}")
            masked_content = mask_phi(content)
            # Get response
            response = get_response(masked_content)
            # response = get_response(pdf_content)
            print(f"type of response: {type(response)}")
            print(response)
            # json_response = json.loads(response)
            json_response = parse_js_object(response)

            print(f"type of json response: {type(json_response)}")

            # Display the processed content
            # st.subheader("Processed Content:")
            # st.write(response)

            st.subheader("Issue Description:")
            st.write(json_response['Issue Description'])

            st.subheader("Clinical Information:")
            st.write(json_response['Clinical Information'])

            st.subheader("Appeal Criteria:")
            st.write(json_response['Appeal Criteria'])

            st.subheader("Clinical Recommendation:")
            st.write(json_response['Clinical Recommendation'])

# def save_uploaded_file(uploaded_file):
#     # Save the uploaded file to a temporary location
#     temp_location = os.path.join("temp", uploaded_file.name)

#     with open(temp_location, "wb") as f:
#         f.write(uploaded_file.read())

#     return temp_location

def save_uploaded_file(uploaded_files):
    locations = []

    for i, file in enumerate(uploaded_files):
        temp_location = os.path.join("temp", f"uploaded_file_{i + 1}.pdf")
        with open(temp_location, "wb") as f:
            f.write(file.read())
        locations.append(temp_location)

    return locations

if __name__ == "__main__":
    main()
