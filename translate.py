
import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

#transcript="transcript.txt"

def translate(transcript):
    tokenizer=AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")
    model=AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")
    pten_pipeline=pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    transcript_translated=pten_pipeline(transcript)
    transcript_translated=transcript_translated[0]["generated_text"]
    return transcript
