# Further fine tune fastchat-13b

1. Get fastchat model running by installing llama-13b weights and applying delta's.
2. Train llama-13b replacing identity - edit dummy.json.
3. Further fine tune using file-content training data.

### Edit `model_name_or_path`

Path to fastchat-13b, after following instructions in this README.

### Edit `data_path`

Betting its the same format as 7b's dummy.json. If not, you'll have to use fastchat-7b until they release it.

```
torchrun --nproc_per_node=8 --master_port=20001 fastchat/train/train_mem.py \
    --model_name_or_path ~/model_weights/llama-13b  \
    --data_path ~/datasets/sharegpt_20230422_clean_lang_split_identity.json \
    --bf16 True \
    --output_dir output_13b \
    --num_train_epochs 3 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 32 \
    --gradient_accumulation_steps 4 \
    --evaluation_strategy "steps" \
    --eval_steps 1500 \
    --save_strategy "steps" \
    --save_steps 1500 \
    --save_total_limit 8 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.04 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap offload" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --lazy_preprocess True


```
https://github.com/lm-sys/FastChat/blob/main/scripts/train_vicuna_13b.sh
Run

```
# Launch it on managed spot to save 3x cost (train Vicuna-13B with around $300)
sky spot launch -n vicuna scripts/train-vicuna.yaml --env WANDB_API_KEY
```
## Requirements

CPU RAM 130GB
https://huggingface.co/docs/transformers/main/model_doc/llama

## Pytorch

https://github.com/lm-sys/FastChat#vicuna-weights

Looks like pytorch

```
torch run ...
```

Search `pytorch` https://github.com/lm-sys/FastChat/search?q=pytorch reveals that likely pytorch 1.13.1 is used.

## Weights

https://github.com/lm-sys/FastChat#vicuna-weights

To run fastchat, you must apply delta weights on top of vicuna weights


https://huggingface.co/docs/transformers/main/model_doc/llama

1. Download Vicuna-13b weights (use form, etc)
2. Download conversion script
   https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/convert_llama_weights_to_hf.py
3. Run script to run conversion
   ```
   python src/transformers/models/llama/convert_llama_weights_to_hf.py \
       --input_dir /path/to/downloaded/llama/weights --model_size 7B --output_dir /output/path
   ```

   This will output the tokenizer and model.

4. The model and tokenizer can be loaded via:
```
from transformers import LlamaForCausalLM, LlamaTokenizer

tokenizer = LlamaTokenizer.from_pretrained("/output/path")
model = LlamaForCausalLM.from_pretrained("/output/path")
```

or follow instructions here:
https://www.linkedin.com/pulse/step-by-step-guide-running-vicuna-13b-large-language-nischal/

## Fine tuning further

Yes you can fine tune further.
https://github.com/lm-sys/FastChat/issues/424

Set path to pre-trained fastchat model

```
torchrun --nproc_per_node=4 --master_port=20001 fastchat/train/train_mem.py \
    --model_name_or_path ~/model_weights/llama-7b  \
    --data_path playground/data/dummy.json \
    --bf16 True \
    --output_dir output \
    --num_train_epochs 3 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 16 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1200 \
    --save_total_limit 10 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --lazy_preprocess True
```

## Weight conversion


Launch r5.2xlarge (64GB CPU RAM) instance

```
mkdir data
```

Attach volume (e.g. 100GB) in same region (select correct subnet if needed)

Mount volume

```
sudo mount /dev/nvme1n1 /data
```

Make sure weights and files are there for 13B

Clone `git clone https://github.com/huggingface/transformers` if /accneeded.

Create virtual env

```
sudo apt update
```

```
sudo apt install python3-pip
```


```
pip install virtualenv
```

```
python -m virtualenv venv
```

```
source venv/bin/activate
```

install dependencies

```
cd ~/data/transformers
```

```
pip install -e .
```

```
pip install -i https://pypi.org/simple/ huggingface-hub transformers
```

Add to path

```
echo "export PATH=$PATH:/home/ubuntu/.local/bin" >> ~/.bashrc
```

Install torch, if neccessary.

```
pip install torch torchvision -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

Install transformers, if neccessary.

```
pip install transformers
```

Install accelerate, if neccessary (because you have too little cpu memory).

```
pip install accelerate
```

Install sentencepiece

```
pip install sentencepiece
```

Install protobuff

```
pip install protobuff
```

Create output file for conversion.

```
mkdir ~/data/LLaMA_HuggingFace_Converted
```

Your mounted ~/data directory should look as follows:

```
.
└── data
    ├── llama.sh
    ├── tokenizer.model
    ├── tokenizer_checklist.chk
    ├── LLaMA/
    └─────13B/
    ├── transformers/
    └── venv/
```

Apply Vicuna weights.

```
python3 ~/data/transformers/src/transformers/models/llama/convert_llama_weights_to_hf.py     --input_dir ~/data/LLaMA/ --model_size 13B --output_dir ~/data/LLaMA_HuggingFace_Converted/
```

Script should take about 15 minutes or so.

Convert.

```
python3 -m fastchat.model.apply_delta \
    --base-model-path ~/data/LLaMA_HuggingFace_Conversion \
    --target-model-path ~/datavicuna-13b \
    --delta-path lmsys/vicuna-13b-delta-v1.1
```

Run cli.

```
python3 -m fastchat.serve.cli --model-path /path/to/model/weights --device cpu
```