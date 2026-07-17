import os
import openai

def analyze_code(file_path):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: API Key not found"
    
    client = openai.OpenAI(api_key=api_key)
    
    with open(file_path, 'r') as f:
        code_content = f.read()
        
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Find security vulnerabilities in this code: {code_content}"}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # هذا الملف سيقوم بفحص نفسه وفحص الملفات الأخرى
    print(analyze_code("analyzer.py"))
