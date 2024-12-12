
from diffusers import StableDiffusionPipeline
from utils.config import MODEL_ID, DEVICE
import os

def text_to_image(prompt, output_dir="outputs/generated_images"):
   
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID)
    pipe.to(DEVICE)


    print(f"Generating image for prompt: {prompt}")
    image = pipe(prompt).images[0]

   
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "generated_image.png")
    image.save(output_path)
    print(f"Image saved at: {output_path}")
    return output_path
