# from phi.agent import Agent 
# from phi.model.groq import Groq  # Use Groq instead of OpenAI
# from phi.tools.yfinance import YFinanceTools 
# from phi.tools.duckduckgo import DuckDuckGo
# import openai
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Set OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Initialize the Web Search Agent
# web_search_agent = Agent(
#     name="Web Search Agent",
#     role="Search the web for information",
#     model=Groq(id="llama-3.3-70b-versatile"),  # Use Groq model here
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources"],
#     show_tools_calls=True,
#     markdown=True,
# )

# # Initialize the Finance AI Agent
# finance_agent = Agent(
#     name="Finance AI Agent",
#     role="Search the web for financial information",
#     model=Groq(id="llama-3.3-70b-versatile"),  # Use Groq model here
#     tools=[
#         YFinanceTools(
#             stock_price=True, 
#             analyst_recommendations=True, 
#             stock_fundamentals=True,
#             company_news=True
#         ),
#     ],
#     instructions=["Use tables to display the data"],
#     show_tools_calls=True,
#     markdown=True,
# )

# # Multi-agent system that combines both agents
# multi_ai_agent = Agent(
#     team=[web_search_agent, finance_agent],
#     model=Groq(id="llama-3.3-70b-versatile"),  # Use Groq model here
#     instructions=["Always include sources", "Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# # Request for the agent to summarize the analyst recommendation and share the latest news for NVDA
# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)

# import streamlit as st
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# import openai
# import os
# from dotenv import load_dotenv
# import pprint

# # Load environment variables
# load_dotenv()

# # Set OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Initialize the Web Search Agent
# web_search_agent = Agent(
#     name="Web Search Agent",
#     role="Search the web for information",
#     model=Groq(id="llama-3.2-3b-preview"),
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources"],
#     show_tools_calls=True,
#     markdown=True,
# )

# # Initialize the Finance AI Agent
# finance_agent = Agent(
#     name="Finance AI Agent",
#     role="Search the web for financial information",
#     model=Groq(id="llama-3.2-3b-preview"),
#     tools=[
#         YFinanceTools(
#             stock_price=True, 
#             analyst_recommendations=True, 
#             stock_fundamentals=True,
#             company_news=True
#         ),
#     ],
#     instructions=["Use tables to display the data"],
#     show_tools_calls=True,
#     markdown=True,
# )

# # Multi-agent system that combines both agents
# multi_ai_agent = Agent(
#     team=[web_search_agent, finance_agent],
#     model=Groq(id="llama-3.2-3b-preview"),
#     instructions=["Always include sources", "Use tables to display data"],
#     show_tools_calls=True,
#     markdown=True,
# )

# # Streamlit UI
# st.title("AI Financial Analysis & Web Search")

# st.header("Request for Financial Analysis or Web Search")
# query = st.text_input("Enter your query:")

# # Add a help text to explain input expectations
# st.markdown("""
#     **Tip**: You can ask for:
#     - Financial stock information, like analyst recommendations or latest news (e.g., `NVDA stock recommendation`).
#     - Web search for the latest news or trending topics (e.g., `latest news on AI`).
# """)

# if st.button("Get Response"):
#     if not query.strip():
#         st.warning("Please enter a valid query.")
#     else:
#         with st.spinner("Processing your request..."):
#             try:
#                 # Execute the query using the multi-agent system
#                 response = multi_ai_agent.run(query)  # Replace run with the correct method if needed
                
#                 # Pretty print the response using pprint
#                 pp = pprint.PrettyPrinter(indent=4)
#                 formatted_response = pp.pformat(response)  # Format the response for better readability
                
#                 st.success("Query completed!")
                
#                 # Display the formatted response
#                 st.markdown("### Response:")
#                 st.code(formatted_response, language='json')
                
#             except AttributeError as e:
#                 st.error(f"An error occurred: {e}")
#             except Exception as e:
#                 st.error(f"An unexpected error occurred: {e}")






import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=False,
    markdown=True,
)

# Initialize the Finance AI Agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Search the web for financial information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            stock_fundamentals=True,
            company_news=True
        ),
    ],
    instructions=["Use tables to display data concisely"],
    show_tools_calls=False,
    markdown=True,
)

# Multi-agent system that combines both agents
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Focus on concise responses"],
    show_tools_calls=False,
    markdown=True,
)

# Streamlit UI
st.title("AI Agent for Financial Analysis & Web Search")

st.header("Request Financial Analysis or Latest News")
query = st.text_input("Enter your query:")

st.markdown("""
    **Tip**: Queries can include:
    - Analyst recommendations (e.g., `Tesla stock recommendation`)
    - Latest news (e.g., `latest news on Tesla`)
""")

if st.button("Get Response"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Processing your request..."):
            try:
                # Execute the query using the multi-agent system
                response = multi_ai_agent.run(query)  # Adapt the method as necessary
                
                # Extract and display the relevant part of the response
                if response:
                    st.markdown(f"### Response:\n{response}")
                else:
                    st.info("No relevant information found.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

