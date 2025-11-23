import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

# 1. Define the Server Configuration
# Since we are using 'npx', the transport is "stdio" (local process), not "http".
MCP_SERVERS = {
    "airbnb": {
        "transport": "stdio", 
        "command": "npx",
        "args": ["-y", "@openbnb/mcp-server-airbnb"]
    }
}

async def main():
    print("🛫 Initiating connection to Airbnb MCP Server...")
    
    # 2. Initialize the Client
    # This will silently start the 'npx' process in the background
    client = MultiServerMCPClient(MCP_SERVERS)

    try:
        # 3. Fetch Tools
        # This is the actual "Ping" test. If this works, the server is running.
        print("🔎 Querying available tools...")
        tools = await client.get_tools()

        if tools:
            print(f"\n✅ Connection Successful! Found {len(tools)} tools:")
            print("-" * 40)
            for tool in tools:
                # Print tool name and a short snippet of description
                desc = tool.description.replace("\n", " ")[:60] if tool.description else "No description"
                print(f"🔹 {tool.name}: {desc}...")
            print("-" * 40)
        else:
            print("\n⚠️  Connected, but no tools were returned.")

    except Exception as e:
        print(f"\n❌ Connection Failed.")
        print(f"Error: {e}")
        print("\nTroubleshooting Tips:")
        print("1. Do you have Node.js installed? (Run `node -v` in terminal)")
        print("2. Can you run the command manually? (Try running `npx -y @openbnb/mcp-server-airbnb` in terminal)")

if __name__ == "__main__":
    asyncio.run(main())