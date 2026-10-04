git rm -rf .
uv add langchain langchain-ollama langchain-openai python-dotenv black isort

Run in windows power sheel

irm https://ollama.com/install.ps1 | iex

ollama pull qwen3:1.7b
ollama run qwen3:1.7b

now run the ollama server in local machine 
ollama serve