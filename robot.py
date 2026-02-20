# first the audio goes to deepgram_transcribe.py
# then it turns into .txt file and goes to text_to_pdf.py
# then it goes to ai.py for gpt analysis

from deepgram_transcribe import transcribe_audio
from text_to_pdf import pdfier
from ai import ai_summarizer

def mvp(audio_file, language = "en"):
    # turn the audio into txt file
    txt_file = transcribe_audio(audio_file,language)

    # turn the .txt into .pdf file so that chatgpt can read the file
    pdf_file = pdfier(txt_file)

    # send the pdf file to openai
    analysis = ai_summarizer(pdf_file)
    
    # return the analysis(it's a json)
    return analysis