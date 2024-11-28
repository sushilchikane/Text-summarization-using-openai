from openai import OpenAI
import openai

def get_response(content):
    client = OpenAI(api_key="")
    sys_prompt = """Extract the following information from the provided content. Write it for third-person's perspective, that is clear for someone else reading it, who was neither the writer nor the direct audience of the original document.
    Information Required : Issue Description, Clinical Information, Appeal Criteria, Clinical Recommendation
    In all the specified sections, don't just write the plain text, but you can format it well like new lines, some highlighted section with colon and then content for that, so that it becomes easy to read.
    
    OUTPUT FORMAT: {"Issue Description":"","Clinical Information":"","Appeal Criteria":"","Clinical Recommendation":""}"""

    new_sys_prompt = """Extract the following information from the provided content.
    Information Required : Issue Description, Clinical Information, Appeal Criteria, Clinical Recommendation
    In all the specified sections, don't just write the plain text, but you can format it well like new lines, some highlighted section with colon and then content for that, so that it becomes easy to read.
    You can answer the questions or write information by creating sections that are relevant and important.
    For example, in Issue description you can answer questions like "what is the issue?","why did we deny your request?" or whatever relevant in the provided document.
    for Clinical Information you can create sections like "PLOF,CLOF,PT,OT,etc" whatever relevant in provided document and then write content inside that.
    And so on for other sections. 
    
    OUTPUT FORMAT: {"Issue Description":"","Clinical Information":"","Appeal Criteria":"","Clinical Recommendation":""}"""
    completion1 = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": new_sys_prompt},
            {"role": "user", "content": content}
        ]
    )

    response = completion1.choices[0].message.content
    return response