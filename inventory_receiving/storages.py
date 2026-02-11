from django.core.files.storage import storages

def inventory_receiving_storage():
    """
    You can then use inventory_receiving_storage in a model field:
    from inventory_receiving.storages import inventory_receiving_storage
    my_field = models.FileField(storage=inventory_receiving_storage)
    Loads configuration only when accessed, not during makemigrations
    """
    return storages["inventory_receiving"] # This will use the S3Boto3Storage backend with the settings defined in settings.py under STORAGES['inventory_receiving'].

#inventory_receiving_storage = storages["inventory_receiving"] # This will use the S3Boto3Storage backend with the settings defined in settings.py under STORAGES['inventory_receiving'].
# You can then use inventory_receiving_storage in a model field:
# from inventory_receiving.storages import inventory_receiving_storage
# my_field = models.FileField(storage=inventory_receiving_storage)
