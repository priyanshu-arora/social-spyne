# Low-Level Design for Social Spyne

## Post Service

### Database Schema (PostgreSQL)

```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    content TEXT NOT NULL,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE post_likes (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id),
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(post_id, user_id)
);

CREATE TABLE hashtags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE post_hashtags (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id),
    hashtag_id INTEGER REFERENCES hashtags(id),
    UNIQUE(post_id, hashtag_id)
);
```

### API Endpoints
-   POST /api/posts
-   GET /api/posts/{id}
-   PUT /api/posts/{id}
-   DELETE /api/posts/{id}
-   POST /api/posts/{id}/like
-   GET /api/posts/feed
-   GET /api/posts/hashtag/{hashtag}

### Key Functions

-   create_post(user_id, content, image_url)
-   get_post(post_id)
-   update_post(post_id, content, image_url)
-   delete_post(post_id)
-   like_post(post_id, user_id)
-   get_user_feed(user_id)
-   get_posts_by_hashtag(hashtag)
