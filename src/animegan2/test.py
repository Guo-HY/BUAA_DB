import os
import argparse

from PIL import Image
import numpy as np

import torch
from torchvision.transforms.functional import to_tensor, to_pil_image

from animegan2.model import Generator
# from model import Generator

torch.backends.cudnn.enabled = False
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True

# class Args:
#   def __init(self):
#     self.checkpoint='./weights/paprika.pt',
#     self.device='cpu',
#     self.image_name='1.jpg',
#     self.input_dir='./oripic',
#     self.output_dir='./samples/results',
#     self.upsample_align=False,
#     self.x32=False

def load_image(image_path, x32=False):
    img = Image.open(image_path).convert("RGB")

    if x32:
        def to_32s(x):
            return 256 if x < 256 else x - x % 32
        w, h = img.size
        img = img.resize((to_32s(w), to_32s(h)))

    return img


def test(output_dir, input_dir, image_name):
    device = 'cpu'
    PT = './animegan2/weights/celeba_distill.pt'
    net = Generator()
    net.load_state_dict(torch.load(PT, map_location="cpu"))
    net.to(device).eval()
    print(f"model loaded: {PT}")
    
    os.makedirs(output_dir, exist_ok=True)

    # for image_name in sorted(os.listdir(args.input_dir)):
    #     if os.path.splitext(image_name)[-1].lower() not in [".jpg", ".png", ".bmp", ".tiff"]:
    #         continue
    image = load_image(os.path.join(input_dir, image_name), False)

    with torch.no_grad():
        image = to_tensor(image).unsqueeze(0) * 2 - 1
        out = net(image.to(device), False).cpu()
        out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
        out = to_pil_image(out)

    out.save(os.path.join(output_dir, image_name))
    print(f"image saved: {image_name}")
        # for end

def animegan2(input_dir, output_dir, image_name):
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '--checkpoint',
    #     type=str,
    #     default='./weights/paprika.pt',
    # )
    # parser.add_argument(
    #     '--input_dir', 
    #     type=str, 
    #     # default='./oripic',
    #     default=input_dir,
    # )
    # parser.add_argument(
    #     '--output_dir', 
    #     type=str, 
    #     # default='./samples/results',
    #     default=output_dir,
    # )
    # parser.add_argument(
    #     '--device',
    #     type=str,
    #     default='cpu',
    # )
    # parser.add_argument(
    #     '--upsample_align',
    #     type=bool,
    #     default=False,
    #     help="Align corners in decoder upsampling layers"
    # )
    # parser.add_argument(
    #     '--x32',
    #     action="store_true",
    #     help="Resize images to multiple of 32"
    # )
    # parser.add_argument(
    #   '--image_name',
    #   type=str,
    #   # default='1.jpg',
    #   default=image_name,
    # )
    # args = parser.parse_args()
    test(output_dir, input_dir, image_name)


if __name__ == '__main__':
  animegan2('./oripic', './samples/results', '1.jpg')
