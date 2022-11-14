import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
client = boto3.client('rekognition')
bucket_images = 'XXXX'

# Create a collection
def create_collection(collection_id):
    print('Creating collection:' + collection_id)
    response=client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')

# Delete collection
def delete_collection(collection_id):
    print('Attempting to delete collection ' + collection_id)
    client=boto3.client('rekognition')
    status_code=0
    try:
        response=client.delete_collection(CollectionId=collection_id)
        status_code=response['StatusCode']
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collection_id + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
        status_code=e.response['ResponseMetadata']['HTTPStatusCode']
    return(status_code)

# Listar imagens no bucket.
def list_images():
    images = []
    bucket = s3.Bucket(bucket_images)
    for image in bucket.objects.all():
        images.append(image.key)    
    return images

# Indexar Imagens na Collection de Rekognition
def index_collection(images):
    for i in images:
        response = client.index_faces(
            CollectionId='faces',
            DetectionAttributes=[],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': bucket_images,
                    'Name': i,
                },
            },
        )


def main():
    collectionId = 'faces'
    delete_collection(collectionId)
    create_collection(collectionId)
    images = list_images()
    index_collection(images)



if __name__ == "__main__":
    main()   