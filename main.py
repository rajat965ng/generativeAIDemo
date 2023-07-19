from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """   
Fund Name is Top 200 Fund provide returns of 33.07% in 3 Years, 21.52% in 5 Years and 19.21% in 10 Years.

Another Fund Name is CREST (Thematic Fund) provide returns of 27.58%% in 3 Years, 14.33% in 5 Years and 11.12% in 10 Years.
"""

if __name__ == "__main__":

    summary_template = """
        given information {information} about a mutual funds from I want you to create:
        1. a short summary
        2. two interesting facts about them  
        3. Which of them is a better option  
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))