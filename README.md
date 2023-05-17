
# NiftyBridge AI Assistant with OpenAI GPT-3.5-Turbo

This project is developed to create an intelligent AI assistant using the OpenAI GPT-3.5-Turbo model API. The AI assistant can answer questions, search for information in documents, and provide support to users.

## Installation

Before getting started with the project, you need to install some dependencies. Follow these steps:

1. Clone the repository to your local machine:

```
git clone hhttps://github.com/krabic/ai_assistant
```

2. Navigate to the project directory:

```
cd ai_assistant
```

## Configuration

Before running the project, you need to configure some parameters.

1. Add to `variables.env` file the following environment variables:

```
API_KEY=your_api_key
OPENAI_API_KEY=your_openai_api_key
```

You can obtain the required API key from the system administrator.

2. Ensure that you have Docker installed on your system. If not, install Docker from the official Docker website (https://www.docker.com/).

## Usage

The project consists of two main components: the AI assistant and the REST API interface. Below are instructions on how to run and use each of them.

### Running the AI Assistant

1. Run the Docker container using the Dockerfile:

```
docker-compose build
docker-compose up
```

2. Now u can send POST request to  
http://0.0.0.0:8080/api/send
    with parameter question and api_key in headers
