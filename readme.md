🤖 AI-Powered Daily Git Commit Summarizer
This script fetches all commits made by a specific author for the current day from a designated Git repository. It then uses the Gemini CLI to automatically generate a professional daily work summary in Markdown.

Instead of struggling to remember what you did all day, simply run this script before logging off to easily prepare your daily work report.

✨ Key Features
Daily Commit Aggregation: Automatically fetches all commit logs since midnight for a specific author using git log.

AI-Powered Summarization: Sends the aggregated commit messages to the gemini CLI to generate a professional summary that consolidates duplicates and highlights key tasks.

Markdown File Expor: Saves the generated summary to the specified output directory as a YYYY-MM-DD_summary.md file.

⚠️ Prerequisites
Before running this script, ensure the following tools are installed on your system and accessible via the command line (i.e., added to your system's PATH):

Python 3: The runtime environment for the script.

Git: Required to query commit logs from your local project.

Gemini CLI: The core tool used for summarizing the commit logs.

For installation and API key setup, please refer to the Official Google AI for Developers Guide.

⚙️ Configuration
Before running the script, you must edit the configuration variables at the top of the file to match your environment.

Python

# --- Configuration ---
AUTHOR_NAME = "hyeonsu"  # 👈 Your exact git config user.name
PROJECT_PATH = "/Users/jsy94/Desktop/healthnyou" # 👈 Absolute path to your Git repository
OUTPUT_DIR = "/Users/jsy94/Desktop" # 👈 Path where the summary file will be saved
# --- End Configuration ---
AUTHOR_NAME: Must exactly match the name set in your git config user.name.

PROJECT_PATH: The local path to your Git-managed project (e.g., the directory containing the .git folder).

OUTPUT_DIR: The directory where the generated .md file will be saved.

🚀 How to Use
(Optional) Make the script executable:

Bash

chmod +x summarize.py
Run the script using Python:

Bash

python summarize.py
(Or ./summarize.py if you made it executable)

💻 Example Execution
When you run the script, you will see output in your terminal similar to the example below, and a new file will be created in your OUTPUT_DIR.

Terminal Output
Bash

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
    * Implemented new API endpoints (login, register).
    * Applied AOP (Aspect-Oriented Programming) to separate common auth logic, reducing code duplication.
* Resolved login error
    * Fixed a bug causing premature JWT token expiration under
        specific conditions.
* Documentation
    * Updated the API specification to reflect the new authentication policies.

📂 Saved to: /Users/jsy94/Desktop/2025-11-10_summary.md
Generated File (2025-11-10_summary.md)
Markdown

# 2025-11-10 Work Summary

* Developed user authentication features and refactored existing logic
    * Implemented new API endpoints (login, register).
    * Applied AOP (Aspect-Oriented Programming) to separate common auth logic, reducing code duplication.
* Resolved login error
    * Fixed a bug causing premature JWT token expiration under
        specific conditions.
* Documentation
    * Updated the API specification to reflect the new authentication policies.
📄 License
This project is distributed under the MIT License. Feel free to use and modify it.