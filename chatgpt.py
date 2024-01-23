import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('openaiapikey.txt')
completion = openai.Completion()

def gpt3_completion(prompt, engine='gpt-3.5-turbo-instruct-0914', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['BOT:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

# def modify_start_message(chat_log,question,answer) -> str:
#     chat_log += f"Human: {question}\nAI: {answer}\n"
#     return chat_log


if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '\nBOT:'
        response = gpt3_completion(prompt)
        print('BOT:', response)
        conversation.append('BOT: %s' % response)