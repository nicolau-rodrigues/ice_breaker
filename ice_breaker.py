import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    print("Hello LangChain")

    summary_template = """Given a LinkdIn information {information} about a person from, I want to create:
     1- a short summary
      2- two interesting facts about them  """

    sumary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = sumary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/helio-cola/")
    
    res = chain.invoke(input={"information": linkedin_data})
    
    print(res)
