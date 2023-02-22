from .models import *
import re

import logging

logger = logging.getLogger(__name__)

def determine_type(data):
    if "\t" in data:
        return 0
    else:
        return 1

def parse_dscan(data):
    shipCount = {}
    solarSystem = ""

    data = data.replace("\r", "")

    data_split = data.split("\n")
    for l in data_split:
        l = l.split("\t")
        
        id_int = int(l[0])

        if not shipCount.get(id_int, False):
            shipCount[id_int] = 1

        else:
            shipCount[id_int] += 1
        
        if len(solarSystem) == 0:
            solarSystem = get_system(l)
            print(solarSystem)


def get_system(line):
    solarSystem = ""
    
    SOLAR_SYSTEM_IDENTIFIERS = [6, 7, 8, 9, 15, 1657, 1404, 1406, 1025]
    solarSystemIdTypes = InvType.objects.filter(groupID__in=SOLAR_SYSTEM_IDENTIFIERS).values_list("typeID", flat=True)

    if line[0] in solarSystemIdTypes:
        logger.info("Grabbing solar system name")
        # Check cits for solar name
        matches = re.match(r'([A-z0-9\- ]+?) -', line[1])
        if matches:
            solarSystem = matches.group(1)
            #print(solarSystem)

        matches = re.match(r'([A-z0-9\- ]+) [XVI]+', line[1])
        if matches:
            solarSystem = matches.group(1)
            #print(solarSystem)

        matches = re.match(r'Customs Office \(([A-z0-9\- ]+) [XVI]+\)', line[1])
        if matches:
            solarSystem = matches.group(1)
            #print(solarSystem)

    return solarSystem


