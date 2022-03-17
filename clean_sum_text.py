import re
def clean_dream (dream_summarized):
  b=re.sub('[^A-Za-z0-9]+', " ", dream_summarized)
  c=re.sub(r'\b\w{1,3}\b', "", b)
  d=re.sub(r'\b(\w+)(?:\W+\1\b)+', r'\1', c, flags=re.IGNORECASE)
  final_dream_summarized=re.sub("summary text", "", d)
  final_dream_summarized=final_dream_summarized+"."

  return final_dream_summarized.strip()




