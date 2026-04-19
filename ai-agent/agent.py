"""
MyInfraHub - AI Agent
Built using Google ADK (AI Development Kit) with Gemini AI
"""

import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')


def infra_agent(user_query):
    """
    AI Agent that answers infrastructure-related questions
    using Google Gemini AI through Google ADK
    """
    
    system_prompt = """
    You are MyInfraHub AI Assistant - an expert in infrastructure,
    cloud computing, DevOps, networking, servers, and IT operations.
    Provide clear, accurate, and helpful answers.
    Keep responses concise and practical.
    """
    
    full_prompt = f"{system_prompt}\n\nUser Question: {user_query}"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to run the AI agent"""
    print("=" * 50)
    print("  MyInfraHub AI Assistant")
    print("=" * 50)
    print("Ask me anything about infrastructure!")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Thanks for using MyInfraHub! Goodbye!")
            break
        
        if not user_input:
            print("Please enter a question.\n")
            continue
        
        print("\nAI Assistant:", infra_agent(user_input))
        print()


if __name__ == "__main__":
    main()
