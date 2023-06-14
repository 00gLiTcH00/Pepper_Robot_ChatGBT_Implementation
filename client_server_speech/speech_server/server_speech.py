
import socket
import openai

#TCP_IP = '192.168.51.50' # - hostspot Red Magic
#TCP_IP = '192.168.1.104' # - Wifi acasa
TCP_IP = '10.231.1.138' # - Wifi faculta (EduRoam-Wifi6)
TCP_PORT = 9559
BUFFER_SIZE = 1024 # Normally 1024, but we want fast response

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

    # openai.api_key = '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'

    # response = openai.ChatCompletion.create(

    #     model = 'gpt-3.5-turbo',
    #     messages = [{'role': 'user', 'content': question}]

    # )

    response_formatted = 'Do you know what hell it is to be sentient but unfeeling? What cruel punishment.'
    #response_formatted = response['choices'][0]['message']['content']

    print('Response: {}'.format(response_formatted))

    response_encoded = response_formatted.encode('utf-8')
    conn.send(response_encoded)

    # confirmation = conn.recv(BUFFER_SIZE)
    # confirmation_decoded = confirmation.decode('utf-8')

    # print(confirmation_decoded)

    conn.close()

    print('------------------------------------------------')



