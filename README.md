# AI Handwriting Generator 🎨

Transform your typed text into beautiful handwritten notes using AI! This Django application integrates with Hugging Face's AI models to generate realistic handwriting in various styles.

![Demo Preview](demo.gif)

## ✨ Features

- 🖋️ Real-time handwriting generation
- 📝 Multiple writing styles and paper types
- 🎨 Different ink color options
- 🚀 Instant preview and download
- 📱 Responsive design
- ⚡ Fast and seamless UI with HTMX

## 🔧 Tech Stack

- Django (with UV package manager)
- HTMX for dynamic interactions
- Hugging Face Hub for AI integration
- Tailwind CSS for styling
- Python 3.11+

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- [UV](https://github.com/astral-sh/uv) package manager
- [Hugging Face API key](https://huggingface.co/settings/tokens)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-handwriting-generator.git
cd ai-handwriting-generator
```

2. Create a virtual environment and install dependencies using UV:

```bash
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
HUGGINGFACE_TOKEN=your_huggingface_api_token
SECRET_KEY=django-insecure-cygdht8j2xr64l00@0du183d30@erec1ql@1i-z($-r=b+)3c8
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Visit `http://localhost:8000` in your browser!

## 📸 Screenshots

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ How it Works

The application uses the [Flux Handwriting model](https://huggingface.co/fofr/flux-handwriting) from Hugging Face to generate handwritten text. When you submit text through the web interface:

1. The text is sent to our Django backend
2. The backend makes a request to Hugging Face's Inference API
3. The generated handwriting image is returned and displayed
4. You can download the generated image or generate new ones

## 📝 Environment Variables

The following environment variables are required:

| Variable            | Description                 |
| ------------------- | --------------------------- |
| `HUGGINGFACE_TOKEN` | Your Hugging Face API token |
| `SECRET_KEY`        | Django secret key           |

## 🔑 Getting a Hugging Face API Token

1. Create an account at [Hugging Face](https://huggingface.co/)
2. Go to your [Profile Settings](https://huggingface.co/settings/tokens)
3. Create a new API token
4. Copy the token to your `.env` file

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the AI models
- [HTMX](https://htmx.org/) for making the UI smooth
- The Django community for the amazing framework

## ⚠️ Note

The demo video is sped up to showcase the functionality quickly. Actual generation times may vary based on the Hugging Face API's response time and your internet connection.

---

Made with ❤️ by [Remith R Nair]
