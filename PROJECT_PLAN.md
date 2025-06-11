# Project Plan: Simple RAG Solution with crewAI and Local LLM

Here's a project plan to implement a simple Retrieval-Augmented Generation (RAG) solution using Python and crewAI.

### **Project Goal**

To create a command-line RAG agent that can answer questions based on a collection of local PDF files. This will be achieved by ingesting the documents into a local vector database and using a local Large Language Model (LLM) for response generation.

---

### **Core Technologies**

* **Programming Language:** Python
* **Agent Framework:** crewAI
* **Document Ingestion:** LangChain, PyPDF
* **Vector Database:** ChromaDB
* **Local LLM Hosting:** Ramalama

---

### **Project Phases & Timeline**

This project is broken down into four main phases. The estimated completion time is 4-6 hours, depending on your familiarity with the tools.

#### **Phase 1: Setup and Installation (Estimated Time: 1 hour)**

1.  **Initialize Project Environment:**
    * Create a new project directory.
    * Set up a Python virtual environment:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

2.  **Install Dependencies:**
    * Create a `requirements.txt` file with the following libraries:
        ```
        crewai
        langchain
        langchain_community
        pypdf
        chromadb
        ramalama
        ```
    * Install the libraries:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Set Up Local LLM with Ramalama:**
    * Download and install Ramalama from the official website.
    * Pull a local LLM. For this project, `qwen3:1.7b` is a good starting point:
        ```bash
        ramalama pull qwen3:1.7b
        ```
    * Ensure the Ramalama server is running.

---

#### **Phase 2: Data Ingestion (Estimated Time: 1.5 hours)**

This phase focuses on creating a Python script (`ingest.py`) to process your local PDF files and store them in ChromaDB.

1.  **Directory Setup:**
    * Create a `documents` folder in your project directory and place your PDF files inside.

2.  **Develop the Ingestion Script (`ingest.py`):**
    * **Import necessary libraries:** `os`, `PyPDFLoader` from `langchain_community.document_loaders`, `RecursiveCharacterTextSplitter` from `langchain.text_splitter`, `Chroma` from `langchain_community.vectorstores`, and `OllamaEmbeddings` from `langchain_community.embeddings`.
    * **Load Documents:** Use `PyPDFLoader` to load the PDF files from the `documents` directory.
    * **Split Text:** Use `RecursiveCharacterTextSplitter` to break down the loaded documents into smaller, manageable chunks. This is crucial for effective retrieval.
    * **Generate Embeddings:** Instantiate `OllamaEmbeddings` to create vector representations of the text chunks using your local LLM.
    * **Store in Vector Database:** Use `Chroma.from_documents` to store the embedded chunks in a persistent local ChromaDB database.

---

#### **Phase 3: Agent and Task Definition (Estimated Time: 1.5 hours)**

In this phase, you'll create the main application file (`main.py`) where you define your crewAI agent and its tasks.

1.  **Import Libraries:** Import `Crew`, `Agent`, `Task`, `Process` from `crewai`, and the necessary components to interact with your local LLM and vector store.

2.  **Initialize Tools:**
    * Create a retriever tool that can query your ChromaDB vector store. This will allow the agent to fetch relevant information from your documents.

3.  **Define the Agent:**
    * Create a RAG agent using the `Agent` class.
    * **Role:** Define a role for the agent, such as "Document Analyst."
    * **Goal:** Set a clear goal, for example, "To analyze the provided documents and answer user questions based on their content."
    * **Backstory:** Provide a brief backstory to give the agent context.
    * **LLM:** Assign your local Ramalama LLM to the agent.
    * **Tools:** Equip the agent with the retriever tool you created.

4.  **Define the Task:**
    * Create a task using the `Task` class.
    * **Description:** The task description should instruct the agent to use the retriever tool to find relevant information and then formulate a comprehensive answer to a user's query.

---

#### **Phase 4: Command-line Interface and Execution (Estimated Time: 1 hour)**

This final phase involves setting up the command-line interface to interact with your RAG agent.

1.  **Create the CLI in `main.py`:**
    * Use a simple `while` loop to continuously prompt the user for input.
    * Capture the user's question from the command line.

2.  **Orchestrate the Crew:**
    * Inside the loop, create an instance of your `Crew` with the defined agent and task.
    * Pass the user's question to the task.

3.  **Execute and Display Results:**
    * Call the `kickoff()` method on your crew to start the process.
    * Print the result returned by the crew to the console.

### **Running the Project**

1.  **Ingest Documents:**
    ```bash
    python ingest.py
    ```

2.  **Run the Agent:**
    ```bash
    python main.py
    ```

You will then be prompted to ask a question in the command line. The agent will use the ingested documents to find the answer and display it.
