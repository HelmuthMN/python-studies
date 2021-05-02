messages = ['hello there', 'pokemon is good', 'i hate java']
sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    print(messages)
    print(sent_messages)    


send_messages(messages[:], sent_messages)
print(messages)