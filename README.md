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
*Paginated list view showing uploaded files across multiple pages.  'api/up/'list/-URl*


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
*Search endpoint filtering uploaded files by tite or description. 'api/v2/search/?q=...URL*









  
