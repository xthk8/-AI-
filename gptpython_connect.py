import os
import openai

openai.api_key = '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'

# ChatGPT와 상호작용하는 함수
def chat_with_gpt(prompt, chat_history=None):
    if chat_history is None:
        chat_history = []

    # 이전 대화 히스토리를 prompt에 추가
    prompt = '\n'.join(chat_history + [prompt])

    response = openai.Completion.create(
        engine="text-davinci-003",  # ChatGPT 엔진
        prompt=prompt,
        max_tokens=350,  # 반환할 최대 토큰 수
        temperature=1.0,  # 온도 설정
        n=1,  # 반환할 대답의 수
        stop=None,  # 대화를 중지시킬 텍스트
        timeout=None  # 요청 제한 시간
    )

    # 상호작용 결과에서 답변 추출
    answer = response.choices[0].text.strip()
    
    # 대화 히스토리에 추가
    chat_history.append(prompt)
    chat_history.append(answer)
    
    return answer, chat_history

# 대화형 루프
chat_history = []
while True:
    user_input = input("사용자: ")
    if user_input.lower() == 'exit':
        break

    # 사용자 입력을 ChatGPT에 전달하여 대답 받기
    response, chat_history = chat_with_gpt(user_input, chat_history)
    print("ChatGPT: " + response)