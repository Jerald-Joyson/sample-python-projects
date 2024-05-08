from PIL import Image, ImageFilter

def resize_image(image, width, height):
    return image.resize((width, height))

def rotate_image(image, angle):
    return image.rotate(angle)

def grayscale_image(image):
    return image.convert('L')

def apply_filter(image, filter_name):
    if filter_name == 'BLUR':
        return image.filter(ImageFilter.BLUR)
    elif filter_name == 'CONTOUR':
        return image.filter(ImageFilter.CONTOUR)
    else:
        return image

def crop_image(image, bbox):
    return image.crop(bbox)

def main():
    # Load image from file
    input_image_path = 'image.jpg'
    output_image_path = 'output_image_{}.jpg'

    with Image.open(input_image_path) as img:
        # Resize
        resized_img = resize_image(img, 300, 300)
        resized_img.save(output_image_path.format('resized'))

        # Rotate
        rotated_img = rotate_image(img, 90)
        rotated_img.save(output_image_path.format('rotated'))

        # Grayscale
        grayscale_img = grayscale_image(img)
        grayscale_img.save(output_image_path.format('grayscale'))

        # Filter
        filtered_img = apply_filter(img, 'BLUR')
        filtered_img.save(output_image_path.format('blurred'))

        # Crop
        cropped_img = crop_image(img, (100, 100, 400, 400))  # x, y, width, height
        cropped_img.save(output_image_path.format('cropped'))

if __name__ == "__main__":
    main()
