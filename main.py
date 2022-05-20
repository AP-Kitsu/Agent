import data.mongo_setup as mongo_setup
import data.scriptps1 as get_computerinfo

def main():
    mongo_setup.global_init()  # Inizio Del Database
    get_computerinfo()

