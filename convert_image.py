from PIL import Image, ImageEnhance

imagem_colorida = Image.open('img01.jpeg')

imagen_pb = imagem_colorida.convert('L')

melhorar = ImageEnhance.Contrast(imagen_pb)

imagen_melhorada = melhorar.enhance(1.5)

imagen_melhorada.save('img02.jpeg')

imagem_colorida.close()

imagen_pb.close()
