import socket
from .validator import show_dic
def show_service():
     while True: 
      target_addres = input("Enter Target Address: ")
      print("")
      try:
       socket.gethostbyname(target_addres)
       break
      except:
        print("Enter Valid Target Address⚠️")
        continue
     max_port = 65535
     min_port = 0
     while True:
       try:
         s_port = int(input("Start Port: "))
         e_port = int(input("End Port: "))
         print("")
         if min_port < s_port <= max_port and min_port < e_port <= max_port:
           print("Ports Accepted.")
           print("Scanning.......")
           print("")
           break
         else:
           print("Port Numbers Must Between [1 to 65535]📌")  
           continue
       except:
         print("Enter Only Numbers🔢")  
         continue
     result = (e_port - s_port+1) 
     count_port = 0 
     port_file = []
     print("-"*50)
     for check_port in range(s_port, e_port+1):
       __socket = socket.socket()
       __socket.settimeout(0.3)
       check_socket = __socket.connect_ex((target_addres, check_port))
       if check_socket == 0:
         file_port_checker = show_dic(check_port)
         print(check_port,"/tcp"" Open",file_port_checker)
         port_file.append((check_port,"/tcp"" open",file_port_checker))
         count_port += 1
       __socket.close()
     print("-"*50)
     print("")  

     print("Total Checked Ports:", result)
     print("Total Open Ports:", count_port)
     print("")
     


     return check_port, target_addres, result, count_port, port_file

          
