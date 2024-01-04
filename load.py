import os
import wave
import json

# Function to read Korean text from a file
def read_korean_text(file_path):
    try:
        with open(file_path, 'r', encoding='euc-kr') as file:
            return file.read().strip()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp949') as file:
            return file.read().strip()

# Function to calculate the duration of a PCM file
def get_pcm_duration(wav_filepath):
    with wave.open(wav_filepath, 'r') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

# Super directory
super_directory = '/home/zgao/Documents/KsponSpeech/KsponSpeech_01/KsponSpeech_01/'

# Audio directory
audio_directory = 'audio/'

# List to hold data for JSON Lines
data_for_jsonl = []

# Iterate over subdirectories in the super directory
for subdir in os.listdir(super_directory):
    subdir_path = os.path.join(super_directory, subdir)
    if os.path.isdir(subdir_path):
        # Iterate over files in the subdirectory
        for filename in os.listdir(subdir_path):
            if filename.endswith(".pcm"):
                wav_filename = filename.replace(".pcm", ".wav")
                audio_path = os.path.join(audio_directory, wav_filename)
                transcription_file = filename.replace(".pcm", ".txt")
                transcription_path = os.path.join(subdir_path, transcription_file)

                # Read the transcription file
                transcription = read_korean_text(transcription_path)

                # Calculate the duration of the audio file
                duration = get_pcm_duration(audio_path)

                # Append data to the list
                data_for_jsonl.append({
                    "audio": {"path": audio_path},
                    "sentence": transcription,
                    "duration": duration
                })

# Write to JSON Lines file
with open('transcriptions.jsonl', 'w', encoding='utf-8') as file:
    for item in data_for_jsonl:
        json.dump(item, file, ensure_ascii=False)
        file.write('\n')

print("JSON Lines transcription file created successfully.")

