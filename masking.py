import spacy
import re

def mask_phi(text):
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)

    phi_labels = ['PERSON', 'DATE', 'ADDRESS', 'SSN', 'MRN', 'PHONE', 'EMAIL']

    # Mask identified PHI entities
    masked_text = text
    for ent in doc.ents:
        # print(ent.label)
        # print("===========")
        if ent.label_ in phi_labels:
            masked_text = masked_text.replace(ent.text, ent.label_)

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    masked_text = re.sub(email_regex, '<email>', masked_text)
    ssn_regex = r'\b\d{3}-\d{2}-\d{4}\b'
    masked_text = re.sub(ssn_regex, '<ssn>', masked_text)
    phone_regex = r'\b\d{3}-\d{3}-\d{4}\b'
    masked_text = re.sub(phone_regex, '<phone>', masked_text)

    return masked_text


# input_text = """Patient: John Doe
# DOB: 05/15/1980
# Address: 123 Main St, Cityville
# SSN: 123-45-6789
# MRN: MRN123456
# Phone: 555-123-4567
# Email: john.doe@example.com

# Patient: Jane Smith
# DOB: 03/20/1992
# Address: 456 Oak St, Townsville
# SSN: 987-65-4321
# MRN: MRN654321
# Phone: 555-987-6543
# Email: jane.smith@example.com"""

# masked_text = mask_phi(input_text)

# print(masked_text)
