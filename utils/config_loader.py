import yaml

def load_config(config_path: str = r"F:\\RAG_Tuto\\customer-support-system\\agentic-tading-bot\\config\\config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

# F:\RAG_Tuto\customer-support-system\agentic-tading-bot

# import os
# import yaml

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# config_path = os.path.join(BASE_DIR, "config", "config.yaml")

# with open(config_path, "r") as file:
#     config = yaml.safe_load(file)