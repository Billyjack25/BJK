import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content(task_type, topic):
    prompt_map = {
        "yt_script": f"Generate a 60-120 sec script on {topic} with Hook → Value → CTA",
        "blog_post": f"Write an SEO blog article targeting '{topic}' in passive income niche",
        "gumroad_copy": f"Write a product description for a digital template about {topic}",
        "affiliate_email": f"Create a high-converting email about {topic} with affiliate CTA"
    }
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_map[task_type]}]
    )
    return response['choices'][0]['message']['content']