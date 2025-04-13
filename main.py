from fastapi import FastAPI, HTTPException
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import action_to_screen

# Load the fine-tuned T5 model and tokenizer
MODEL_PATH = "./t5"
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

app = FastAPI()

@app.get('/')
def root():
    return {'app': 'Jivani'}


@app.post('/interpret-command')
async def interpret_command(command: str):
    try:
        inputs = tokenizer(command, return_tensors="pt", max_length=512, truncation=True)
        inputs = {key: value for key, value in inputs.items()}
        with torch.no_grad():
            output_ids = model.generate(**inputs, max_length=512)
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        event_dict = {}
        pairs = output_text.split(',')
        for pair in pairs:
            if ':' in pair:
                key, value = pair.strip().split(':', 1)
                event_dict[key.strip()] = value.strip()
        if(action_to_screen.ACTION_TO_SCREEN.get(event_dict["action"].split("_")[1])):
            event_dict["screen"] = action_to_screen.ACTION_TO_SCREEN[event_dict["action"].split("_")[1]]
        return event_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
