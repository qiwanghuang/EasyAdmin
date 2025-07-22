from mysql.connector.utils import read_int
from openai import OpenAI

class ChatLLM:
    def __init__(self, api_key, base_url) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.client = OpenAI(api_key = api_key, base_url = base_url)

    def chat(self, system_prompt, user_prompt, stream: bool, model: str, **kwargs) -> dict:
        pass

if __name__ == '__main__':
    client = ChatLLM(api_key = "", base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1").client
    # 创建流式响应 ChatCompletionStreamManager
    stream = client.chat.completions.create(
        model = "qwen-plus",
        messages = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁？'}
        ],
        stream = True
    )

