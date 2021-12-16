# Log4J-Huntress-Automate-Script
This python script will automate the testing for the Log4J vulnerability for HTTP and HTTPS connections.

**Pre-Requisits**

1. Python 2 must be installed on the system you are running the script from.
2. You must install the python packages required to run the script:

  You can do this through pip. Pip should already be installed if you have installed pyton from https://python.org.
  To ensure pip is installed you can run in cmd:
    `py -m ensurepip --upgrade`
  
  Then install the packages:
  
    `py -m pip install requests`
    `py -m pip install shlex`
    `py -m pip install subprocess`
    
 3. The script also calls Nmap, so this means Nmap must be installed on the target machine. Nmap can be downloaded from https://nmap.org/download.html
 4. Ensure you add nmap to the PATH environment variable during the installation.

**Running the Script**

1. First create a list of devices you want to test. These can be in the format of IP addresses, Hostnames, CIDR addresses and a range of addresses _(E.G. 192.168.0.2-192.168.0.6)_ save each target on a new line.  **The file must be named Targets and saved in the same folder as the python script. It must be a text file. Each target**
2. Load up the Huntress Log4Shell Vulnerability Tester https://log4shell.huntress.com - This is a great tool created by Caleb Stewart, Jason Slagle and John Hammond.
3. Copy your unique identifier string.
4. Run the HuntressAutomate.py python script.
    `py HuntressAutomate.py`
5. Paste your unique Identifier and press enter. Wait for the script to run.
6. Navigate back to the Huntress website and 'View Connections'. Any machines listed here are vulnerable to Log4Shell.  
