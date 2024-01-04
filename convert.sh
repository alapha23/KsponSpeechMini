#!/bin/bash

# Directory containing the PCM files
DIR="/home/zgao/Documents/WhisperKo/KsponSpeechMini/audio"

# Loop through all PCM files in the directory
for pcmfile in "$DIR"/*.pcm; do
    # Construct the WAV filename by replacing the .pcm extension with .wav
    wavfile="${pcmfile%.pcm}.wav"

    # Convert PCM to WAV (adjust parameters as needed)
    ffmpeg -f s16le -ar 16000 -ac 1 -i "$pcmfile" "$wavfile"

    echo "Converted $pcmfile to $wavfile"
done

rm "$DIR"/*.pcm

echo "Conversion completed."

