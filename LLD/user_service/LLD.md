# Low-Level Design for Social Spyne

## User Service

### Database Schema (PostgreSQL)

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    bio TEXT,
    profile_picture_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_follows (
    id SERIAL PRIMARY KEY,
    follower_id INTEGER REFERENCES users(id),
    followed_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(follower_id, followed_id)
);
```

### API Endpoints
-   POST /api/users/register
-   POST /api/users/login
-   GET /api/users/{id}
-   PUT /api/users/{id}
-   POST /api/users/{id}/follow
-   GET /api/users/{id}/followers
-   GET /api/users/{id}/following

### Key Functions

-   register_user(username, email, password)
-   authenticate_user(email, password)
-   get_user_profile(user_id)
-   update_user_profile(user_id, data)
-   follow_user(follower_id, followed_id)
-   get_user_followers(user_id)
-   get_user_following(user_id)