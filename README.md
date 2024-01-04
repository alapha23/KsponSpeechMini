
## Dataset Preparation

Expected dataset structure
```
.
├── audio
│   ├── KsponSpeech\_01.wav
│   ├── KsponSpeech\_02.wav
│   ├── KsponSpeech\_02.wav
│   └── ... (more .wav files)
├── dataset
│   ├── train.json
│   └── test.json
└── transcriptions.jsonl
...
```

#### 1. Copy all audio files of KpsonSpeech\_01 into our target

Edit the script `move_all.sh` and change `base_dir` accordingly
```
base_dir="/home/zgao/Documents/KsponSpeech/KsponSpeech_01/KsponSpeech_01"
```
`base_dir` should be the path where you can find folders from `KsponSpeech\_0001` to `KsponSpeech\_0124`.

```
vi move_all.sh
bash move_all.sh
```

#### 2. Convert pcm to wav

Make sure ffmpeg is intalled.
Edit the script `convert.sh` and replace `DIR` with the absolute path of audio directory
```
vi convert.sh
bash convert.sh
```

This process will take aprox. 1~2 days

#### 3. Create transcriptions.jsonl (if you are not using `KsponSpeech_01`)

If you are using `KsponSpeech_01`, aka.`KsponSpeech\_0001` to `KsponSpeech\_0124`., then you can use the transcription.jsonl that comes with this repo as is, and can skip step 3 and 4 and go directly to evaluation or inference.

Else, edit the script `load.py` so `super_directory` is where you can find folders from `KsponSpeech\_0001` to `KsponSpeech\_0124`.
In my case, 
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

#### 4. Split transcriptions.jsonl into train.json and test.json

As title, I used vim to split transcriptions.jsonl into 1:4, where the test.json takes 1 and train.json takes 4. The two files reside in dataset.

If you are using the same dataset (`KsponSpeech_01`) then you can use the given two json files as is.

#### To evaluate the fine-tuned model

```
# WER
python evaluation.py --model_path=openai/whisper-tiny --language=Korean --metric wer > whisper-tiny.wer.out
# CER
python evaluation.py --model_path=openai/whisper-tiny --language=Korean --metric cer > whisper-tiny.cer.out
```

To change the evaluation set, change `dataset/test.json`

### To infer the fine-tuned model

```
python infer.py --language=Korean --audio_path=dataset/test.wav --model_path=models/whisper-tiny-finetune
```
Replace `models/whisper-tiny-finetune` with the path to where you have downloaded the model

## To fine-tune another model

#### 1. fine-tune

```
CUDA_VISIBLE_DEVICES=0 python finetune.py --language=Korean --base_model=openai/whisper-tiny --output_dir=output/ --per_device_train_batch_size=256 --learning_rate=0.05 --num_train_epochs=4
```

#### 2. Merge Lora

```
python merge_lora.py --lora_model=output/whisper-tiny/checkpoint-best/ --output_dir=models/
```


