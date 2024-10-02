"""Run the Flask Application"""


from app import create_app
import socket


def find_available_port():
    """
    Find an available port on localhost.

    Returns:
        int: Available port number.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


if __name__ == '__main__':
    app = create_app()
    available_port = find_available_port()
    print(f'Starting server on port {available_port}')
    app.run(debug=True, port=available_port)