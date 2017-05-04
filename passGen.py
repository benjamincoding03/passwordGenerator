#!/usr/bin/python
import sys, argparse, random, string

def main():
	try:
		p = argparse.ArgumentParser(description = 'Random password generator')
		req = p.add_argument_group('required arguments')
		req.add_argument('-l', '--length', dest='length', help = 'Length of password')
		args = p.parse_args()
		length = int(args.length)
		# gets desired length of password

		charset = string.ascii_letters + string.digits + '!@#$%^&*()'
		passwd = (''.join(random.choice(charset) for i in range(length)))
		# creates charset and makes password

		print passwd
		sys.exit()

	except ValueError:
		print 'Entered length must be an integer'
		sys.exit()

	except TypeError:
		print 'Enter a value'
		sys.exit()

main()

