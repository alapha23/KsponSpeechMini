#!/bin/bash

# Define the base directory
base_dir="/home/zgao/Documents/KsponSpeech/KsponSpeech_01/KsponSpeech_01"

# Define the target directory
target_dir="audio"

# Create target directory if it doesn't exist
mkdir -p "$target_dir"

# Loop from 9 to 124
for i in {9..124}; do
    # Format the folder number with leading zeros
    folder_num=$(printf "%04d" $i)

    # Define the source directory
    src_dir="$base_dir/KsponSpeech_$folder_num"

    # Copy .pcm files from the source to the target directory
    cp "$src_dir/KsponSpeech_"*".pcm" "$target_dir/"
done

echo "Files copied successfully."

