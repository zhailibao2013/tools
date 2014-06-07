import os
from optparse import OptionParser
from jinja2 import Environment,FileSystemLoader
from ConfigParser import ConfigParser
    
parser = OptionParser() 
parser.add_option("-t", "--template", dest="tplfile", 
                  default='windows.html',help="the template of config file") 
parser.add_option("-w", "--output", dest="outputf", 
                  default='window.cfg',help="the output config file") 
(options, args) = parser.parse_args()
cf = ConfigParser()
if os.path.exists('config.ini'):
    cf.read('config.ini')
else:
    print 'config.ini not found'
vars={}
for name in cf.options('main'):
    vars[name]=cf.get('main',name)

jinja_templates = os.path.join(os.path.dirname(__file__),'./templates')
#print jinja_templates
env = Environment(loader=FileSystemLoader(jinja_templates))
with open(options.outputf,'w') as f:
    f.write(env.get_template(options.tplfile).render(vars=vars))
