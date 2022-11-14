# face-analize-lambda
Using AWS Lambda, Rekognition, Python

*AWS CLI*

1. Instalar AWS CLI
2. Criar usuario no IAM com política de "AdministratorAccess"
3. aws configure

    3.1. Configure as credenciais

4. Crie os buckets e sincronize as fotos e site estático

    4.1 aws s3 mb s3://images-lambda-XX

    4.2 aws s3 sync images s3://images-lambda-XX

    4.3 aws s3 mb s3://faceanalysis-XX

    4.4 aws s3 sync XX-site s3://faceanalysis-XX

*Ambiente Python - Criar ambiente virtual*

1.    python -m venv venv
2.    .\venv\Scripts\activate
3.    pip install -r requirements.txt


*Deploy Lambda*

1. Crie a função no lambda, configure a Policy - Rekognition, S3 (FullAcess)
2. zip faceanalise.zip faceanalise.py
3. aws lambda update-function-code --function-name "FUNCTIONNAME" --zip-file fileb://faceanalise.zip

*Extras*

1. Lista de imagens indexadas:

    1.1 aws rekognition list-faces --collection-id faces



