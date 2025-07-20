from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)
    encrypted_data = data ^ key
    encrypted_img = Image.fromarray(encrypted_data.astype('uint8'), 'RGB')
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, output_path, key):
    img = Image.open(encrypted_path).convert('RGB')
    data = np.array(img)
    decrypted_data = data ^ key
    decrypted_img = Image.fromarray(decrypted_data.astype('uint8'), 'RGB')
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    key = 123  # Simple numeric key
    encrypt_image("original_image.jpg", "encrypted_image.png", key)
    decrypt_image("encrypted_image.png", "decrypted_image.jpg", key)
