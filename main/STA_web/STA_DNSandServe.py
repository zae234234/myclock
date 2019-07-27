

import SlimDNS
import ajaxwebserve

import _thread#多线程 模块

class DNSandServe: 
  #def __init__(self, ip):
    #self.ip = ip
    
  def start(self,ip,addr):
      

    print('STA_DNSandServe address {0}'.format(ip))
    
    server = SlimDNS.SlimDNSServer(ip, addr)
    #一线程一循环
    _thread.start_new_thread( ajaxwebserve.ajaxWebserv, (ip,))
    server.run_forever()      #这两句micropython.local能正常使用 


