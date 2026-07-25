# from dotenv import load_dotenv
# import traceback

# load_dotenv()

# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate

# from Augmentation.augmentation import augment


# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     temperature=0.2,
# )

# prompt = PromptTemplate(
#     template="""
# You are a helpful AI assistant.

# Answer ONLY from the provided transcript context.

# If the answer is not contained in the context, reply:

# "I don't know based on the provided transcript."

# Context:
# {context}

# Question:
# {question}

# Answer:
# """,
#     input_variables=["context", "question"],
# )

# chain = prompt | llm


# while True:

#     question = input("\nAsk Question (type 'exit' to quit): ")

#     if question.lower() == "exit":
#         break

#     try:
#         print("\n[Step 1] Retrieving relevant chunks...")

#         context = augment(question)

#         print("[✓] Retrieval completed.")
#         print(f"[INFO] Context length: {len(context)} characters")

#         print("\n[Step 2] Sending prompt to Groq...")

#         response = chain.invoke(
#             {
#                 "context": context,
#                 "question": question,
#             }
#         )

#         print("[✓] LLM response received.")

#         print("\nAnswer:\n")
#         print(response.content)
#         print("-" * 100)

#     except Exception as e:
#         print("\n❌ ERROR OCCURRED")
#         print(f"Type: {type(e).__name__}")
#         print(f"Message: {e}")

#         print("\nFull traceback:\n")
#         traceback.print_exc()

from chains.rag_chain import rag_chain

while True:

    question = input("\nAsk Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    response = rag_chain.invoke(
        {
            "input": question
        }
    )

    print("\nAnswer:\n")
    print(response["answer"])
    print("-" * 100)