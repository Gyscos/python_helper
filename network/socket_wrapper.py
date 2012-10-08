import socket

class SocketWrapper:
    def __init__(self, sock):
        self.sock = sock

    def read_all(self):
        msg = ''

        while True:
            chunk = self.sock.recv(2048)
            if not chunk:
                break
            msg += str(chunk, encoding='utf-8')

        return msg

    def read_raw_length(self, length):
        left = length
        data = b''
        while left > 0:
            chunk = self.sock.recv(left)
            if not chunk:
                # Error !
                break
            data += chunk
            left -= len(chunk)
        return data

    def read_sized(self):
        chunk = read_raw_length(4)
        length = struct.unpack('!i', chunk)

        data = read_raw_length(length)
        return str(data, encoding='utf-8')

    def send_msg(self, msg):
        # print("Msg :" + msg)
        data = bytes(msg, encoding='utf-8')
        self.sock.sendall(data)

    def send_line(self, msg):
        # Make sure no \n are in msg ?
        self.send_msg(msg + '\n')

    def send_sized(self, msg):
        data = bytes(msg, encoding='utf-8')
        self.sock.sendall(struct.pack('!i', len(data)) + data)

def connect(addr):
    s = socket.socket(socket.AF_INET)
    s.connect(addr)
    return SocketWrapper(s)

def get_answer_sized(addr, msg):
    s = connect(addr)
    s.send_sized(msg)
    return s.read_sized()

def get_answer(addr, msg):
    s = connect(addr)
    s.send_msg(msg)
    return s.read_all()
