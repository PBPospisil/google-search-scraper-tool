from constants import (KWARG_MUNICIPALITY,KWARG_OPTIONAL, KWARG_ORGANIZATION, KWARG_TARGET_ATTRS)
import json

def unpackArgs(kwargs):
    attrsJson = kwargs.get(KWARG_TARGET_ATTRS)
    if attrsJson:
        try:
            targetAttributes = json.loads(attrsJson)
        except:
            raise ValueError("Invalid argument (attrs): error encountered while loading json")
        
    return [kwargs.get(KWARG_ORGANIZATION),
            kwargs.get(KWARG_MUNICIPALITY),
            targetAttributes,
            kwargs.get(KWARG_OPTIONAL)]

def validateArgs(listingOrganization, listingMunicipality):
    if(listingOrganization is not None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_ORGANIZATION))
    if(listingMunicipality is not None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_MUNICIPALITY))

def writeContentToFile(content):
    with open('batch_file.txt', 'a') as batch_file:
        batch_file.write('{content}\n'.format(content=content))
        batch_file.close()