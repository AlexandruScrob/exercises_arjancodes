import os

from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Country(BaseModel):
    capital: str = Field(description="capital of the country")
    name: str = Field(description="name of the country")


load_dotenv()

OPENAI_MODEL = "gpt-4"
OPEN_API_KEY = os.environ.get("OPEN_API_KEY")

PROMPT_COUNTRY_INFO = """
    Provide information about {country}.
    """

PROMPT_COUNTRY_INFO_FORMAT = """
    Provide information about {country}. If the country doesn't exist, make up something.
    {format_instructions}
    """


def main():
    # Set up a parser + inject instructions into the prompt template.
    parser = PydanticOutputParser(pydantic_object=Country)

    llm = ChatOpenAI(openai_api_key=OPEN_API_KEY, model=OPENAI_MODEL)

    # get user input
    country = input("Enter the name of a country:")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(country=country)

    response = llm(chat_prompt_with_values.to_messages())
    print(response)

    chat_prompt_with_values_format = chat_prompt.format_prompt(
        country=country, format_instructions=parser.get_format_instructions()
    )

    response = llm(chat_prompt_with_values_format.to_messages())
    data = parser.parse(response.content)
    print(f"The capital of {data.name} is {data.capital}")


if __name__ == "__main__":
    main()
