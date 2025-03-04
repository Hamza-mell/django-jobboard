Job : 
- title - location - job type - description - published at - Vacancy - salary - category - experience

    - apply job 
    - post job

Blog : 
- title - description - created_at - category - tags - author

    - search
    - comment
    - recent posts

contact
home 
login 


  path('accounts/',include('accounts.urls')),
    path('blog/',include('blog.urls')),
    path('contact/',include('contact.urls')),
    path('/',include('home.urls')),
    path('job/',include('job.urls')),