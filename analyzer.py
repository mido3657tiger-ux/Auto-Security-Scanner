import os
import openai

def analyze():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("API Key found. Ready to scan.")
    else:
        print("API Key NOT found.")

if __name__ == "__main__":
    analyze()
