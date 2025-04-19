import requests
import json

SERVER_URL = "http://localhost:8000/rpc"

def list_tools():
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/list",
        "id": 1
    }
    response = requests.post(SERVER_URL, json=payload)
    print("Tools:", response.json())

def call_tool(name):
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": name},
        "id": 2
    }
    response = requests.post(SERVER_URL, json=payload)
    print("Response:", response.json())

if __name__ == "__main__":
    list_tools()
    call_tool("Sri")
