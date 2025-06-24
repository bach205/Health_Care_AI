from .config import load_llms_model_merged
import torch
loaded = load_llms_model_merged()
model = loaded["model"]
tokenizer = loaded["tokenizer"]

async def call_chatbot(question):
  prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": question}],
    tokenize=False
  )

  inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
  outputs = model.generate(**inputs, max_new_tokens=1024, temperature=0.7)
  print(tokenizer.decode(outputs[0], skip_special_tokens=True))


async def stream_chatbot(question):
    print("start streaming")
    prompt = tokenizer.apply_chat_template(
        [{"role": "user", "content": question}],
        tokenize=False
    )
    
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]

    generated = input_ids
    past_key_values = None

    model.eval()
    is_answer = False
    with torch.no_grad():
        outputs = model(
                input_ids=generated[:, :-1],
                past_key_values=past_key_values,
                use_cache=True,
            )
        past_key_values = outputs.past_key_values
        for _ in range(1024):  # max_new_tokens
            outputs = model(
                input_ids=generated[:, -1:],
                past_key_values=past_key_values,
                use_cache=True,
            )

            next_token_logits = outputs.logits[:, -1, :]
            next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)

            # In token mới ra ngay
            new_text = tokenizer.decode(next_token[0],skip_special_tokens=True)

            if(not is_answer):
              if(new_text == "\n\n"):
                is_answer = True
            else:
                print(new_text, end="", flush=True)

            # Kiểm tra nếu gặp <eos>
            if next_token.item() == tokenizer.eos_token_id:
                break

            # Cập nhật
            generated = torch.cat((generated, next_token), dim=1)
            past_key_values = outputs.past_key_values