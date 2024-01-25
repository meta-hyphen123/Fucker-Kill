import os
import subprocess
import urllib
import socket
from rich import print

pathdog = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 构建路径
path_open = os.path.join(pathdog, 'Fucker-Tool')


dog = """

$$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\              $$\   $$\ $$\ $$\       $$\       
$$  _____|$$ |  $$ |$$  __$$\ $$ | $$  |$$  _____|$$  __$$\             $$ | $$  |\__|$$ |      $$ |      
$$ |      $$ |  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |            $$ |$$  / $$\ $$ |      $$ |      
$$$$$\    $$ |  $$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |            $$$$$  /  $$ |$$ |      $$ |      
$$  __|   $$ |  $$ |$$ |      $$  $$<   $$  __|   $$  __$$<             $$  $$<   $$ |$$ |      $$ |      
$$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |            $$ |\$$\  $$ |$$ |      $$ |      
$$ |      \$$$$$$  |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |            $$ | \$$\ $$ |$$$$$$$$\ $$$$$$$$\ 
\__|       \______/  \______/ \__|  \__|\________|\__|  \__|            \__|  \__|\__|\________|\________|
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                                                                                                                                  
 """
shit = """                                  '                            '                                                                                         
                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                               .WWWWWWWW#WWWKKWWKKKKEEEWKWKKKKKKKKKKEEKKKG                          
                             EGLLGiLLGGGEKWWKKEKKKWWWKKWW.         EE#KWWG                          
     GLGGLLGEEEEEEEEKKEKKWiGEEGKKKEGKKKWKKKKWKWKKWWWKKKKKKGEEGGGGGGKKEEEEEEEEEEEEEEEEEEEEEEEGE      
     G#EEGGGGGEGEKKKEGGGGEKEEEKKKEEEKKKKKKKKKKWKKKWWWGEKEGLt,.                                      
     GWEEGGEELGGGGEEKKEKEt    KKEEG,    E  GEEEEEEEEt                                               
     GWEEEEEEEKEE              GEKt        GEEEEKEEE                                                
     EEEEEEt                  KEKE           EEEEEEE                                                
                             KEEE            EEEEKEEE                                               
                            KEEKE             EEEEEEEG                                              
                             ,EKG              EEKKKEEE                                             
                                                EEKKKKEE                                            
                                                .EKKKKEKE                                           
                                                  EEKKEE                                            
                                                   KKL
"""
print(f'[white]{dog}[/white]')
print(f'[white]{shit}[/white]')

print("""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
1. Ip-Scanner                   | 7. Sub-Domain-Scanner      
2. Discord-Nuke                 | 8. DDOS-TOOL
3. Subdirectory-Scanner         | 9. Discord-Token-Grabber
4. Email-Boomber                | 10. Keylogger 
5. Phone-Locator                | 11. Web-Crawler
6. Port-Scanner                 | 12. Reverse-Shell 
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
""")

def about_url(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        host = parsed_url.hostname

        # Fetch IP address
        ip = socket.gethostbyname(host)

        # Determine the port based on the URL scheme
        if parsed_url.scheme == 'http':
            port = 80
        elif parsed_url.scheme == 'https':
            port = 443
        else:
            print("Unsupported URL scheme.")
            return

        # Print information to the console
        print(f"URL: {url}\nIP Address: {ip}\nPort: {port}")

    except Exception as e:
        # Handle any errors that may occur
        print(f"Error fetching information: {str(e)}")

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        return output
    except Exception as e:
        return f"Error running command: {str(e)}"

def run_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def main():
    # 切换到指定目录
    os.chdir(path_open)
    while True:
        user_input = input(">").strip()
        if not user_input:
            continue
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == '1':
            run_python_script(os.path.join(path_open, "ip-lookup.py"))
        elif user_input.lower() == '2':
            run_python_script(os.path.join(path_open, "nuke-bot", "main.py"))
        elif user_input.lower() == '3':
            run_python_script(os.path.join(path_open, "Subdirectory-scanner", "main.py"))
        elif user_input.lower() == '4':
            run_python_script(os.path.join(path_open, "email-bomber.py"))
        elif user_input.lower() == '5':
            run_python_script(os.path.join(path_open, "phone-locator.py"))
        elif user_input.lower() == '6':
            run_python_script(os.path.join(path_open, "port-scanner.py"))
        elif user_input.lower() == '7':
            run_python_script(os.path.join(path_open, "subdomain", "main.py"))
        elif user_input.lower() == '8':
            run_python_script(os.path.join(path_open, "ddos.py"))
        elif user_input.lower() == '9':
            run_python_script(os.path.join(path_open, "discord-token-grabber.py"))
        # 添加其他选项...

        else:
            result = run_command(user_input)
            print(result)

if __name__ == "__main__":
    main()
