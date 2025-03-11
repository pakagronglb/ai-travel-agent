# Travel AI Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)
![Google Maps](https://img.shields.io/badge/Google%20Maps-API-red.svg)
![Exa](https://img.shields.io/badge/Exa-Search%20API-purple.svg)
![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-Search-orange.svg)

## 📝 Description

This Travel AI Agent is an intelligent assistant that helps users plan detailed travel itineraries. The agent leverages multiple AI models and external APIs to provide comprehensive travel recommendations including accommodations, activities, restaurants, and transportation options based on user preferences.

## ✨ Features

- **Personalized Itinerary Planning**: Generate custom travel plans based on destination, duration, budget, and preferences
- **Google Maps Integration**: Automatically include Google Maps URLs for all recommended locations
- **Web Search Capabilities**: Gather up-to-date information about attractions, opening hours, and admission fees
- **Budget-Conscious Recommendations**: Tailor suggestions to fit within the user's specified budget
- **Multi-Agent Architecture**: Utilizes specialized agents for different tasks (planning, mapping, information gathering)

## 🛠️ Technologies Used

- **Python**: Core programming language
- **OpenAI API**: Powers the intelligent conversation and planning capabilities
- **Google Maps API**: Provides location data and mapping functionality
- **Exa Search API**: Enables web search capabilities for up-to-date information
- **DuckDuckGo Search**: Alternative search engine for gathering information
- **Agno Framework**: Orchestrates the multi-agent system

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- API keys for:
  - OpenAI
  - Google Maps
  - Exa Search

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pakagronglb/ai-travel-agent.git
   cd ai-travel-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   MAPS_API_KEY=your_google_maps_api_key
   EXA_API_KEY=your_exa_api_key
   ```

### Usage

Run the travel agent:
```bash
python travel_agent.py
```

Example prompts:
- "I am planning a trip to Thailand for 7 days with a budget of $1500."
- "I want to visit Japan for 10 days in April with my family. Our budget is $5000."
- "Plan a romantic weekend getaway to Paris with a luxury budget."

## 📋 Project Structure

```
travel-ai-agent/
├── travel_agent.py     # Main application file
├── maps_tools.py       # Google Maps API integration
├── prompts.py          # System prompts and instructions
├── .env                # Environment variables (API keys)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

## 🔒 Security Notes

- Never commit your `.env` file or expose your API keys
- The included `.gitignore` file helps prevent accidental exposure of sensitive information

## 🙏 Credits

This project was created following the tutorial by [Jie Jenn](https://www.youtube.com/watch?v=FLYcpeYLJFI) on YouTube. The tutorial provides excellent guidance on building AI agents with multiple API integrations.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📬 Contact

If you have any questions or feedback, please open an issue in the repository. 