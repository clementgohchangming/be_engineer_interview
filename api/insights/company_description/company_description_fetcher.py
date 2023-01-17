import random
import time


def get_company_description(domain: str) -> str:
    # This mocks a db call
    # sleep for 1 to 2 seconds randomly to simulate a slow db call
    time.sleep(random.randint(1, 2))
    return f"This is a description of {domain}"
