

import socket 
def ajaxWebserv( IP_addr ):
  
  #地址簇
  #socket.AF_INET =2 — TCP/IP – IPv4
  #socket.AF_INET6 =10 — TCP/IP – IPv6  
  #套接字类型
  #socket.SOCK_STREAM =1 — TCP流
  #socket.SOCK_DGRAM =2 — UDP数据报
  #socket.SOCK_RAW =3 — 原始套接字
  #socket.SO_REUSEADDR =4 — socket可重用
  s_web=None
  s_web = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建套接字 地址簇TCP/IP – IPv4   套接字类型 TCP流
  s_web.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #根据选项值设置套接字  socket.SOL_SOCKET =4095
  s_web.bind((str(IP_addr),80))                      #绑定ip 端口 (ip,pot) 必须是个元组  s.listen(1)                                           #开始监听 接受套接字的最大个数，至少为0，如果没有指定，则默认一个合理值。
  
  s_web.listen(3) 
  print('--01-->(ajaxWebserv) ajaxwebserve have listenning ......')
  
  while True:
    try:  
      conn, addr = s_web.accept()                             # conn：新的套接字对象，可以用来收发消息,address：连接到服务器的客户端地址

      print('--02-->(ajaxWebserv) Got a connection from :',addr)
      request = conn.recv(1024)                           #接收数据，返回接收到的数据对象。（1024）为字节数
      #sendall()函数通过数据块连续发送数据
      #向客户端  发送 response_head
      conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: FireBeetle\nContent-Type: text/html\n\n')
      #在 串口中打印 请求头
      #print("AjaxWebserve received request_head:\r{0}".format(str(request)))
      
      #---------------------------------------------------------------------------------
      #向客户端  发送 内容 此处可以是网页内容  
      conn.send("AjaxWebserve have received:")                                    #send data
      
      #---------------------------------------------------------------------------------
      conn.sendall('\r\n')
  
    except Exception as e:   
      print('--03-->(ajaxWebserv) effor inform:',e)
    finally:
      #关闭套接字
      conn.close()                                       
      #print("Connection with  closed")

