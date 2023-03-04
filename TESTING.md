# Locations Testing

[Return to the README.md file](https://github.com/SanZangana/drf-api#readme)

[View live website here!](https://caption-this-react.herokuapp.com/)

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Lighthouse-testing](#lighthouse-testing)
4. [Testing Tools](#testing-tools)
5. [Manual Testing](#manual-testing)
6. [Unit Testing](#unit-testing)


## Testing User Goals

### User Goals

#### As a user I want to be able to view all posts and individual ones.


* If the user wishes to view the posts and access the API endpoint, they may use [this URL](). The specific posts can be accessed easily if the user then enters a valid id after "/posts/", such as 1, 2, 3 etc.

#### As a user I want to be able to view all profiles and individual ones.

* The user has the opportunity to access the API endpoint if they wish to view the accounts. To do that, they may use [this url](). Accessing a specific account is also possible, to do this, please enter a valid id after "/accounts/", such as 1, 2 , 3 etc.

#### As a user I want to be able to view all ratings and individual ones.

* The user can access the API endpoint to view likes through [this URL](). To access a specific like, the user must enter a valid id, such as 1, 2, 3 etc.

#### As a user I want to be able to view all reviews and individual ones.

* The user can access the API endpoint to view comments through [this URL](https://locations-api.herokuapp.com/reviews/). To access a specific review, the user must enter a valid id, such as 1, 2, 3 etc.

#### As a superuser, I want full CRUD functionality in the Django Rest Framework when developing the API.

* The superuser can access the API during development, where they will have full CRUD functionality regarding posts, profiles, ratings and reviews. This requires an account.

## Testing Tools


### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

* Chrome Devtools was used to change css and html syntax and seeing the direct changes, without changing the original code in GitPod. Also used to debug.


### Responsiveness

* Chrome DevTools was being used to test responsiveness across multiple screen sizes. 


## Manual Testing

Testing was done manually as well, to make sure everything worked properly across different browsers, screens and systems.


### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No responsiveness or functionality issues. | Pass |
Safari | No responsiveness or functionality issues. | Pass |
Microsoft Edge | No responsiveness or functionality issues. | Pass |

### System Compatibility

System | Operating System | Outcome | Pass/Fail | 
--- | --- | --- |
PC | Windows 10 | No responsiveness or functionality issues. | Pass |
MacBook Pro M1 | macOS Big Sur version. 11.4 | No responsiveness or functionality issues. | Pass |
iPhone 12 | iOS version 16.1.1 | No responsiveness or functionality issues. | Pass |

### Test Results

#### Home Page

![Home Page](assets/readme/caption-this-api.png)

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
Home page | The user is greeted | Pass |

![All Posts](assets/readme/ct-api-posts.png)

![Posts By ID](assets/readme/ct-api-post-id.png)


#### Posts Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Posts | Users can see all posts created and ordered by id, name and date created | Pass |
Posts by id | Users can see individual posts created and ordered by id, name and date created. | Pass |

![All Profiles](assets/readme/ct-api-accounts.png)

![Profiles By ID](assets/readme/ct-api-accounts-id.png)

#### Profiles Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Profiles | Users can see all profiles created and ordered by id, name and date created | Pass |
Posts by id | Users can see individual profiles created and ordered by id, name and date created. | Pass |

![All Ratings](assets/readme/ct-api-likes.png)

#### Likes Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Ratings | Users can see all ratings created and ordered by id, name and date created | Pass |

![All Reviews](assets/readme/ct-api-comments.png)

![Reviews By ID](assets/readme/ct-api-comments-id.png)

#### Reviews Page

Page | Expected Outcome | Pass/Fail |
--- | --- | --- |
All Reviews | Users can see all reviews created and ordered by id, name and date created | Pass |
Reviews by id | Users can see individual reviews created and ordered by id, name and date created. | Pass |