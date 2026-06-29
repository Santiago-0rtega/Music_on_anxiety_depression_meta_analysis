import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
prompt = '''Using only Chen2019.pdf, answer in 5 bullets: title, animal species/strain, music exposure, control condition, and ethics approval. Include exact quotes.'''
async def main():
    params = StdioServerParameters(command='uv', args=['run','--directory',r'C:\Users\zannt\OneDrive\Github repos\notebooklm-mcp','notebooklm-mcp'], env={'NOTEBOOKLM_HEADLESS':'false'})
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool('query_notebook', {'notebook_id':'615bcf8e-a441-468a-ba63-2bd609d68b49', 'question':prompt})
            print(result.content[0].text)
asyncio.run(main())
