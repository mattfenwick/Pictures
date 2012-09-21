import os


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


def makeRows(files):
    rows = []
    for row in files:
        # we need to escape the path and description, I think
        rows.append(''.join(['<tr><td>', 'no description', '</td><td><a href="', row, '">', row, '</a></td></tr>\n']))
    return ''.join(rows)


def getFiles():
    '''() -> [String]'''
    return ['europe/' + x for x in os.listdir('europe')]


def makeHTML():
    return ''.join([header, makeRows(getFiles()), footer])




if __name__ == "__main__":
    print makeHTML()
