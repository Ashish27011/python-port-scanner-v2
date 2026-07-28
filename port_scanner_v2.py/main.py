from utils import banner
from scanner import service
from scanner import validator
from reports import w_report
def run_main_pc():
   banner.show_banner()
   print("")
   check_port, target_address, result, count_port, port_file = service.show_service()
   w_report.show_report(target_address, result, count_port, port_file)
   print("Report Saved successfully in [report.txt]💾")
   print("")
   banner.show_end_banner()   
run_main_pc()
while True:
   try:
      q_again = input("Do you Want Check Again🔁 [y/n]: ")
      if q_again == "y" or q_again == "Y":
         run_main_pc()
      if q_again == "n" or q_again == "N":
         print("Thanks For Use🙏")  
         break 
      else:
         print("Enter Valid Input!")
         continue 
            
   except:
      print("Enter Valid Input!")
      continue  