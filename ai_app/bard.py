
# using ai models built by third party
def ai_respo(prompt, instruction):
    from transformers import pipeline
    generator = pipeline('text-generation', model='gpt2')
    content=prompt + instruction
    prompt = content
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result

#my own custom fast response model, no hard system requirements as the above
import random

def read_txt(file_path):
    content = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
    except Exception as e:
        print(f"Error: The file '{file_path}' could not be read. {e}")
    
    return content

def filter_content(content, keywords):
    filtered_content = []
    for line in content:
        if any(keyword.lower() in line.lower() for keyword in keywords):
            filtered_content.append(line)
    return filtered_content

def generate_response(filtered_content):
    if not filtered_content:
        return "I couldn't find anything related to your query."
    return random.choice(filtered_content)

def ai_response(file_path, query):
    # Read the content from the file
    content = read_txt(file_path)
    
    # Split the query into keywords
    keywords = query.split()
    
    # Filter the content based on keywords
    filtered_content = filter_content(content, keywords)
    
    # Generate a response
    response = generate_response(filtered_content)
    
    return response

'''
# Example usage:
file_path = '/home/user/aicats/ai_cat/propela.txt'  # Replace with the path to your text file
query = "objectives"  # Replace with your query
response = ai_response(file_path, query)
print(response)
'''