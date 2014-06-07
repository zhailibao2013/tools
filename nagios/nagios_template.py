#!/usr/bin/env python
# create nagios config using jinja2 template,must exist of template and config.ini
#author:zhailibao
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

jinja_templates = os.path.join(os.path.dirname(__file__),'./templates')
#print jinja_templates
hosts=[]
default={}
#item = type('item',(object,),dicts)
for item in cf.options('main'):
    default[item]=cf.get('main',item)

for section in cf.sections():
    vars={}
    if section != 'main':
        for item in cf.options(section):
            vars[item]=cf.get(section,item)
    ##mergedict
    
    if vars:
        mergedict = default.copy()
        mergedict.update(vars)
    #hosts.append(type('item',(object,),vars))
        #http://www.yihaomen.com/article/python/319.htm,Dynamic create class method
        hosts.append(type('item',(object,),mergedict))
env = Environment(loader=FileSystemLoader(jinja_templates))
with open(options.outputf,'w') as f:
    f.write(env.get_template(options.tplfile).render(hosts=hosts))
