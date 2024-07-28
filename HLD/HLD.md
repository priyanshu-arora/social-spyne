## HLD Social Spyne

- Client Application:
	-   Web application (React.js)
-  API Gateway / Load Balancer:
   -	AWS Load Balancer
- Microservices:
	-	User Service:
	    -   Manages user accounts, profiles, and relationships
	    -   Handles authentication and authorization
-  Post Service:
    -   Manages creation, retrieval, updating, and deletion of posts
    -   Handles post likes and view counts
-  Comment Service:
    -   Manages comments on posts
    -   Handles comment likes and replies
-  Search Service:
    -   Integrates with Elasticsearch
    -   Provides search functionality for posts, users, and hashtags
-  Notification Service:
    -   Manages and sends notifications to users

- Databases:

	-   User DB: PostgreSQL
	-   Post DB: PostgreSQL
	-   Comment DB: PostgreSQL
	-   Elasticsearch: For efficient searching
	-   Notification DB: MongoDB (Or any noSQL)

- Message Queue:
	-   Since considering we are using AWS so kinesis could be userd for  asynchronous communication between services

- Caching Layer:

	-   Redis for caching frequently accessed data

- File Storage:

	-   Amazon S3 for user-uploaded images
- Logging:
	- AWS Cloudwatch and x-Ray traces