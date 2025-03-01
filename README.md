# 🤖 NLP Telegram Bot

A Telegram bot for summarizing Persian text using Natural Language Processing (NLP) libraries.

## 🎉 Features
- **Text Summarization** using methods like TF-IDF and PageRank  
- **Telegram Interaction** via commands  
- **Easy Installation and Setup** in a Python environment  

## 🔧 Prerequisites
- **Python 3.7+**  
- A Telegram Bot token (obtained from BotFather)  
- Install required libraries (listed in `requirements.txt`)

## 📦 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourUsername/nlp-telegram-bot.git
   ```
2. **Navigate to the project directory**  
   ```bash
   cd nlp-telegram-bot
   ```
3. **Create a virtual environment (optional but recommended)**  
   - On Unix-based systems (Linux/Mac):
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
4. **Install the required libraries**  
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure your bot token**  
   - Open `bot/config.py` and replace `TELEGRAM_BOT_TOKEN` with the token you received from BotFather.

6. **Run the bot**  
   ```bash
   python main.py
   ```
7. **Test and use**  
   - Open your Telegram bot.  
   - Send `/start` to receive a welcome message.  
   - Send `/summarize [Your text]` to get a summarized version of the text.

## 🏗️ Project Structure

```
nlp-telegram-bot/
├── bot/
│   ├── config.py           # Bot token and configurations
│   ├── handlers/           # Telegram handlers (start, summarize, etc.)
│   └── utils/              # Helper modules (summarizer.py, etc.)
├── main.py                 # Main entry point to run the bot
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── __init__.py
```

## 💡 Usage

- **`/start` command**  
  Starts the bot and sends a welcome message.
  
- **`/summarize` command**  
  Summarizes the provided text. In the basic version, the text should be in the same message after `/summarize`.  
  - Example:  
    ```
    /summarize In recent years, with the growth of new technologies...
    ```
  - For multi-line text, you can either put all text after `/summarize` in the same message or use a multi-step approach with `ConversationHandler`.

- **Reporting issues**  
  If you encounter any errors, check the terminal logs and ensure your bot token and internet connection are correct.

## 🤝 Contributing
1. Fork this repository.  
2. Create a new branch.  
3. Make your changes and commit them.  
4. Submit a Pull Request so your changes can be reviewed.

## 📝 License
This project is released under the [MIT](LICENSE) License. Contributions are welcome!  

> **Note:** For longer multi-line texts, consider using a `ConversationHandler` or put the entire text after `/summarize` in a single message.

Enjoy exploring the fascinating world of NLP! 🚀