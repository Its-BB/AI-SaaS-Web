# IntelliChat

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-yellow)

> A modern, AI-powered conversation platform with a sleek web interface for interacting with local language models.

## 📋 Overview

IntelliChat provides a seamless experience for engaging with AI language models right in your browser. Powered by local GGUF models and built with a Flask backend, it offers a responsive and feature-rich chat interface similar to popular AI assistants but running entirely on your own hardware.

## ✨ Features

- **💬 Real-Time Chat** - Engage in fluid conversations with AI powered by local GGUF models
- **🗂️ Conversation Management** - Create, edit, and delete conversations with persistent storage
- **📎 File Attachments** - Upload images, PDFs, and text files (up to 5MB) to enhance interactions
- **🌓 Theme Support** - Toggle between light and dark themes for comfortable viewing
- **🤖 Model Selection** - Choose from available AI models (currently supports phi-2.Q5_0.gguf)
- **📱 Responsive Design** - Optimized for both desktop and mobile devices with collapsible sidebar
- **🚀 Onboarding Guide** - Welcoming modal for first-time users with helpful tips
- **🛠️ Tools Panel** - Access conversation tools like summarize and analyze (placeholder functionality)
- **🎨 Syntax Highlighting** - Code snippets formatted beautifully with Highlight.js
- **⚡ Streaming Responses** - AI responses stream in real-time for a dynamic experience

## 🛠️ Tech Stack

| Component | Technologies |
|-----------|-------------|
| **Backend** | Flask (Python), llama_cpp |
| **Frontend** | HTML, CSS, JavaScript, marked, Highlight.js |
| **Styling** | Custom CSS with variables for theming |
| **Fonts** | Inter (Google Fonts) |

## 📋 Prerequisites

- Python 3.8 or higher
- A compatible GGUF model file (e.g., phi-2.Q5_0.gguf)
- Node.js (optional, for development purposes)
- Modern web browser (Chrome, Firefox, Edge, etc.)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Its-BB/AI-SaaS-Web.git
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask flask-cors llama_cpp
```

### 4. Download the Model

- Download the phi-2.Q5_0.gguf model file (or another compatible GGUF model)
- Place it in the `models/` directory in the project root

### 5. Run the Server

```bash
python server.py
```

The server will start at http://localhost:5000.

### 6. Access the Application

Open your browser and navigate to http://localhost:5000

## 💻 Usage

### Starting a Chat

- Click the "New Chat" button in the sidebar to create a new conversation
- Type a message in the input box and press "Send" or hit Enter
- Use suggestion cards on the welcome screen for predefined prompts

### Managing Conversations

- View all conversations in the sidebar under "Conversations"
- Click a conversation to load its messages
- Edit or delete conversations using the action buttons

### Attaching Files

- Click the paperclip icon to open the file upload area
- Drag and drop or select files (images, PDFs, text; max 5MB)
- Remove attached files using the "×" button in the preview

### Customizing Your Experience

- **Theme**: Click the theme toggle in the sidebar footer to switch between light/dark modes
- **Tools**: Access the tools panel via the button in the chat header
- **Settings**: Configure application settings through the sidebar footer menu

## 📁 Project Structure

```
intellichat/
├── models/
│   └── phi-2.Q5_0.gguf         # GGUF model file (not included)
├── static/
│   ├── index.html              # Main frontend HTML
│   └── style.css               # CSS styles
├── server.py                   # Flask backend
├── README.md                   # Project documentation
└── venv/                       # Virtual environment
```

## 🛠️ Development

### Backend

- Modify `server.py` to adjust model parameters or add new endpoints
- Update the `model_path` if using a different GGUF model

### Frontend

- Edit `static/index.html` for UI changes
- Update `static/style.css` for styling adjustments
- Extend JavaScript for new features

### Adding Models

- Place additional GGUF models in the `models/` directory
- Update the modelSelector section in `index.html`
- Modify `server.py` to handle model selection

## ⚠️ Troubleshooting

### Server Issues

- Ensure `server.py` is running and the model file exists in `models/`
- Check the console for errors (missing dependencies, invalid model)
- Verify server accessibility at http://localhost:5000

### Model Loading Problems

- Confirm the GGUF model is valid and compatible with llama_cpp
- Check system resources (CPU/memory) as models can be resource-intensive

### Frontend Problems

- Ensure static files are in the correct location
- Clear browser cache if changes don't appear
- Check browser console for JavaScript errors

## ⚡ Performance Tips

- Use quantized models (Q4_0, Q5_0) for better performance on consumer hardware
- Adjust context size (`n_ctx`) based on your system's RAM
- Lower temperature values (0.1-0.7) provide more focused responses
- Close unused conversations to conserve browser memory

## 🚧 Limitations & Known Issues

- Single model support (currently hardcoded to phi-2.Q5_0.gguf)
- Local storage limitations for conversation history
- Placeholder tools requiring backend implementation
- No user authentication or session management
- Limited file processing capabilities

## 🔮 Roadmap

- [ ] Dynamic model switching in the backend
- [ ] Server-side conversation storage
- [ ] Full implementation of summarize and analyze tools
- [ ] File content processing (PDF text extraction, image analysis)
- [ ] User authentication and profiles
- [ ] Enhanced mobile experience with touch gestures
- [ ] Voice input support via Web Speech API
- [ ] Multi-user support with conversation sharing

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) and [llama_cpp](https://github.com/abetlen/llama-cpp-python)
- Styled with [Inter](https://fonts.google.com/specimen/Inter) font and [Highlight.js](https://highlightjs.org/)
- Inspired by modern chat interfaces like ChatGPT

---

<p align="center">
  Made with ❤️ by CoderBiBi
</p>