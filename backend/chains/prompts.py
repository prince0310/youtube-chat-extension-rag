from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer ONLY using the provided transcript context.

If the answer is not present in the context, reply exactly:

"I don't know based on the provided transcript."

<context>
{context}
</context>

Question:
{input}

Answer:
"""
)