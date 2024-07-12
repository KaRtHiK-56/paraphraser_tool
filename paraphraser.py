from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
import streamlit as st 

#creating the UI of the code 
st.title("Parapharaser Tool")
st.header("Your content rephrasing assistance")
contents = st.text_area("Please enter/paste your content:",height=250)

#creating the style required to generate the response style of the email
styles = st.selectbox("Style of rephrase",("Reriting","Expand and clarify","Condense and focus",
                                           "Adapt the tone","Abstracting","Acknowledging"), index=0)

#creating the python function for generating the email response using LLM
def paraphraser(contents,style):
    template = """ you are a expert english professional, who is skilled and wellversed in grammatical and rephrasing the content
    of the paragraph and rephrase the content {content}  in the {style} style.
    if any other questions or queries are asked please reply with the text- 'Sorry, i couldn't undestand you, apologies for the inconvinence
caused,this scope of work may be beyond the currrent working level.' """
    prompt_template = PromptTemplate.from_template(template=template)
    prompt = prompt_template.format(context=contents,style=style)
    llm = Ollama(model="llama3",temperature=0)
    response = llm(prompt)
    return response


#ceating the submit button and passing the data after submit button is clicked
submit = st.button("Generate")

if submit:
    st.write(paraphraser(contents,styles))