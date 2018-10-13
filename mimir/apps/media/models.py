from django.db import models

class Image(models.Model):
    source      = models.ImageField(upload_to='images/source')
    file_name   = models.CharField(max_length=80)
    class_label = models.CharField(max_length=80)
    class_index = models.IntegerField()
    prediction  = models.FloatField()

class Dataset(models.Model):
    name        = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    model_file  = models.FileField(upload_to='images/source')

class NeuralNet(models.Model):
    name        = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    active      = models.BooleanField()
    dataset     = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    model_file  = models.FileField(upload_to='images/source')

class SaliencyMap(models.Model):
    source      = models.ImageField(upload_to='images/source')
    image       = models.ForeignKey(Image, on_delete=models.CASCADE)
    network     = models.ForeignKey(NeuralNet, on_delete=models.CASCADE)

    target_layer = models.IntegerField()
    target_class = models.IntegerField()

class GradCam(models.Model):
    source      = models.ImageField(upload_to='images/source')
    image       = models.ForeignKey(Image, on_delete=models.CASCADE)
    network     = models.ForeignKey(NeuralNet, on_delete=models.CASCADE)
    
    target_layer = models.IntegerField()
    target_class = models.IntegerField()

class GuidedGradCam(models.Model):
    source      = models.ImageField(upload_to='images/source')
    image       = models.ForeignKey(Image, on_delete=models.CASCADE)
    network     = models.ForeignKey(NeuralNet, on_delete=models.CASCADE)
    
    target_layer = models.IntegerField()
    target_class = models.IntegerField()