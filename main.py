from artdirector import ArtDirector

ad = ArtDirector()
ad.load("input.jpg")
ad.crop([400, 400], focus=[600, 600], zoom=0.3)
ad.save("output.jpg")
print(ad.image)
