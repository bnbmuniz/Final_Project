import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# #load tokenizer and pre-trained model
# tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
# model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# #load audio file from folder of choice
# file_path = "/Users/barbara/Downloads/33712a11-4888-41f1-beed-96489bb6380d.wav"

# speech, rate = librosa.load(file_path,sr=16000)

# input_values = tokenizer(speech, return_tensors = 'pt').input_values

# #Store logits (non-normalized predictions)
# logits = model(input_values).logits

# #Store predicted id's
# predicted_ids = torch.argmax(logits, dim =-1)

# #decode the audio to generate text
# transcript = tokenizer.decode(predicted_ids[0])

# print(transcript.lower())


# from transformers import AutoProcessor, AutoModelForCTC

# processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")

# model = AutoModelForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
# from datasets import load_dataset
# import torch

# dataset = load_dataset("hf-internal-testing/librispeech_asr_demo", "clean", split="validation")
# dataset = dataset.sort("id")
# sampling_rate = dataset.features["audio"].sampling_rate

# processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
# model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# # audio file is decoded on the fly
# inputs = processor(dataset[0]["audio"]["array"], sampling_rate=sampling_rate, return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits
# predicted_ids = torch.argmax(logits, dim=-1)

# # transcribe speech
# transcription = processor.batch_decode(predicted_ids)
# transcription[0]
