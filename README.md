# LangChain Tutorial Project

This is a simple LangChain setup that demonstrates how to initialize and use a chat model.

## Setup

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Set up API keys:**
   You have two options:

   **Option A: Use a .env file (recommended)**
   Create a `.env` file in the project root with:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   LANGSMITH_API_KEY=your_langsmith_api_key_here  # optional
   LANGSMITH_PROJECT=default  # optional
   ```

   **Option B: Enter keys when prompted**
   Run the script and enter your API keys when prompted.

3. **Get your API keys:**
   - **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
   - **LangSmith API Key**: Get from [LangSmith](https://smith.langchain.com/) (optional, for tracing)

## Running the Project

```bash
python3 main.py
```

The script will:
1. Load environment variables from `.env` file (if it exists)
2. Prompt for any missing API keys
3. Initialize a GPT-4o-mini chat model
4. Test the model with a simple message
5. Display the response

## What's Working

✅ All required dependencies are installed  
✅ The code structure is correct  
✅ Environment variable handling is set up  
✅ The model initialization is working  

You just need to add your OpenAI API key to make it fully functional! 