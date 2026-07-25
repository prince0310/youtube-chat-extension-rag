# from dotenv import load_dotenv

# load_dotenv()

# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate

# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     temperature=0.2,
# )

# prompt = PromptTemplate(
#     template="""
# You are a helpful assistant.

# Answer ONLY using the provided transcript context.

# If the answer cannot be found in the context, simply say:
# "I don't know based on the provided transcript."

# Context:
# {context}

# Question:
# {question}

# Answer:
# """,
#     input_variables=["context", "question"],
# )

from Retrieval.retrieval import retrieve


def augment(query: str):

    docs = retrieve(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context