# Lecture 12

## Housekeeping
- Week in World of AI
    * [AI Startups](https://youtu.be/uUosHefPnWs?si=XT3MZkRurF1o8WF6)
    * [Future of AI](https://youtu.be/uqc8PWYq9Hw?si=sqg45S4BRnwsmGL4)
    * [Bolt Update](https://youtu.be/i0bQ495vMBA?si=n8ljFPeQ4vZ7HPor)
    * [Microsoft Tool Kit](https://youtu.be/Z8pCrC-NQ0U?si=EIM6_ShL-At-yBId)
    * [Tokenformer](https://youtu.be/4weeoIjWIXI?si=2l6u3g4LoTpKCAmH)
    * [LLM Use Advice](https://youtu.be/nMORNaE_qe4?si=fcJWm44bhO9uExAX)
- Reminder: Have Open AI key for remainder of semester; if CSV is not updated and do not see PRs; I review the [#continuous integration channel on Discord](https://discord.com/channels/1204850325748457543/1204856923149697045)
- Choosing alternative to n8n; Will go through in class
- Remember to `git pull upstream master && git push`
- Remember to: `uv run pip install --upgrade aider-chat`
- Office Hours today; Have not had chance to reply on Discord
- Quiz this week; 20 minutes - 20 questions
- In lieu of homework, will do break-outs today

## Where Everyone Should Be Revisited:
- Discord Notifications with Webhook (DM me if you need the hook; Look in Discord help channel for Webhooks)
- Upstream forked and Setup on Personal Github accounts; Know Git/hub:
    * `ssh-keygen` & `ssh-add {-l}`
    * `git set upstream <branch>`
    * `git pull upstream master`
    * `git merge`
    * `git push {origin}`
    * `git checkout {-b} <branch>`
    * `ssh -vT git@github.com # check ssh key setup`
    * understand `.gitignore` and `.*` hidden files in project
    * understand `git log` and how to reset out sync repos with the `upstream`
    * if on Mac: `ssh-add --apple-use-keychain  ... && ssh-add --apple-load-keychain` otherwise:
    * `ssh-add -K ~/.ssh/.ssh`
- Pull Requests on Github, forks, and origin/upstreams synchronized.
- Basics of AI coding with V0 and setting up code on local repo; Understand how to use Aider and LLM
- Knowledge of TypeScript ecosystem with `npx`, `npm`, and NodeJS (ask AI if uncertain)
- AI Tooling: V0, Replit, Chat.dev, Copilot, Cursor, & Concepts:
    * Large Language Models (LLMs)
    * Feed forward networks (& ANNs)
    * Context Windows
    * Retrieval Augmented Generation (RAG)
    * Chain & Tree of Thought (CoT/ToT)
    * Self Taught Reasoning (STaR)
    * Tokenization and Transformer Architectures as well as Next Token Prediction
    * Mixture of Experts (MoE)
    * Agentic Approaches
    * Benchmarking, Weigths/Biases (Parameters) & Open Source Relevance (open weights, data, and models)
- API Keys setup & sample `.aider.conf.yml` in proper subdirectory
- Have me (jeffrey-l-turner) as reviewer/collaborator on Pull Requests (note Canvas will be graded once assignment complete)
- Make Sure you're information is accurate on CSV posted in Discord
- Signup for [Pythathagora](https://www.pythagora.ai) - no luck getting access so far; Recommendation: use Cursor with Pythagora
- Understand basics of complexity theory and non-deterministic algos
- Up to date on CSV file. Will place whether Open AI key assigned
- Know how to use Github to create PRs, add me as reviewer and not close until graded
- Review [Cursor Directory](https://cursor.directory/)
- Aider Keys (Open AI) installed and working

## Tooling Criteria Selection (for future use)
- Open Source?
- Restricted/Unrestricted Source Code Editing
- Open Model Usage (Open AI api compatibility)
- Improvement Layer on top of LLM (e.g. "Architect")
- Overall Momentum and Direction for Tooling

## Groups to setup Agentic Framework
- Group Break-Out
    * Choose a repo lead (ideally with Docker experience)
    * Software Architecture Diagram
    * Abstraction Levels: Top-Level Architecture, Project Organization, Modules, Front-End/Back-End, Functional Decomposition
    * Development Environment
    * Data Storage: Mutability & Access (regionalized, sharding, etc.)

## Resources:
- Channels I Follow for this Class: [Wes Roth](https://www.youtube.com/@WesRoth), [Matthew Berman](https://www.youtube.com/@matthew_berman), [David Shapiro](https://www.youtube.com/@DaveShap/videos), [Indy Dev Dan](https://www.youtube.com/@indydevdan), [Greg Isenberg](https://www.youtube.com/@GregIsenberg), [3 Blue 1 Brown](https://www.youtube.com/@3blue1brown), [AI Explained](https://www.youtube.com/@3blue1brown)
- Tools: [Aider](https://aider.chat/), [LLM](https://github.com/simonw/llm), & [uv](https://github.com/astral-sh/uv) [Data Centric](https://youtube.com/@data-centric?si=SjrEhrokPgsDoeYF) [Internet of Bugs](https://youtube.com/@internetofbugs?si=hahhYKaGX59agFjH) [The AI Grid](https://youtube.com/@theaigrid?si=ZhJcF-WMTwlFZwuP) [AI Workshop](https://youtube.com/@ai-gptworkshop?si=_yLxq63PT90ZhCa5)
- [Open AI Key Management](https://platform.openai.com/)
