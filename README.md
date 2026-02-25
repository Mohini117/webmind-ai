# 📌 WebMind AI <br>
WebMind AI is a web scraping and AI-powered question-answering system built using Streamlit, LangChain, FAISS, and Groq's Llama3-8b-8192 model. It allows users to extract and analyze website content, providing intelligent answers based on retrieved information.

# Demo video :


https://github.com/user-attachments/assets/66459a44-2cdf-4c93-929b-aa0bb4533706


# 🚀 Features  <br>
✅ Web Scraping – Extracts text from any given website URL.<br>
✅ AI-Powered Answers – Uses Llama3-8b-8192 for answering questions based on website data.<br>
✅ For Embeddings - Uses deepseek R1 model(try it out!).<br>
✅ FAISS Vector Search – Enables efficient retrieval of relevant content.<br>
✅ Cool UI with Background Video – Enhances user experience with a visually appealing interface.<br>

# 🛠️ Tech Stack <br>
Python<br>
Streamlit<br>
LangChain<br>
FAISS (Facebook AI Similarity Search)<br>
Groq Llama3-8b-8192<br>
Ollama Embeddings<br>
WebBaseLoader for web scraping<br>
Requests for handling HTTP requests<br>
dotenv for environment variable management<br>

# 📦 Installation & Setup <br>
1️⃣ Clone the Repository<br>
git clone https://github.com/Mohini117/webmind-ai.git<br>
cd webmind-ai<br>


2️⃣ Create a Virtual Environment (Optional but Recommended)<br>
python -m venv venv<br>
source venv/bin/activate  # For macOS/Linux<br>
venv\Scripts\activate  # For Windows<br>

3️⃣ Install Dependencies<br>
pip install -r requirements.txt<br>

4️⃣ Set Up API Keys<br>
GROQ_API_KEY=your_api_key_here<br>

5️⃣ Run the Streamlit App<br>
streamlit run app.py<br>

# 💡 How It Works<br>
1️⃣ Enter a website URL → WebMind AI scrapes and processes its content.<br>
2️⃣ Ask a question → The AI retrieves the most relevant information from the scraped data.<br>
3️⃣ Get intelligent responses → The system provides an AI-generated answer.<br>

# 📌 Example Use Cases<br>
🔹 Extract insights from news articles<br>
🔹 Analyze blog posts for research<br>
🔹 Summarize website content<br>
🔹 Compare information across different sources<br>

# 🛠️ Future Improvements<br>
Support for multi-page scraping.<br>
Enhancing response accuracy using RAG (Retrieval-Augmented Generation).<br>
Expanding model capabilities for deeper analysis.<br>

# 🤝 Contributing<br>
🔹 Fork the repository<br>
🔹 Create a feature branch<br>
🔹 Submit a PR with a detailed description<br>
