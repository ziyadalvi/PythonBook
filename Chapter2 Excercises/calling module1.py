print('Import:')
import module1

print('Reload')
from imp import reload
reload(module1)

print('exec:')
exec(open('module1.py').read())
