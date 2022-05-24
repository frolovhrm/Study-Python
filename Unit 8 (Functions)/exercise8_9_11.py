"""Упражнение 9"""

# messages = ['Hello', 'How are you', 'When you come']
#
# def show_messages(messages):
#     while messages:
#         mess = messages.pop()
#         print(mess)
#
#
# show_messages(messages)

"""Упражнение 10"""

messages = ['Hello', 'How are you', 'When you come']
sent_messages = []
messages_2 = messages[:]

def send_message(messages):
    count = 0
    while messages:
        count +=1
        mess = messages.pop()
        print(f'{count}. - {mess}\t')
        sent_messages.append(mess)

send_message(messages_2)

print(f'\nСписок отправленных {sent_messages}')

print(f'\nCписок копия {messages_2}')

print(f'\nИсходный список {messages}')