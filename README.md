# BDZMS – Python Microservice 

**BDZMS** is a Python microservice that wraps the **BDZ.bg API**, providing endpoints to fetch data related to the Bulgarian state railway company BDZ. This microservice uses **FastAPI** and 
utilizes the **ms_core** library, which is a toolkit I wrote for building HTTP microservices with FastAPI, Pydantic, and TortoiseORM. 

This service is part of the transport tracking platform, integrating with the **BurgasBusMS** for a complete transport tracking solution. 

## Features 
- Wraps BDZ.bg API to provide railway data such as train schedules, routes, and station information. 
- Built with **FastAPI** for fast, asynchronous handling of HTTP requests. 
- Integrated with **ms_core** for simplified microservice development. 
- Uses **TortoiseORM** with **asyncpg** for efficient database handling. 

## 🛠 Stack 
**FastAPI, Pydantic, TortoiseORM, ms_core, asyncpg, uvicorn, aiohttp** 

## 🚀 Startup Guide

1. **Install dependencies:** 
   ```bash 
   pip install -r requirements.txt 
   ```

2. **Start the microservice:** 
   ```bash 
   uvicorn main:app --reload 
   ``` 

3. **Build for production:** 
   ```bash 
   uvicorn main:app --host 0.0.0.0 --port 8000 
   ``` 

The microservice will be accessible at `http://localhost:8000` by default. 

## 📡 API Communication 
The microservice handles API requests through FastAPI endpoints, processes them, and communicates with external services using **aiohttp**. It uses **ms_core** for simplified interactions with databases and external APIs. 

## 🧪 Testing 
- The microservice includes unit tests to ensure data processing and API communication work correctly. You can run tests using `pytest`. 
