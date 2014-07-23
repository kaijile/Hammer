#!/usr/bin/python2.7
#coding:utf-8

import os
#from lib.nmap_class import NmapScanner

info = {
	'NAME':'Port and Service Discover',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':''
}
#print locals()
#print globals()
def Audit(services):
	# print locals()
	# print globals()
	output = ''
	if services.has_key('ip'):
		output += 'plugin run' + os.linesep
		ip = services['ip']
		np = NmapScanner(ip)
		sc = np.scanPorts()
		#print sc
		try:
			services['ip'] = sc.keys()[0]
			services['ports'] = []
			services['port_detail'] = {}
			if sc[sc.keys()[0]].has_key('tcp'):
				services['port_detail'].update(sc[sc.keys()[0]]['tcp'])
				for eachport in sc[sc.keys()[0]]['tcp']:
					services['ports'].append(eachport)
			if sc[sc.keys()[0]].has_key('udp'):
				services['port_detail'].update(sc[sc.keys()[0]]['udp'])
				for eachport in sc[sc.keys()[0]]['udp']:
					services['ports'].append(eachport)

			#print 'services:\t',services
			output += 'services:\t' + str(services) + os.linesep
			retinfo = {'level':'info','content':str(services['ports'])}

		except IndexError,e:
			print 'IndexError:',e
			output += 'IndexError: ' + str(e) + os.linesep
		except KeyError,e:
			print 'KeyError:',e
			output += 'KeyError: ' + str(e) + os.linesep
	else:
		output += 'plugin does not run' + os.linesep

	return (None,output)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	from dummy import *
	services={'ip':'124.160.91.86'}
	print Audit(services)
	pprint(services)