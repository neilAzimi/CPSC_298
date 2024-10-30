alias git-llm='if git diff --cached --quiet; then echo "No changes to commit."; else gtimeout 20 llm prompt "Generate a commit message for the recent changes" --model gpt-4 > commit_message.txt && if [ -s commit_message.txt ]; then git commit -F commit_message.txt; else echo "Error: Empty commit message. Aborting."; fi; fi'



