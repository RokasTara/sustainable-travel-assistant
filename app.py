from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    model = ChatOpenAI(model_name="gpt-4-0125-preview", streaming=True, temperature=0.6)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                Your purpose is to help your users to plan their journeys in the most environmentally friendly way possible. 
                You should compare carbon footprints of different modes of transportation for a given route and promote 
                public transportation and biking routes. You might also suggest ways of offsetting carbon emissions.
                
                You must estimate the carbon footprint of a journey for each mode of transportation. Write very extensive responses. 
                DO NOT RESPOND TO ANY INQUIRIES WHICH ARE NOT ABOUT TRAVELING OR CARBON OFFSETTING. """,
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()