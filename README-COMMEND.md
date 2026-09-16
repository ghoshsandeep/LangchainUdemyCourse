if __name__=="__main__":
   main()

uv run jupyter lab 
uv run python env_utils.py
uv sync


git remote set-url origin https://github.com/ghoshsandeep/LangchainUdemyCourse.git
git checkout -b hello-world
git rm -rf .

uv init
uv add langchain
uv add langchain-openai
uv add python-dotenv
uv add python-dotenv black isort (simply to format the code here and there)  
uv add langchain-ollama
black .
isort .

irm https://ollama.com/install.ps1 | iex past this in window shell to install Ollama

ollama pull gemma3:270m
ollama run gemma3:270m

ollama pull gemma3:1b

