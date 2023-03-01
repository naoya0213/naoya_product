import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
def waifu_diffusion(prompt):
  pipe = StableDiffusionPipeline.from_pretrained(
    'hakurei/waifu-diffusion',
    torch_dtype=torch.float16
  ).to('cuda')
  with autocast("cuda"):
    image = pipe(prompt, guidance_scale=6).images[0]
  return image
# image.save("test.png")
# prompt = "1girl, aqua eyes, baseball cap, blonde hair, closed mouth, earrings, green background, hat, hoop earrings, jewelry, looking at viewer, shirt, short hair, simple background, solo, upper body, yellow shirt"
 