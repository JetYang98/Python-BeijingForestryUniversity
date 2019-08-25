import socket
from os.path import getsize

def file_deal(file_name):
    """
    定义函数用于处理用户索要下载的文件
    """
    try:
        # 二进制方式读取
        files = open(file_name, "rb")
        mes = files.read()
    except:
        pass
    else:
        files.close()
        return mes

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 固定端口号
    tcp_socket.bind(("192.168.1.14",8888))
    # 将主动套接字转为被动套接字
    tcp_socket.listen(128)

    while True:
        # 利用accept获取分套接字以及客户端的地址
        client_socket, client_addr = tcp_socket.accept()
        # 接收客户端的数据
        file_name = client_socket.recv(4096).decode()
        file_size = bytes()
        try:
            # 接受文件大小
            file_size = str(getsize(file_name)).encode()
        except:
            print("未找到文件：%s" % file_name)
        client_socket.send(file_size)
        # 调用函数处理用户下载的文件
        mes = file_deal(file_name)

        if mes:
            # 如果文件不为空发送
            client_socket.send(mes)
        #关闭分套接字
        client_socket.close()

if __name__ == "__main__":
    main()
