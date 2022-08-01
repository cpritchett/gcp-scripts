# Script to retrieve compute engine details.
# Author - Rajathithan Rajasekar - 03/03/2020
# https://gist.github.com/rajathithan/c26c84cdaf74011fe3a6716f665e6269
# Updated - Chad Pritchett - 07/20/2022

from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import re
import sys

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)

#print(str(sys.argv))
if (len(sys.argv)) >=3:
    project = sys.argv[1]
    instance = sys.argv[2]
    zone = sys.argv[3]

    # Get instance details
    request = service.instances().get(project=project, zone=zone, instance=instance)
    response = request.execute()
    
    # Get machine type
    mtype = re.search(r'(.*)/(.*)', response['machineType']).group(2)

    # Get operating system name
    osu = response['disks'][0]['licenses'][0]
    os = re.search(r'(.*)/(.*)', osu).group(2)

    # Get disk size
    dsize = str(response['disks'][0]['diskSizeGb']) + ' GB'

    # Use machine type to get cpu count & memory size
    mrequest = service.machineTypes().get(project=project, zone=zone, machineType=mtype)
    mresponse = mrequest.execute()

    # Get cpu count
    cpu = mresponse['guestCpus']

    # Get memory size
    megabyte = mresponse['memoryMb']
    gigabyte = 1.0/1024
    memory = str(gigabyte * megabyte) + ' GB'

    # Get Creation Time 
    ctime = response['creationTimestamp']

    # Last Started 
    laststart = response['lastStartTimestamp']

    # Last Stopped
    if 'lastStopTimestamp' in response:
        laststop = response['lastStopTimestamp']
    else:
        laststop = None

    # Get status
    if 'status' in response:
        status = response['status']
    else:
        status = None
   

    # Get status Message
    if 'statusMessage' in response:
        smessage = response['statusMessage']
    else:
        smessage = None

    # Get Labels
    if 'labels' in response:
        labels = response['labels']
    else:
        labels = None

    print(f'{project},{instance},{zone},{mtype},{os},{cpu},{memory},{dsize},{ctime},{laststart},{laststop},{status},{smessage},{labels}')