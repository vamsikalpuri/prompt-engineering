# prompt-engineering
# Smart Q&A Assistant (Python)

AI-powered Smart Q&A Assistant using:
- OpenAI GPT-5
- Role Prompting
- Few-shot Learning
- Python

---

# Setup

## Create Virtual Environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python main.py


#** Sample Input**

Explain Kubernetes

# **Sample Output**
Definition:
Kubernetes is a container orchestration platform.

Key Features:
- Auto scaling
- Self healing
- Container orchestration


Architecture Flow

User Question
      ↓
Prompt Builder
      ↓
OpenAI GPT-5
      ↓
AI Response
