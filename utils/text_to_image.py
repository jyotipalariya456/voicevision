

from diffusers import StableDiffusionPipeline
from utils.config import MODEL_ID, DEVICE
import torch
import os

def text_to_image(prompt, output_dir="outputs/generated_images"):
    # Load the pre-trained model
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float32)
    pipe.to(DEVICE)

    # Generate image
    print(f"Generating image for prompt: {prompt}")
    image = pipe(prompt, num_inference_steps=15).images[0]

    # Save the image
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "generated_image.png")
    image.save(output_path)
    print(f"Image saved at: {output_path}")
    return output_path