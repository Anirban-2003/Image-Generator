import openai
import gradio
openai.api_key = "api-key"

def Image(user_input):
  response = openai.Image.create(
    prompt=user_input,
    size="1024x1024",
    n=1,
  )
  image= response.data[0].url
  return image

demo = gradio.Interface(fn=Image, inputs = "text", outputs = "text", title = "Text to Image Generator")

demo.launch(share=True)