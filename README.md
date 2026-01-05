# Uploader (File Upload API Project)


# Description

This project is a Django REST Framework (DRF) API that allows users to **upload, retrieve, update, and delete files, images, and videos**.  
It features **full CRUD functionality** with **pagination**, **authentication**, and **permission handling** to ensure secure access.  

The project uses both **ViewSets** and **regular API views** and includes **test endpoints** to validate CRUD operations.  
It demonstrates best practices for a backend API including file validation, structured responses, and API testing.


# Features

- Upload files, images, and videos
- List and retrieve uploaded content with **pagination**
- **Search** uploaded content by name or description
- Track **time and date of creation** for each file
- Update or delete uploaded files
- **User authentication** with **Simple JWT** and **permissions** to secure endpoints
- Built with **ViewSets** and **APIViews**
- Includes **test endpoints** to verify CRUD operations
- File type and size validation
- Validators .Regulation what users can and cannot write into DRF REST API  
  

## Demo / Screenshots

# Home page 
![Description of Screenshot](screenshot_1.png)
*Initial API welcome page.  '/api/-URL*


# List  View

![Description of Screenshot](list.png)
*Paginated list view showing uploaded files across multiple pages.  'api/up/'list/-URL*


# Create

![Description of Screenshot](create.png)
![Description of Screenshot](validators.png)
![Description of Screenshot](creating_1.png)
*Creating/uploading a new file via the API with built-in validation, ready for production use. 'api/up/'- URL*



# Retrieve

![Description of Screenshot](Retrieve.png)
*Retrieving details of a single uploaded file .*'view/<int:pk>/'*-URL



# Update

![Description of Screenshot](update_1.png)
![Description of Screenshot](update.png)
*Updating an existing file’s details . 'update/<int:pk>/'-URL*



# Delete 

![Description of Screenshot](delete.png)
![Description of Screenshot](delete_after.png)
*Deleting a file from the server using the API. File is removed permanently. 'delete/<int:pk>/'URL*



# Search 

![Search page showing filtered results](search.png)
![Search page showing filtered results](search_word.png)
*Search endpoint filtering uploaded files by tite or description. 'api/search/?q=...URL*



# ViewSets

This project uses **Django REST Framework ViewSets** to manage standard CRUD operations for files, images, and videos.  
ViewSets simplify the code by automatically handling **list, create, retrieve, update, and delete** actions, while supporting **pagination, authentication, and permissions**.  
In this project, **ViewSets and APIViews work together seamlessly**, complementing each other in the Uploader app and making it **more robust and maintainable**.


# Api Root

![Search page showing filtered results](ApiRoot.png)
api/v2/-URL 



# List,Create, and Pagination 

![Search page showing filtered results](list_create.png)
![Search page showing filtered results](list_pagination_create.png)
*Listing and creating uploaded files with pagination support.api/v2/video-up/-URL*



# Retrieve,Update, or Delete

![Search page showing filtered results](retrieve_update_delete.png)
Retrieving, updating, and deleting an uploaded file via the API. .api/v2/video-up/1/-URL*




# Search 

![Search page showing filtered results](VSsearch.png)
![Search page showing filtered results](search_VS.png)
*Search works same as View but only URL chaging. api/v2/search/'-URL



# Authentication & Permissions

The Uploader API is protected using **authentication and permission classes** to restrict access to endpoints.


# Unauthorized Request and Authentication Method

![Permission Denied](permission_denied.png)
*Accessing `GET /api/up/list/` without authentication returns **HTTP 403 Forbidden**, indicating that login is required.*
- Uses **Simple JWT** for authentication
- Protected endpoints require a valid access token in the request header


# Py_Client

![Description of Screenshot](py_client.png)
*A simple Python client used to test and interact with the REST API endpoints.*

# Video
![Description of Video](video.webm)

















  
