from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=80)

class Category(models.Model):
    name = models.CharField(max_length=80)

class DatasetCategory(models.Model):
    index    = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dataset  = models.ForeignKey(Dataset, related_name='dataset_categories', on_delete=models.CASCADE)


class NeuralNetwork(models.Model):
    name       = models.CharField(max_length=80)
    active     = models.BooleanField(default=False)
    dataset    = models.ForeignKey(Dataset, on_delete=models.CASCADE, blank=True, null=True)
    model_file = models.FileField(upload_to='neuralnets/')

class NeuralNetworkLayer(models.Model):
    name    = models.CharField(max_length=80)
    index   = models.IntegerField()
    network = models.ForeignKey(NeuralNetwork, related_name='neural_network_layers', on_delete=models.CASCADE)





class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    imagefile = models.ImageField(upload_to='media/')

class ImageCategoryPrediction(models.Model):
    image      = models.ForeignKey(Image, on_delete=models.CASCADE)
    network    = models.ForeignKey(NeuralNetwork, on_delete=models.CASCADE)
    index      = models.IntegerField()
    confidence = models.DecimalField(max_digits=3, decimal_places=3)

class SaliencyMap(models.Model):
    source  = models.ImageField(upload_to='images/source')
    image   = models.ForeignKey(Image, on_delete=models.CASCADE)
    network = models.ForeignKey(NeuralNetwork, on_delete=models.CASCADE)

    target_layer = models.IntegerField()

class GradCam(models.Model):
    source  = models.ImageField(upload_to='images/source')
    image   = models.ForeignKey(Image, on_delete=models.CASCADE)
    network = models.ForeignKey(NeuralNetwork, on_delete=models.CASCADE)
    
    target_layer = models.IntegerField()
    target_class = models.IntegerField()

class GuidedGradCam(models.Model):
    source  = models.ImageField(upload_to='images/source')
    image   = models.ForeignKey(Image, on_delete=models.CASCADE)
    network = models.ForeignKey(NeuralNetwork, on_delete=models.CASCADE)
    
    target_layer = models.IntegerField()
    target_class = models.IntegerField()