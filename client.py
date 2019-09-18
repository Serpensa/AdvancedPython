import yaml
import socket
import json
from argparse import ArgumentParser


def make_request(text):
    return{
        'data': text

    }




if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024
    }

    parser = ArgumentParser()

    parser.add_argument('-c', '--config', type=str, required=False,
                        help='Sets config path')
    parser.add_argument('-ht', '--host', type=str, required=False,
                        help='Sets server host')
    parser.add_argument('-p', '--port', type=str, required=False,
                        help='Sets server port')

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            file_config = yaml.safe_load(file)
            config.update(file_config or {})

    if args.host:
        host = args.host
    else:
        host = config.get('host')

    if args.port:
        port = args.port
    else:
        port = config.get('port')

    buffersize = config.get('buffersize')

    sock = socket.socket()
    sock.connect((host, port))

    massage = input('Input your message: ')
    request = make_request(massage)
    string_request = json.dumps(request)
    sock.send(string_request.encode())
    bytes_response = sock.recv(buffersize)

    response = json.loads(bytes_response)
    print(response)

    print(f'Send message to {host}:{port}')
    print(request)

    sock.close()

