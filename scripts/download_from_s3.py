import boto3

bucket_name = "retrieval-api-documents"
file_key = "regulation.pdf"
download_path = "data/regulation.pdf"

s3 = boto3.client("s3")

def download_pdf():
    print("Downloading file from S3...")

    s3.download_file(bucket_name, file_key, download_path)

    print("Download complete!")

if __name__ == "__main__":
    download_pdf()