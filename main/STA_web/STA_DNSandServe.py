

import SlimDNS
import ajaxwebserve

import _thread#多线程 模块

class DNSandServe: 
  #def __init__(self, ip):
    #self.ip = ip
    
  def start(self,ip,addr):
         
    server = SlimDNS.SlimDNSServer(ip, addr)
    print('--01-->(STA DNS Serve) IP and URL\n\tIP: ',ip,'\n\tURL: http://',addr,'.local')
    #两个线程
    _thread.start_new_thread( ajaxwebserve.ajaxWebserv, (ip,))
    #-------------------------------------------------------------
    #server.run_forever()      #这两句micropython.local能正常使用
   
    _thread.start_new_thread(server.run_forever,())
    #-------------------------------------------------------------
    print('--02-->(STA DNS Serve) STA webserve have setted')


