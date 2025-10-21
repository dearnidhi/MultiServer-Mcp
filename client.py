import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

async def main():
    try:
        print("🚀 Starting DIRECT TOOL CALLS...")
        
        # Setup MCP client
        client = MultiServerMCPClient(
            {
                "math": {
                    "command": "python",
                    "args": ["mathserver.py"],
                    "transport": "stdio",
                },
                "texttools": {
                    "command": "python", 
                    "args": ["texttools.py"],
                    "transport": "stdio",
                }
            }
        )

        # Load tools
        print("📦 Loading tools from servers...")
        tools = await client.get_tools()
        print(f"✅ Tools loaded: {[tool.name for tool in tools]}")

        # DIRECT TOOL CALLS - NO AGENT
        print(f"\n🔧 Testing tools directly...")

        # Test math tools
        add_tool = [t for t in tools if t.name == "add"][0]
        result = await add_tool.ainvoke({"a": 15, "b": 25})
        print(f"✅ add(15, 25) = {result}")

        multiply_tool = [t for t in tools if t.name == "multiply"][0]
        result = await multiply_tool.ainvoke({"a": 8, "b": 12})
        print(f"✅ multiply(8, 12) = {result}")

        # Test text tools
        count_tool = [t for t in tools if t.name == "count_words"][0]
        result = await count_tool.ainvoke({"text": "hello world how are you"})
        print(f"✅ count_words('hello world how are you') = {result}")

        upper_tool = [t for t in tools if t.name == "uppercase_text"][0]
        result = await upper_tool.ainvoke({"text": "hello india"})
        print(f"✅ uppercase_text('hello india') = {result}")

        reverse_tool = [t for t in tools if t.name == "reverse_text"][0]
        result = await reverse_tool.ainvoke({"text": "python"})
        print(f"✅ reverse_text('python') = {result}")

        print(f"\n🎉 ALL DIRECT TOOL CALLS SUCCESSFUL!")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


















if __name__ == "__main__":
    asyncio.run(main())