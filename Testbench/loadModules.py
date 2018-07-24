'''
Example file that loads all modules.
If one or more of the modules do not load properly, i.e., they are not found,
the function will give you a warning.

How to run testbech files:
from top level directory:
python3 -m Testbench.loadModules
'''

from Modules import *

try:
    ''' initialize genetic algorithm '''
    WH = Warehouse.Warehouse()
    ''' initialize genetic algorithm '''
    RT = Routing.Routing()
    ''' initialize genetic algorithm '''
    GA = GA.GA()
    ''' initialize genetic algorithm '''
    OM = OrderModule.OrderModule()

    print ("All modules loaded successfully")
except:
     print ("Could not load some modules")
