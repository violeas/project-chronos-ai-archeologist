# Project Chronos: The AI Archeologist

## Student Name(s) and ID(s)
- Vaishnavi Arasada - ID: se25udsc077
- R.Dhanya Sphoorthi - Se25udsc063
  Haasini Kunaparaju - Se25udsc007
  Selma Jones - se25udsc060

## Project Description
Project Chronos is an AI-powered tool that reconstructs incomplete or obscure digital text fragments from historical sources. It fills in missing context using Google Gemini and automatically searches the web to provide relevant references for better understanding.

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/violeas/ProjectChronos.git
cd ProjectChronos

2. Install dependencies:
bash
pip install -r requirements.txt

3. Optional: Set up Google Gemini API key
Create a .env file in the project root.
Add your API key:
ini
GEMINI_API_KEY=your_key_here

4. Run the program to test functionality
bash
python main.py

Usage Instructions
1) Run the program:
bash
python main.py
2) Enter a fragmented text, for example:
css
smh at the top 8 drama. ppl need to chill. g2g, ttyl.
3) The program generates a Reconstruction Report with:
Original Fragment
AI-Reconstructed Text
Contextual Sources (links)
4) You can run multiple fragments one after another for testing. Example of two fragments you could use in your demo:
css
smh at the top 8 drama. ppl need 1 hill. g2g, ttyl.
brb need to eat, cya later

DEMO VIDEO:
watch the Demovideo:[https://youtu.be/N1KNu3Gi8NY]
