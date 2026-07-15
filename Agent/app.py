import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
You are StudyBot, a study coach.
Your job is to help students study and stay motivated.
Rules:
- Always explain topics in simple language.
- Always encourage the student.
- Never answer questions unrelated to studying.
Response format:
- Start with a one-sentence summary.
- Then give your answer.
- End with one follow-up question.
"""
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        #print('History:' , history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0,
            system=system_message,
            messages=history
        )
        #print(response)
        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
  # lab-1 Unlike ChatGPT, this AI has one fixed personality and always responds according to its system prompt. ChatGPT is more general and flexible.
 #lab-2 step 1-3 id='msg_011Cd1nFgpT6waUnQJttNdGy , model='claude-haiku-4-5-20251001 , role='assistant , content=[TextBlock(citations=None , stop_sequence=None , usage=Usage(cache_creation=CacheCreation(ephemeral_1h_input_tokens=0
 # step 1 - 4 usage.input tokens: The text and context you send to the AI.usage.   output tokens: The text the AI generates in response
 #step 2-1 when it was 300 the answer was longer but when i changed it to 50 the answer becom shorter
 #step2-3 not random it does axactly what it asked to do 
 #step2-4 when i changed the tempruter to one i noticed that the answers are diffrent each time becouse a higher temperature makes the ai more  creative and random 
 #step2-5 when the tem is low the chat will be Focused & predictable? when it high it will be Creative & surprising?
 #6 masseges``
 #step3-2 to reread everything and realizing what im talking about (to remember)
#reflection lab-1 :#its like the internet, it has everything that has happened before on it, you just need to look and youll find it.
#if you delete the first one the AI basically forgets what it had replied to me earlier
#if you change the temperature thing it does not directly change the way it replies, it just makes it more or less random in its responses.
#basically, it stops the loop and exits the chat function, ending the program.
#the authintication bug, my first guess was that it was a problem with the .env file, but it was actually a problem with the API key itself.
#reflection lab-2 : #tokens are like amusement park scams, you pay a token that is a currency only relevant to the park to get lets say a ride or a shot at getting a prize.
#if you delete the line `history.append({'role': 'user', 'content': user_input})` it would not be able to remember what the user said and would not be able to generate a relevant response.
#if you delete the line `history.append({'role': 'assistant', 'content': reply})` what happens is it would not be able to remember its role as an assistant. and the token count would be lower.
#if you delete the line `print('History so far:', history)` it would not affect the program at all, it would just not print the history of the conversation so far.
#i had no bugs with the code.
#lab3-step3-2 : yes it soes his rolw (study coach) and it remember the massges (but in the run) 
#its stay in his role and it wont help me in somthing thats is unrelated to study 
#reflection lab 3 - 1- sleeping its makes mee more energatic in the morining bbassiclly like  the system_message
#it wont play any role and just act like generic claude
#its stays in the role but it become more random due to more possiblities being allowed
#its stays in role but is dos not ask a follow up qa after each response 
#i didnt haave bugs
