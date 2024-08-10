from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient

class AzureBlobStorageConnector:
    
    def __init__(
            self, 
            account_name=None,
            account_key=None,

            ):
        self.account_name = account_name
        self.account_key = account_key


    
    def create_connection_string(self):
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={self.account_name};AccountKey={self.account_key};EndpointSuffix=core.windows.net"
        return connection_string

    def create_blob_service_client(self, connection_string : str): 
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        return blob_service_client 

    def retrieve_blob_client(
            self, 
            blob_service_client : BlobServiceClient,
            container_name : str, 
            blob_name : str
            ):

        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        print(f"Retrieving {blob_name} from {container_name}")
        return blob_client 
    
    def retrieve_data_from_blob(
            self, 
            blob_client : BlobClient,
            file_name : str 
            ):
    
        with open(file_name, 'w+') as file:
            download_stream = blob_client.download_blob()
            blob_content = download_stream.readall()  
            contents = blob_content.decode('utf-8') 
            file.write(contents) 

        print(f'Blob Downloaded successfully. Saved as {file_name}')

if __name__ == "__main__":
    azblobconnector = AzureBlobStorageConnector()

