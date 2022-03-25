from googleapiclient.discovery import Resource, build
from apiclient.http import MediaFileUpload
from fp_th_di.logger import logger
from google.oauth2 import service_account

def get_google_drive_credential(
    serviceAccountSecretCredentialsLocation:str,
    scopes:list
  ):
  """Get google drive credential or create new one if not found
  """  
  credentials = service_account.Credentials.from_service_account_file(
        serviceAccountSecretCredentialsLocation, scopes=scopes)
  return credentials

def create_google_drive_service(
    serviceName:str,
    serviceAccountSecretCredentialsLocation:str,
    apiVersion:str,
    scopes:list
  ):
  return build(
    serviceName, 
    apiVersion, 
    credentials=get_google_drive_credential(
      serviceAccountSecretCredentialsLocation=serviceAccountSecretCredentialsLocation,
      scopes=scopes
    )
  )

def generate_google_drive_folder_metadata(folderName:str, parentFolderId:str) -> dict:
  """Generates metadata dict for folder type

  Args:
    folderName (str): folder name to create
    parentFolderId (str): google id of parent folder to create new folder in

  Returns:
    dict: the folder metadata
  """    
  return {
    'name': folderName,
    'mimeType': 'application/vnd.google-apps.folder',
    'parents': [parentFolderId]
  }

def create_new_google_drive_folder(driveService:Resource, folderName:str, parentFolderId:str) -> str:
  """Creates new google drive folder

  Args:
    driveService (Resource): google drive service
    folderName (str): folder name
    parentFolderId (str): google id of parent folder to create new folder in

  Returns:
    str: new folder id
  """    
  folder = driveService.files().create(fields='id',
    body=generate_google_drive_folder_metadata(
      folderName=folderName,
      parentFolderId=parentFolderId
    )).execute()
  logger.info('Successfully created new Google Drive folder:', folder.get('id'))
  return folder.get('id')

def search_for_google_drive_folder(driveService:Resource, folderName:str) -> str:
  """Search for targeted folder by name

  Args:
    driveService (Resource): google drive service
    folderName (str): name of folder to search for

  Returns:
    str: [description]
  """    
  logger.info('Searching for Google Drive Folder:', folderName)
  pageToken = None
  while True:
    response = driveService.files().list(
      q="mimeType = 'application/vnd.google-apps.folder'",
      spaces='drive',
      fields='nextPageToken, files(id, name)',
      pageToken=pageToken
      ).execute()
    for file in response.get('files', []):
      if file.get('name') == folderName:
        logger.info('Found folder: %s (%s)' % (file.get('name'), file.get('id')))
        return file.get('id')
    pageToken = response.get('nextPageToken', None)
    if pageToken is None:
      break
  logger.info('Could not found targeted folder in your Drive')


def generate_file_metadata(filename:str, parentFolderId:str, mimeType:str) -> dict:
  """Generates metadata dict for file type

  Args:
    filename (str): file to create
    parentFolderId (str): google id of parent folder to create the file in
    mimeType (str): file mime type. For example: 
        image/png or image/jpeg for images
        application/vnd.openxmlformats-officedocument.spreadsheetml.sheet for xlsx file
        application/vnd.ms-excel for xls file
        text/csv for csv file

  Returns:
    dict: the folder metadata
  """    
  return {
    'name': filename,
    'mimeType': mimeType,
    'parents': [parentFolderId]
  }

def upload_file_to_google(driveService:Resource, localFileLocation:str, filename:str, parentFolderId:str, mimeType:str) -> str:
  """Upload a file from local to google drive folder

  Args:
    driveService (Resource): google drive service
    localFileLocation (str): path to file location
    filename (str): filename
    parentFolderId (str):  google id of parent folder to create the file in
    mimeType (str): file mime type. For example: 
      image/png or image/jpeg for images
      application/vnd.openxmlformats-officedocument.spreadsheetml.sheet for xlsx file
      application/vnd.ms-excel for xls file
      text/csv for csv file

  Returns:
    str: google id of the file uploaded to Google Drive
  """  
  media = MediaFileUpload(f'{localFileLocation}/{filename}', mimetype=mimeType)

  # Upload the file, use supportsAllDrives=True to enable uploading if targeted parent folder is shared drives.
  file = driveService.files().create(
    body=generate_file_metadata(
      filename=filename,
      parentFolderId=parentFolderId,
      mimeType=mimeType
    ), 
    media_body=media, 
    supportsAllDrives=True
  ).execute()
  logger.info("Successfully created file '%s' id '%s'." % (file.get('name'), file.get('id')))
  return file.get('id')

