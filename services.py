from constants import (KWARG_MUNICIPALITY,KWARG_OPTIONAL, KWARG_ORGANIZATION, KWARG_TAG, KWARG_TAG_ATTRS)

def unpackArgs(kwargs):
    return [kwargs.get(KWARG_ORGANIZATION),
            kwargs.get(KWARG_MUNICIPALITY),
            kwargs.get(KWARG_TAG),
            kwargs.get(KWARG_TAG_ATTRS),
            kwargs.get(KWARG_OPTIONAL)]

def validateArgs(listingOrganization, listingMunicipality, tag, tagAttributes):
    if(listingOrganization == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_ORGANIZATION))
    if(listingMunicipality == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_MUNICIPALITY))
    if(tag == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_TAG))
    if(tagAttributes == None):
        raise ValueError("Missing argument ({arg})".format(arg=KWARG_TAG_ATTRS))

def writeContentToFile(content):
    with open('batch_file.txt', 'a') as batch_file:
        batch_file.write('{content}\n'.format(content=content))
        batch_file.close()