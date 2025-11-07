# Generative AI Tutor Prototype (Completed – 2024)

## Overview
This repository documents a **completed research prototype** developed in early 2024 to explore how **Generative AI** can provide instructional support to **novice Python programmers**.  
The system was implemented as a lightweight Flask-based web application that delivers **context-aware code explanations** and **debugging hints** using GPT-style language models.  

The project extends ideas from the *AI-Driven Project-Learning Prototype* and investigates how generative models can act as **explainable, ethical learning companions** rather than answer-generating tools.  
It was later published here for reference and open-access sharing.

---

## Research Motivation
Recent developments in large language models (LLMs) have enabled code generation and feedback at unprecedented levels of fluency.  
However, educational use demands **transparent, formative feedback** instead of direct problem-solving.  
This prototype examined how generative-AI feedback could:  
1. Improve learners’ comprehension of small Python programs.  
2. Encourage self-explanation and debugging strategies.  
3. Demonstrate responsible-AI principles in learning environments.

---

## System Summary
The tutor accepts short Python code snippets and allows two interaction modes:

| Mode | Function |
|------|-----------|
| **Explain my code** | Produces a beginner-level narrative explaining program behavior. |
| **Debug hint** | Suggests likely errors and step-by-step reasoning paths. |

The app can operate in two modes:
- **Mock Mode** – runs without an API key, generating offline example responses.  
- **Live Mode** – connects to OpenAI GPT API for authentic generative feedback.

---
Copyright © 2025 Ragunath Nagaraj. All Rights Reserved.
