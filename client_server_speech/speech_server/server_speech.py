
import socket
import openai

TCP_IP = 'your IP'
TCP_PORT = #your port
BUFFER_SIZE = #your buffer size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1) 

while True:

    conn, addr = s.accept()
    print('Connection address: {}'.format(addr))

    data = conn.recv(BUFFER_SIZE)
    if not data:
        print('No message received!')
        break

    question = data.decode('utf-8')
    print('Received question: {}'.format(question)) 

    openai.api_key = 'your API key'

    response = openai.ChatCompletion.create(

         model = 'gpt-3.5-turbo',
         messages = [{'role': 'user', 'content': question}]

    )

    response_formatted = response['choices'][0]['message']['content']

    print('Response: {}'.format(response_formatted))

    response_encoded = response_formatted.encode('utf-8')
    conn.send(response_encoded)
    
    conn.close()

    print('------------------------------------------------')



