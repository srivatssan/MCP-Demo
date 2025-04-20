# 🧠 Model Context Protocol (MCP) Example – Python Implementation

This repository provides a minimal yet functional example of the **Model Context Protocol (MCP)** using Python. It demonstrates how a Large Language Model (LLM) agent can communicate with enterprise systems through a standardized client-server interface using **JSON-RPC** over **HTTP**, including support for **Server-Sent Events (SSE)**.

You can read my blog to understand the subject better: https://srivatssan.medium.com/model-context-protocol-exhaustively-explained-f5a30a87a3ff?sk=1b971265640303c66b04377371c82102 

---

## 📦 Repository Structure

```
mcp-protocol-example/
├── client/
│   └── main.py       # Python MCP client using JSON-RPC
├── server/
│   └── main.py       # FastAPI-based MCP server with /rpc and /events endpoints
```

---

## 🚀 How to Run This Example

### 1️⃣ Start the Server

Make sure you have FastAPI and Uvicorn installed:

```bash
pip install fastapi uvicorn
```

Then, start the MCP server:

```bash
cd server
uvicorn main:app --reload
```

This starts a FastAPI server with:
- `POST /rpc`: JSON-RPC handler for tool listing and invocation
- `GET /events`: Simulated SSE endpoint emitting heartbeat messages every 5 seconds

---

### 2️⃣ Run the Client

Install the required Python requests package:

```bash
pip install requests
```

Then run the client to interact with the server:

```bash
cd client
python main.py
```

Output:
```
Tools: [{'name': 'greet', 'description': 'Greets the user', ...}]
Response: {'message': 'Hello, Sri!'}
```
You can run http://localhost:8000/events
and you should see the heartbeat event being returned
like the one shown below. 

_data: {'event': 'heartbeat'}

data: {'event': 'heartbeat'}
_
...


****
---


## ⚙️ What It Demonstrates

- A basic MCP server exposing tools via `tools/list` and `tools/call`
- A client sending JSON-RPC requests to list and call tools
- Simulated real-time connection using `/events` SSE endpoint
- Modular structure ready to extend for `resources/` and `prompts/` support

---

## 🧩 Next Steps

You can expand this prototype by:
- Adding more tools with different schemas
- Supporting `resources/list` and `resources/read`
- Managing prompt templates with `prompts/get`
- Implementing authentication and access control
- Handling streaming responses from server to client

---

## 📚 References

- [Model Context Protocol (official site)](https://modelcontextprotocol.io)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Server-Sent Events (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

---

Created with ❤️ by [Srivatssan Srinivasan](https://www.linkedin.com/in/srivatssan)
