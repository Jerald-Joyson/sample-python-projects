from PIL import Image, ImageFilter

def resize_image(image_path, width, height, output_path):

    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    resized_image.save(output_path)

def rotate_image(image_path, angle, output_path):

    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    rotated_image.save(output_path)

def grayscale_image(image_path, output_path):

    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)

def filter_image(image_path, filter_type, output_path):

    image = Image.open(image_path)
    filtered_image = image.filter(filter_type)
    filtered_image.save(output_path)

def crop_image(image_path, bbox, output_path):

    image = Image.open(image_path)
    cropped_image = image.crop(bbox)
    cropped_image.save(output_path)

def main():
    image_path = "image.jpg"

    # Resize
    resize_image(image_path, 300, 200, "resized_image.jpg")

    # Rotate
    rotate_image(image_path, 90, "rotated_image.jpg")

    # Grayscale
    grayscale_image(image_path, "grayscale_image.jpg")

    # Filter
    filter_image(image_path, ImageFilter.BLUR, "blurred_image.jpg")

    # Crop
    crop_bbox = (100, 100, 400, 300)
    crop_image(image_path, crop_bbox, "cropped_image.jpg")

if __name__ == "__main__":
    main()
