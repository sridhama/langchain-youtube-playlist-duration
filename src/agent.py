from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, tools
from langchain.agents import AgentType, Tool
from ytpd import get_total_playlist_duration

OPENAI_API_KEY = 'YOUR_API_KEY_HERE'

@tool
def ytpd(playlist_url: str) -> str:
    """Returns the duration of YouTube playlist with URL {playlist_url}. \
    Use this tool for any questions related to finding the duration of a \
    YouTube playlist. The input is {playlist_url} the URL to the YouTube \
    playlist, and the output is the playlist duration as a string in the \
    `HH:MM:SS` format."""
    return get_total_playlist_duration(playlist_url)

tools = [Tool(name = "YTPD",
              func=ytpd,
              description="Returns the duration of YouTube playlist with URL {playlist_url}. \
                    Use this tool for any questions related to finding the duration of a \
                    YouTube playlist. The input is {playlist_url} the URL to the YouTube \
                    playlist, and the output is the playlist duration as a string in the \
                    `HH:MM:SS` format."
              )]

llm = ChatOpenAI(temperature=0,
                 openai_api_key=OPENAI_API_KEY)

agent = initialize_agent(tools, llm, 
                         agent=AgentType.OPENAI_FUNCTIONS,
                         verbose=True)

playlist_urls = ['https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab',
                 'https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr',
                 'https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi'
                 ]

agent.run(f'What is the duration of all three playlists combined? Here are the links to the playlists: {playlist_urls[0]} and {playlist_urls[1]} and {playlist_urls[2]}')