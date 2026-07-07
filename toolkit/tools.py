import os

from langchain.tools import tool
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults 
from data_models.models import RagToolSchema
from langchain_pinecone import PineconeVectorStore

from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()

@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """ this is a retiever tool"""
    return ""

@tool
def tavily_tool(question:str):
    """ this is a tavily tools"""
    return TavilySearchResults(
        question,
        max_results=5,
        search_depth="advanced",
        include_answer= True,
        include_raw_content=True
    )

@tool
def create_polygon_tool():
    """this is a polygon tool"""
    return PolygonFinancials(api_wrapper=PolygonAPIWrapper())

@tool
def create_bing_tool():
    """ this is a bing tool"""
    return BingSearchResults()


def get_all_tools(question):
    return [
        retriever_tool,
        tavily_tool,
        create_polygon_tool,
        create_bing_tool
 ]

if __name__ ==  '__main__':
    get_all_tools("myquestions")


