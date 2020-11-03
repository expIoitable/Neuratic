import requests
import json
import Config
from Config import *

Logo = """
                                                        ,,
`7MN.   `7MF'                                    mm     db
  MMN.    M                                      MM
  M YMb   M  .gP"Ya `7MM  `7MM  `7Mb,od8 ,6"Yb.mmMMmm `7MM  ,p6"bo    Neuratic OSint
  M  `MN. M ,M'   Yb  MM    MM    MM' "'8)   MM  MM     MM 6M'  OO    Tool By vivid#6221
  M   `MM.M 8M""""""  MM    MM    MM    MM     ,pm9MM  MM     MM 8M
  M     YMM YM.    ,  MM    MM    MM    8M   MM  MM     MM YM.    ,   For Contact:
.JML.    YM  `Mbmmd'  `Mbod"YML..JMML.  `Moo9^Yo.`Mbmo.JMML.YMbmd'    vivid@fbi.systems
"""
# Because of the broken logo I have to do this ;/
print(Logo)

class OSint:

# Mainly Troubleshooting

    if AltFinder != False:
        print("(+) Alt-Finder Enabled. ")
    else:
        pass

    if MailboxLayer != False:
        print("(+) MailboxLayer Key Connected.")
    else:
        print('Error Using MailboxLayer API Key. Please Enter Your Key In "Config.py"')
        exit()

    User = input(str("Enter The Target Email: "))

    try:
        TargetEmail = requests.get(f"http://apilayer.net/api/check?access_key={MailboxLayer}&email={User}&smtp=1&format=1").text
        TargetLoad = json.loads(TargetEmail)

        if TargetLoad["smtp_check"] != True:
            print("Error Validating Email - Please Use A Valid Email Address.")
            exit()
        else:
            pass

        # Data About the email Sent
        MailboxGraph = f"""
Data From MailboxLayer

Email:              {TargetLoad["email"]}
User:               {TargetLoad["user"]}
Domain:             {TargetLoad["domain"]}
Format Valid:       {TargetLoad["format_valid"]}
MX Found:           {TargetLoad["mx_found"]}
SMTP check:         {TargetLoad["smtp_check"]}
Catch All:          {TargetLoad["catch_all"]}
Role:               {TargetLoad["role"]}
Disposable:         {TargetLoad["disposable"]}
Score:              {TargetLoad["score"]}
    """
        print(MailboxGraph)
    except:
        print("(-) Please use a valid MailboxLayer API Key.")
        exit()

    if AltFinder
