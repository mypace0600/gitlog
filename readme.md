# 🤖 AI-Powered Daily Git Commit Summarizer

This Python script fetches all commits made by a specific author for the current day from a designated Git repository and uses the Gemini CLI to automatically generate a professional daily work summary in Markdown.

Instead of struggling to remember what you did all day, simply run this script before logging off to easily prepare your daily work report.

## ✨ Key Features

- **Daily Commit Aggregation**: Automatically fetches all commit logs since midnight for a specific author using `git log`.  
- **AI-Powered Summarization**: Uses Gemini CLI to generate a professional summary that consolidates duplicates and highlights key tasks.  
- **Markdown Export**: Saves the generated summary to the specified output directory as a `YYYY-MM-DD_summary.md` file.  

## ⚠️ Prerequisites

Make sure the following tools are installed and accessible via the command line:

- **Python 3**: Runtime environment for the script.  
- **Git**: Required to query commit logs from your local project.  
- **Gemini CLI**: Core tool used for summarizing the commit logs.  

For installation and API key setup, refer to the [Official Google AI for Developers Guide](https://developers.google.com/).  

## ⚙️ Configuration

Edit the configuration variables at the top of the script to match your environment:

```python
AUTHOR_NAME = "hyeonsu"  # Your exact git config user.name
PROJECT_PATH = "/Users/jsy94/Desktop/healthnyou"  # Absolute path to your Git repository
OUTPUT_DIR = "/Users/jsy94/Desktop"  # Path where the summary file will be saved
````

* `AUTHOR_NAME`: Must exactly match `git config user.name`.
* `PROJECT_PATH`: Local path to your Git-managed project (directory containing `.git`).
* `OUTPUT_DIR`: Directory where the generated `.md` file will be saved.

## 🚀 How to Use

(Optional) Make the script executable:

```bash
chmod +x summarize.py
```

Run the script:

```bash
python summarize.py
```

Or if executable:

```bash
./summarize.py
```

### 💻 Example Execution

```bash
$ python summarize.py
🔍 Searching for today's logs from 'hyeonsu' in '/Users/jsy94/Desktop/healthnyou'...

--- 📜 Today's Commits ---
- feat: Add user authentication endpoint
- fix: Resolve JWT expiration error on login
- refactor: Separate auth logic using AOP
- docs: Update 'Authentication' section in API spec
----------------------------

💎 Generating summary with Gemini CLI...

✅ Summary generation complete!

# 2025-11-10 Work Summary

* Developed user authentication features and refactored existing logic
    * Implemented new API endpoints (login, register)
    * Applied AOP (Aspect-Oriented Programming) to separate common auth logic, reducing code duplication
* Resolved login error
    * Fixed a bug causing premature JWT token expiration under specific conditions
* Documentation
    * Updated the API specification to reflect the new authentication policies

📂 Saved to: /Users/jsy94/Desktop/2025-11-10_summary.md
```

## 📄 License

This project is distributed under the MIT License. Feel free to use and modify it.
