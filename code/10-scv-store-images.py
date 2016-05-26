import urllib.request
import os

def save_images_from_image_net():
    tea_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07933530'   
    tea_image_urls = urllib.request.urlopen(tea_images_link).read().decode()

    pic_idx = 1

    if not os.path.exists('tea'):
        os.makedirs('tea')

    for i in tea_image_urls.split('\n'):
        try:
            print(".......", i)
            urllib.request.urlretrieve(i, "tea/"+str(pic_idx)+".jpg")
            pic_idx += 1

        except Exception as e:
            print(str(e))
        
if __name__ == "__main__": 
    save_images_from_image_net()
