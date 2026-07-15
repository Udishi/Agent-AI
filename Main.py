from agent import Agent

def main():

    agent = Agent()

    print("="*50)
    print("🤖 Local AI Agent (Llama 3)")
    print("="*50)

    while True:

        user = input("\nYou: ")

        if user.lower() == "exit":
            break

        response = agent.run(user)

        print("\nAgent:", response)

if __name__ == "__main__":
    main()
