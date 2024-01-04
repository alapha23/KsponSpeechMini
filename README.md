
## Dataset Preparation

```
.
├── audio
│   ├── KsponSpeech\_01.wav
│   ├── KsponSpeech\_02.wav
│   ├── KsponSpeech\_02.wav
│   └── ... (more .wav files)
└── transcriptions.jsonl
```

### 1. Copy all audio files of KpsonSpeech\_01 into our target

Edit the script `move_all.sh` and change `base_dir` accordingly
```
vi move_all.sh
bash move_all.sh
```

### 2. Convert pcm to wav

Make sure ffmpeg is intalled.
Edit the script `convert.sh` and replace `DIR` with the absolute path of audio directory
```
vi convert.sh
bash convert.sh
```

This process will take aprox. 1~2 days

### 3. Create transcriptions.jsonl

Edit the script `load.py` so `super_directory` is where you can find folders from `KsponSpeech\_0001` to `KsponSpeech\_0124`.
```
super_directory = '/home/zgao/Documents/KsponSpeech/KsponSpeech_01/KsponSpeech_01/'

# Audio directory
audio_directory = 'audio/'
```

Then run the script
```
pip install wave
python load.py
```
