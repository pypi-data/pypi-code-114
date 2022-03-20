from google.cloud import storage
import logging

class Google_Storage_Utility(object):
  """
  !!!Welcome to Google_Storage_Utility Doc String!!!
  Google_Storage_Utility class consists of storage utility methods.

  gcp_create_bucket(project_id, bucket_nm): create new bucket named bucket_nm, under the google project, specified as project_id
  gcp_list_buckets(project_id):
  gcp_blob_list(project_id, bucket_nm, prefix):
  """

  def __init__(self, project_id):
    self.project_id = project_id
    self.storage_client = storage.Client(project=project_id)

  def gcp_create_bucket(self, bucket_nm):
    new_bucket = self.storage_client.create_bucket(bucket_nm)
    return new_bucket.name

  def gcp_list_buckets(self):
    bucket_list = []
    buckets = self.storage_client.list_buckets()
    for bucket in buckets:
      bucket_list.append(bucket.name)
    return bucket_list

  def gcp_blob_list(self, bucket_nm, prefix):
    bucket = self.storage_client.get_bucket(bucket_nm)
    iterator = bucket.list_blobs(delimiter='/', prefix=prefix)
    response = iterator._get_next_page_response() 
    print(iterator)
    print(response)
    '''
    list(iterator) # Need for iteration
    for prefix in iterator.prefixes:
      out = f"gs://{bucket_nm}/{prefix}"
    '''
    prefix_list = {}
    level = 0
    list1 = []
    for prefix in response.get('prefixes', ""):
      list1.append(f"gs://{bucket_nm}/{prefix}")
    prefix_list[level] = list1
    return prefix_list

  def list_gcs_directories(self, bucket, prefix):
    # from https://github.com/GoogleCloudPlatform/google-cloud-python/issues/920
    iterator = self.storage_client.list_blobs(bucket, prefix=prefix, delimiter='/')
    prefixes = {}
    for page in iterator.pages:
        print(page)
        for prefix in page.prefixes: 
          print(prefix)
          print(dir(page))   
    return prefixes

  def gcp_blob_all_list(self, bucket_nm):
    bucket = storage.Bucket(self.storage_client, bucket_nm, user_project=self.project_id)
    all_blobs = list(self.storage_client.list_blobs(bucket))
    prefix_dict = {}
    blob_list = []
    #print(all_blobs)
    for blob in all_blobs:
      #print(blob.name.count("/"), blob.name)
      if not prefix_dict.get(blob.name.count("/")):
        prefix_dict[blob.name.count("/")] = []
      if blob.name[-1] == "/":
        prefix_dict[blob.name.count("/")].append(blob.name)
      else:
        blob_list.append(blob.name)       
    return prefix_dict, blob_list

  def create_blob(self, bucket_nm, blob_nm, filepath):
    new_bucket = self.storage_client.get_bucket(bucket_nm)
    new_blob = new_bucket.blob(blob_nm) # 'remote/path/storage.txt'
    #blob.upload_from_string('New contents!')
    out = new_blob.upload_from_filename(filename=filepath) # '/local/path.txt'
    return out

  def retrieve_blob(self, bucket_nm, blob_nm):
    bucket = client.get_bucket('bucket-id')
    blob = bucket.get_blob('remote/path/to/file.txt')
    return blob.download_as_bytes()

  def test(self):
    return self.project_id