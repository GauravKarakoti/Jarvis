import languagemodels as lm
def ReplyBrain(input):
    lm.config["max_ram"] = "4gb"
    output=lm.do(input)
    return output
print(ReplyBrain('''summarize this 
                 
                 DocuBot - Documents Summarization Agent
Overview
DocuBot is an AI-powered document summarization agent designed to process lengthy documents and generate concise summaries. It supports various file formats, offers customizable summary lengths, and provides multi-language support. DocuBot helps users quickly grasp the key points of reports, research papers, legal documents, and more.

Features
Multi-Format Support: Works with PDF, DOCX, TXT, and more.
Customizable Summaries: Allows users to choose summary length (short, medium, or detailed).
Multi-Language: Supports summaries in multiple languages.
Key Section Identification: Highlights important sections like key findings, action items, or conclusions.
User Preferences: Customize the summary based on personal or business needs.
How It Works
Upload Document: Upload any supported document.
Choose Summary Type: Select the type of summary (Short, Medium, Detailed).
Receive Summary: DocuBot analyzes the document and returns a summary.
Download or Share: The summarized document can be downloaded or shared via email.
'''))
