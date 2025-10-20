# ai-agent-commerce-web

## 📝 Introduction

This repository aims to develop a chatbot easy demo tailored for the commerce website.

## 🌟 Features
- General conversation with agent
    - For example: "What's your name?", "What can you do?"
- Text-Based Product Recommendation
    - For example: "Recommend me a t-shirt for sports."
- Image-Based Product Search
    - Product recommendation and search are limited to items in a predefined catalog.

## ⚙️ Tech Stacks
* Frontend: [Next.js](https://nextjs.org/)
* Backend: [FastAPI](https://fastapi.tiangolo.com/)
* Databases: None. (For simplicity, Product data is stored in a python file only)
* Log Monitor: [Dozzle](https://dozzle.dev/)

## 🚧 Current stage

The project has completed the basic demo fullfuilling three features, but requires more tests...

## 🛠️ Local build

This project uses [Docker Compose](https://docs.docker.com/compose/) for local development.  
The configuration file is located at [docker/docker-compose.yml](docker/docker-compose.yml), and a high-level explanation of each container service is available in the [Docker README](docker/README.md).

### 🔐 Environment Setup

Obtain the required environment variable files from the author and place it at:

- `mcp/.env`
- `frontend/.env.local`

### ⚙️ Prerequisites

Ensure your system has the following installed:

- [Docker](https://docs.docker.com/engine/install/)
- [Node.js and npm](https://nodejs.org/en/download)

### 🚀 Start All Services

Navigate to the `/docker` directory and run:

```bash
docker compose up --build
```

(Optional) To verify that all Docker containers are running properly:
```bash
docker ps -a
```

### 💻 Start the Frontend
Install the frontend dependencies:

```bash
cd frontend
npm i
```

Then run the development server:

```bash
npm run dev
```

Once started, the chatbot will be available at http://localhost:3000.
