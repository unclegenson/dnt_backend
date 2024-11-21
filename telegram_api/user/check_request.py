import hmac
import hashlib
import json
import time
from urllib.parse import parse_qs, unquote



def validate_telegram_data(data):
    # Step 1: Parse the data string to extract fields and values
    bot_token = "token"  # Replace with your bot's token
    current_timestamp = int(time.time())

    parsed_data = parse_qs(data)

    username = json.loads(parsed_data["user"][0])["username"]
    user_id = json.loads(parsed_data["user"][0])["id"]
    auth_stamp = parsed_data.get('auth_date', [None])[0]  # Get the first element or None if not found
    difference = abs(current_timestamp - int(auth_stamp))

    #print(f"Current: {current_timestamp}, receive: {auth_stamp}, Diff: {difference}")

    if(difference>12):
        return False,0,0


    received_hash = parsed_data.pop('hash')[0]  # Extract and remove the hash from parsed data
    # Step 2: Sort the fields alphabetically and create the data_check_string
    data_check_string = '\n'.join(f"{key}={unquote(value[0])}" for key, value in sorted(parsed_data.items()))

    # Step 3: Generate the secret key using the bot's token and "WebAppData"
    secret_key = hmac.new(key=b"WebAppData", msg=bot_token.encode(), digestmod=hashlib.sha256).digest()

    # Step 4: Compute the HMAC-SHA256 signature of the data_check_string using the secret key
    computed_hash = hmac.new(key=secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256).hexdigest()


    # Step 5: Compare the computed hash with the received hash
    return computed_hash == received_hash , username,user_id
