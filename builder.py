import os
import json


header = '''
<!doctype html>
<html>
 <head>
    <title>Pictures</title>
    <link rel="stylesheet" type="text/css" href="style.css" />
 </head>
<body>
 <table>
  <thead><!-- what's the element name? -->
   <tr><th>Description</th><th>Picture</th></tr>
  </thead>
  <tbody>
'''

footer = '''
  </tbody>
 </table>
</body>
</html>'''


###################
## reading from the file system

def readPictures():
    '''() -> Error [String]'''
    return ['europe/' + x for x in os.listdir('europe')]


def readJson():
    '''() -> Error JsonObject'''
    with open('descriptions.json', 'r') as j: # does this throw if the file isn't there?
        jsObj = json.loads(j.read())
    return jsObj
    

def checkContents(jsObj):
    '''JsonObject -> Error (Map String String)'''
    out = {}
    if not isinstance(jsObj, dict):
        raise TypeError("wanted a dict, but got " + type(jsObj))
    for (k, v) in jsObj.iteritems():
        if (not isinstance(k, basestring)) or (not isinstance(v, basestring)):
            raise TypeError("wanted strings for keys and values, got " + str((k, v)))
        out['europe/IMG_' + k + '.JPG'] = v
    return out
    
###################
##
    
def getDescriptions():
    '''() -> Error (Map String String)'''
    jsObj = readJson()
    return checkContents(jsObj)
    
    
def checkMatch():
    '''() -> Error (Map String String)'''
    files = readPictures()
    descs = getDescriptions()
    for f in files:
        if f not in descs:
            raise ValueError("found file that doesn't have a description: " + f + json.dumps(descs))
    fileSet = set(files)
    for (k, _) in descs.iteritems():
        if k not in fileSet:
            raise ValueError("found description that doesn't have a file: " + k)
    # if no exception thrown, done
    return descs
    

def makeRows(descs):
    '''Map String String -> [String]'''
    rows = []
    for (name, desc) in sorted(descs.iteritems(), key=lambda (key, val): key):
        # we need to escape the path and description, I think
        rows.append(''.join(['<tr><td>', desc, '</td><td><a href="', name, '">', name, '</a></td></tr>\n']))
    return ''.join(rows)


def makeHTML():
    data = checkMatch()
    return ''.join([header, makeRows(data), footer])




if __name__ == "__main__":
    print makeHTML()
