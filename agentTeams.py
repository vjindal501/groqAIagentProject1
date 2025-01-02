from phi.agent import Agent
from phi.llm.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="web agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data, and dont truncate the data"]
    # ,debug_mode=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"), #if model is not provide it will use default model "gpt-4o" for now which is paid tier1
    instructions=["Always include sources", "use tables to display data"],
    markdown=True,
    show_tool_calls=True
)

agent_team.print_response("summarize analyst recommendations and share the latest news for GRMN", stream=True)