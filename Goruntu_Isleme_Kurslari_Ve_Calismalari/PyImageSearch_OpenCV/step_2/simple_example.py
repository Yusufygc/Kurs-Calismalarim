import argparse
# argparse: komut satırı argümanlarını ayrıştırmak için kullanılan bir modül
# pratik olması için kullanıcıyı selamlayan bir kod satırı.
# girdi termnalde yazılırken --name "Name" şeklinde yazılmalıdır.
# HOW TO RUN THIS SCRIPT: open cmd write the file path and work this -> python simple_example.py --name "Name"

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))