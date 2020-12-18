""" for signals handlers """
import os


def image_cleaner(sender, instance, *args, **kwargs):
    os.remove(instance.foto.file.name)