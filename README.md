# learnship
Int Task simple blog and comments

Login API : http://127.0.0.1:8000/api/v1/login/
    method: post
    body: { username, password }
    response: {token}

Create Article API: http://127.0.0.1:8000/api/v1/articles/
    method: post
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data with slug and comments}

Create Comment API: http://127.0.0.1:8000/api/v1/comments/
    method: post
    auth: bearer **"token"**
    body: { article , text}
    reponse : { data}


GET All Articles API: http://127.0.0.1:8000/api/v1/articles/
    method: GET
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data with slug and comments}

GET All Articles API: http://127.0.0.1:8000/api/v1/articles/<UUID>/
    method: GET
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data with slug and comments}

GET Article by slug: http://127.0.0.1:8000/api/v1/articles/slug/?search=first-title
    method: GET
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data with slug and comments}

**UPDATE and DELETE created user can do changes other users can't change.**

Update Article API: http://127.0.0.1:8000/api/v1/articles/<UUID>/
    method: PUT
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data}


Delete Article API: http://127.0.0.1:8000/api/v1/articles/<UUID>/
    method: DELETE
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data}


Update Article API: http://127.0.0.1:8000/api/v1/comments/<UUID>/
    method: PUT
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data}


Delete Article API: http://127.0.0.1:8000/api/v1/comments/<UUID>/
    method: DELETE
    auth: bearer **"token"**
    body: { title , content}
    reponse : { data}

