#!/usr/bin/python3
# Helper script JSON file modifier

import argparse
import json

parser = argparse.ArgumentParser(prog="Config Modifier")

parser.add_argument("-p", "--django_super_user_password")
parser.add_argument("-e", "--django_super_user_email")
parser.add_argument("-u", "--django_user_password")
parser.add_argument("-w", "--django_user_email")
parser.add_argument("-k", "--production_secret_key")
parser.add_argument("-l", "--local_secret_key")
parser.add_argument("-d", "--production_database_password")
parser.add_argument("-f", "--local_database_password")

args = parser.parse_args()

print(f"{args=}")

json_data = json.load(open("console/scantron_secrets.json", "r", encoding="latin1"))

if args.django_super_user_password is not None:
    json_data["django_super_user_password"] = args.django_super_user_password

if args.django_super_user_email is not None:
    json_data["django_super_user_email"] = args.django_super_user_email

if args.django_user_password is not None:
    json_data["django_user_password"] = args.django_user_password

if args.django_user_email is not None:
    json_data["django_user_email"] = args.django_user_email

if args.production_secret_key is not None:
    json_data["production"]["SECRET_KEY"] = args.production_secret_key

if args.local_secret_key is not None:
    json_data["local"]["SECRET_KEY"] = args.local_secret_key

if args.production_database_password is not None:
    json_data["production"]["DATABASE_PASSWORD"] = args.production_database_password

if args.local_database_password is not None:
    json_data["local"]["DATABASE_PASSWORD"] = args.local_database_password
