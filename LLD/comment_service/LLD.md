# Low-Level Design for Social Spyne

## Comment Service

### Database Schema (PostgreSQL)

```sql
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id),
    user_id INTEGER REFERENCES users(id),
    content TEXT NOT NULL,
    parent_comment_id INTEGER REFERENCES comments(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comment_likes (
    id SERIAL PRIMARY KEY,
    comment_id INTEGER REFERENCES comments(id),
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(comment_id, user_id)
);
```

### API Endpoints
-   POST /api/comments
-   GET /api/comments/{id}
-   PUT /api/comments/{id}
-   DELETE /api/comments/{id}
-   POST /api/comments/{id}/like
-   GET /api/posts/{id}/comments

### Key Functions

-   create_comment(post_id, user_id, content, parent_comment_id)
-   get_comment(comment_id)
-   update_comment(comment_id, content)
-   delete_comment(comment_id)
-   like_comment(comment_id, user_id)
-   get_post_comments(post_id)