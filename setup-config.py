import os
from typing import Dict
import yaml


def main():
    # load config
    with open(os.getcwd() + "/config-example.yaml") as f:
        config: Dict = yaml.safe_load(f)

    fee = input("Would you like to use a fee, if you do then enter the fee in mojo: Note if you have a fee then the pool will need to connect to a wallet: ")
    if fee != "":
        config["block_claim_fee"] = int(fee)
        config["wallet_id"] = int(input("What is the wallet id you would like to receive the rewards at?, this must match the wallet address you will enter later: "))
        config["wallet_fingerprint"] = int(input("What is the wallet fingerprint for this wallet ID?"))
    config["default_target_address"] = input("What is the wallet address you would like to receive the rewards at? :")
    config["pool_url"] = 'http://' + input("what is the ip address or domain of the server that you are running the solo-pool on? :")
    # save config
    with open(os.getcwd() + "/config.yaml", mode="w") as f:
        yaml.safe_dump(config, f)


if __name__ == "__main__":
    main()
