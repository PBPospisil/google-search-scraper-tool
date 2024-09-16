from constants import (KWARG_MUNICIPALITY,
                       KWARG_ORGANIZATION,
                       KWARG_TAG,
                       KWARG_TARGET_ATTRS,
                       KWARG_PATTERN,
                       KWARG_OPTIONAL)

def unpackArgs(kwargs):
    return [kwargs.get(KWARG_ORGANIZATION),
            kwargs.get(KWARG_MUNICIPALITY),
            kwargs.get(KWARG_TAG),
            kwargs.get(KWARG_TARGET_ATTRS),
            kwargs.get(KWARG_PATTERN),
            kwargs.get(KWARG_OPTIONAL)]

def validateArgs(listingOrganization, listingMunicipality):
    if(listingOrganization is None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_ORGANIZATION))
    if(listingMunicipality is None):
        raise ValueError("Invalid argument ({arg})".format(arg=KWARG_MUNICIPALITY))

def writeContentToFile(content):
    with open('batch_file.txt', 'a') as batch_file:
        batch_file.write('{content}\n'.format(content=content))
        batch_file.close()