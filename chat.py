from openai import OpenAI

with open("key.txt", "r", encoding="utf-8") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

messages = []  # ← 新增：对话历史

while True:
    q = input("\n你：")
    if q in ("q", "退出"):
        break

    messages.append({"role": "user", "content": q})  # ← 存下你说的话

    r = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,  # ← 改这里：发全部历史
    )

    answer = r.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})  # ← 存下它的回答
    print("AI：" + answer)