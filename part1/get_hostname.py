from ncclient import manager
import sys
import xml.dom.minidom

HOST='10.1.98.176'
PORT=380
USER='cisco1'
PASS='cisco1'

def main():
	with manager.connect(host=HOST,port=PORT,username=USER,password=PASS, hostkey_verify = False, device_params = {'name':'default'},look_for_keys=False,allow_agent=False) as m:
	print("***Below listed are the remote devices capabilities***")
	for capability in m.server_capabilities:
		print(capability.split('?')[0])

	hostname_filter = ""
				<filter>
					<native xmlns=""http://cisco.com/ns/yang/Cisco-ISO_XE_native"">
		<hostname></hostname>
		</native>

				</filter>

			""

result = m.get_config('running', hostname_filter)
xml_doc = xml.dom.minidom.parseString(result.xml)
hostname = xml_doc.getElementsByTagName("hostname")
print(hostname[0].firstChild.nodeValue)

if __name__=='__main__':
	sys.exit(main())





