import openai
import json

    
openai.api_key = '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'
response = openai.Completion.create(
  model='text-davinci-003',
  prompt='写一段中文,500字',
  temperature=0.8,
  max_tokens=800,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
)

print(json.dumps(response, ensure_ascii=False))
    
# 去除非中文字符
def remove_non_chinese(text):
    return ''.join(c for c in text if c >= u'\u4e00' and c<=u'\u9fa5')



if __name__ == '__main__': 
    # 测试代码
    text = response['choices'][0]['text']
    print(text)
    print(remove_non_chinese(text)) # 你好
