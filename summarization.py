import transformers
from transformers import pipeline


#dream="dream.txt"
# transcript="transcript1234.txt"
def sum_text(MyText):
    summarizer = pipeline("summarization")
    summarized = summarizer(MyText, min_length=8, max_length=10)
    return summarized[0]["summary_text"]



    # #open and read the transcript
    # f1=open(transcript, "r", encoding="utf8")
    # to_tokenize=f1.read()

    # #Initialize the HugginFace summarization pipeline
    # summarizer=pipeline("summarization")
    # summarized_1=summarizer(to_tokenize, min_length=75, max_length=200)

    # #open text file
    # text_file=open("teste_agora.txt", "w")
    # #write string to file
    # summarized_1=str(summarized_1)
    # text_file.write(summarized_1)
    # #close file
    # text_file.close()

    # f2=open("teste_agora.txt", "r", encoding="utf8")
    # to_tokenize2=f2.read()
    # summarized_2=summarizer(to_tokenize2, min_length=20, max_length=100)
    # print(summarized_2)
    # #transcript=summarized_2[0]["summary_text"]

    # #Return summarized text
    # #return transcript


#print(sum_text("zombie apocalypse child"))

