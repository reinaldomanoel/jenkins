# Python Modules
import os
import argparse


if __name__ == "__main__":
    # Argument menu / parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-pass", "--airgap_pass", type=str, required=True,
                        help="Password of the Username with priveleges to deploy applications on target environment")
    args = parser.parse_args()

    airgap_pass = os.environ.get('ConanPwsAirGap')
    print("Temp Hash main airgap: "+ airgap_pass)
    
