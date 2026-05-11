import os
# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_question(question: str):
    response = client.responses.create(
        model="gpt-5",

        reasoning={
            "effort": "medium"
        },

        input=[
            # ROLE PROMPTING
            {
                "role": "developer",
                "content": ROLE_PROMPT
            },

            # FEW-SHOT EXAMPLES
            *FEW_SHOT_EXAMPLES,

            # ACTUAL USER QUESTION
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.output_text


if __name__ == "__main__":
    print("Smart Q&A Assistant Started")
    print("Type 'exit' to quit")

    while True:
        user_question = input("Ask Question: ")

        if user_question.lower() == "exit":
            break

        try:
            answer = ask_question(user_question)

            print("AI Response:")
            print(answer)
            print("-" * 50)

        except Exception as e:
            print(f"Error: {e}")
