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
*Initial API welcome page*


# List  View
![Description of Screenshot](list.png)
*Paginated list view showing uploaded files across multiple pages*

# Delete View
![Description of Screenshot](delete.png)
![Description of Screenshot](delete_after.png)
*Deleting a file from the server using the API. File is removed permanently.*



# Search 
![Search page showing filtered results](search.png)
![Search page showing filtered results](search_word.png)
*Search endpoint filtering uploaded files by tite or description*









  
