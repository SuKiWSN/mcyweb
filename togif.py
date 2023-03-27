from PIL import Image
import cv2
import glob
import os

def convert_mp4_to_jpgs(input_file):
    video_capture = cv2.VideoCapture(input_file)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"output/frame_{frame_count:03d}.jpg", image)
        still_reading, image = video_capture.read()
        frame_count += 1

def convert_image_to_gif(output_file):
    width = 520
    images = glob.glob(f"output/*.jpg")
    images.sort()

    frames = []
    for image in images:
        img = Image.open(image)
        w, h = img.size
        img = img.resize((width, int(width * h/w)))
        frames.append(img)
    frame_one = frames[0]
    frame_one.save(output_file, format="GIF", append_images=frames[1:], save_all=True, duration=30, loop=0)

    fl = os.listdir("output")
    for filename in fl:
        os.remove("output/" + filename)

def convert_mp4_to_gif(input_file, output_file):
    convert_mp4_to_jpgs(input_file)
    convert_image_to_gif(output_file)


if __name__ == '__main__':
    while True:
        if not os.path.exists("output"):
            os.mkdir("output")
        root = input("输入文件或文件夹路径\n>")
        root = root.replace(" ", "")
        if root == "exit":
            break
        if os.path.isdir(root):
            if not os.path.exists(os.path.join(root, "outputs")):
                os.mkdir(os.path.join(root, "outputs"))
            fl = os.listdir(root)
            for fname in fl:
                if fname.endswith('.mp4'):
                    fpath = os.path.join(root, fname)
                    convert_mp4_to_gif(os.path.join(root, fname), os.path.join(root, "outputs", os.path.splitext(fname)[0] + '.gif'))
                    print(os.path.splitext(fname)[0] + '.gif', "finished")
        else:
            if root.endswith('.mp4'):
                convert_mp4_to_gif(root, os.path.join(os.path.split(root)[0], os.path.splitext(root)[0]+'.gif'))
                print(os.path.splitext(os.path.split(root)[1])[0] + ".gif", "finished")
            else:
                print("No .mp4 file found")

        os.rmdir("output")
