import requests
import argparse

parser = argparse.ArgumentParser("Fliesenleger des Königs")
parser.add_argument("url", help="The URL to the website", type=str)
parser.add_argument("filename", help="The filename", type=str)
args = parser.parse_args()

response = requests.get (f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={args.url}")

with open(f"{args.filename}.png", "wb") as file:
    file.write(response.content)