import argparse

def int_to_hex_string(value, bits):
	# from here: https://stackoverflow.com/a/16427237/6609908
	return "{0:0{1}X}".format(value & ((1<<bits) - 1), bits//4)

def create(args) :
	hex_3_digits = '{:0>3X}'
	hex_2_digits = '{:0>2X}'
	message = hex_3_digits.format(args.node_id + (0x600 if args.sdo == 'transmit' else 0x580)) # node-id int to string hex with zeros to the left
	message += '#'

	command_byte = 0

	if args.flow == 'download': #write to server
		if args.size == None:
			raise ValueError('For download, size (-sz, --size) shouldn\'t be None')
		else:
			command_byte = 1 << 5
			command_byte |= ((4 - args.size) << 2)
			command_byte |= 1

			data = ''

			if args.data == None:
				raise ValueError('For download, data (-d, --data) shouldn\'t be None')
			else:
				if args.decimal: # data in decimal
					#print("data: ", args.data, int_to_hex_string(int(args.data),32))
					data = '{:0>8}'.format(int_to_hex_string(int(args.data), 32))
				else: # data in hexadecimal
					data = '{:0>8}'.format(args.data)

			data = '.'.join([data[i:i+2] for i in range(0,8,2)][::-1])

			command_byte |= int(not args.not_expedited) << 1


	else: # upload from server to client
		command_byte = 2 << 5
		#command_byte |= (4 << 2) # useless
		command_byte |= 0
		data = '00.00.00.00'

	message += hex_2_digits.format(command_byte)

	args.index = '{:0>4}'.format(args.index)
	message += '.' + args.index[2:] + '.' + args.index[:2]
	message += '.{:0>2}'.format(args.subindex)
	message += '.' + data
	print(message)

parser = argparse.ArgumentParser(description='Create or interpret SDO message from CANopen protocol')

subparser = parser.add_subparsers(help='Create or Interpret CANopen SDO message')

interpret_parser=subparser.add_parser('interpret')
interpret_parser.add_argument('message', help='CANopen SDO message to be interpreted in the format 123#45.67.89.0A.BC.DE.F1.23')

create_parser=subparser.add_parser('create')
create_parser.set_defaults(func=create)
create_parser.add_argument('node_id', type=int, metavar='1..127', choices=range(1,128), help='node\'s id in decimal')
create_parser.add_argument('-f', '--flow', required=True, choices=['download', 'upload'], help='indicates the message\'s flow direction: download to the server node (write to server node) or upload from server node (read from server node)')
create_parser.add_argument('-sdo', '--sdo', required=True, choices=['receive', 'transmit'], help='indicates if this message should be RECEIVED by this node id or TRANSMITED by this node id')
create_parser.add_argument('-sz', '--size', required=False, choices=range(5), type=int, help='size (in bytes) of the data to be transmitted in upload - write - messages ONLY (useless for download - read - messages)')
create_parser.add_argument('-ne', '--not-expedited', required=False, action='store_true', help='non-expedited message: not all the data is contained here (THIS IS NOT HANDLED HERE - DO NOT USE!)')
create_parser.add_argument('-i', '--index', required=True, help='index of Communication Object Identifier')
create_parser.add_argument('-si', '--subindex', required=True, help='subindex of Communication Object Identifier')
create_parser.add_argument('-d', '--data', required=False, help='data to be downloaded')
create_parser.add_argument('-dec', '--decimal', action='store_true', required=False, help='indicates that DATA is in decimal representation (hexadecimal is default)')

args = parser.parse_args()
args.func(args)
