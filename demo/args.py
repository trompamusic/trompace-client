import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--print", help="Print the generated mutations", action="store_true")
parser.add_argument("-s", "--submit", help="Submit the generated mutations to a CE", action="store_true", default=True)

args = parser.parse_args()