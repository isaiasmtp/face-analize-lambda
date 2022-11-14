import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')
bucket_images = 'XXXX'
bucket_site = 'XXXX'

def detectd_faces():
    detected_faces = client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='temp',
        Image={
            'S3Object': {
                'Bucket': bucket_images,
                'Name': '_analyse.jpg',
            },
        },
    )
    return detected_faces

def create_list_faceId_detected(detected_faces):
    facesId_detected = []
    for images in range(len(detected_faces['FaceRecords'])):
        facesId_detected.append(detected_faces['FaceRecords'][images]['Face']['FaceId'])
    return facesId_detected

def compare_images(facesId_detected):
    result = []
    for i in facesId_detected:
        result.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=i,
                FaceMatchThreshold=80,
                MaxFaces=10,
            )
        )
    return result

def get_json(faceMatches):
    data = []
    for face in faceMatches:
        if(len(face.get('FaceMatches'))) >= 1:
            profile = dict(
                        nome = face['FaceMatches'][0]['Face']['ExternalImageId'],
                        faceMatches = round(face['FaceMatches'][0]['Similarity'], 2)
                    )
            data.append(profile)
    return data

def delete_image_from_collection(facesId_detected):
    client.delete_faces(
        CollectionId='faces',
        FaceIds=facesId_detected
    )

def public_data(data):
    file = s3.Object(bucket_site, 'data.json')
    file.put(Body=json.dumps(data))

def main(event, context):
    faces = detectd_faces()
    facesId_detected = create_list_faceId_detected(faces)
    faceMatches = compare_images(facesId_detected)
    data = get_json(faceMatches)
    public_data(data)
    delete_image_from_collection(facesId_detected)