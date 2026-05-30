# ⚡ System Control Interface v1.0.0

A high-performance, minimalist terminal automation assistant. This application seamlessly unifies native operating system controls—such as direct web routing, persistent quick-access hotkeys, and live global news feeds—with an advanced, real-time streaming AI conversation engine powered by OpenRouter.

---

## 🚀 Key Features

*   **Automated Web Routing:** Instantly launches specific domains, parses strict URLs, or seamlessly falls back to optimized Google searches.
*   **Persistent Quick Access:** Save and manage single-key custom shortcuts (e.g., `y` for YouTube) that automatically persist across sessions via a local JSON storage engine.
*   **Live News Integration:** Query and stream real-time global news headlines directly inside your terminal session using the NewsAPI framework.
*   **Streaming AI Fallback:** For general inquiries or complex chatter, the terminal ecosystem hands over control to a streaming AI engine utilizing OpenRouter (`openai/gpt-oss-120b:free`).

---

## 🛠️ Getting Started

Follow these streamlined deployment steps to set up the control interface on your local environment:

### Step 1: Install Dependencies
Execute the following command in your terminal or command prompt to install all necessary external package requirements:
```bash
pip install -r requirements.txt

### Step 2: Configure Environment Variables
Copy `.env.example` to a new file named `.env` and add your keys:

OPENROUTER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
