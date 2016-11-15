# FrnT
> /frənt/

## Iteration 02

 * Start date: November 7, 2016
 * End date: November 14, 2016

## Process

> (Optional:) Introduction

#### Roles & responsibilities

> Describe the different roles (e.g. developers, communication facilitator,
proof-reader, etc.) on the team, and the responsibilities associated with each role.

> ##### Repo Manager
>
> - Ticket creation
> - Code review
> - Style/lint enforcement
> - Merge of pull requests
> - Builds and CI
>
> ##### Contributor
> - Develop features 
> - De-bugging
> - Unit testing
> - Quality assurance


#### Events
> Please describe the meetings you planning to have:
>  * When and where? In-person or online?
>  * What's the purpose of each meeting?

##### Scrum meetings (in-person): 
- Every Tuesday after tutorial for 30 minutes
- Share what each member has accomplished in the last week, what's blocking them and what they will work on for the coming week


##### Planning meeting (in person, Nov 7):
- Identify what features need to be completed for the MVP
- Delegate tasks and responsibilities among the group
    
##### Review meeting (in person, Nov 14): 
- TBD


#### Artifacts
> Please describe the artifacts that you will produce in order to organize and keep track of your team's progress.
> For example:
>  * To-do lists, burndown chart, schedule, etc.
>  * If you include charts/diagrams, make sure to explain what they represent.
>  * If you're maintaining a to-do list, make sure to mention which tool you're using, how you are prioritizing items and how items get assigned to team members.

## Product
> * Describe your goals for this iteration and the tasks that you will have to complete in order to achieve these goals.
> * When listing goals/tasks, order the items from most to least important.
> * Feel free (but not obligated) to specify some/all tasks as user stories.

#### Goals and tasks:

* Refine the product vision based on iteration 1 feedback:
    - Clarify why renting furniture is desirable compared to owning furniture.
    - Clarify the IRL workflow of furniture transportation/delivery.
    - Consider options to limit seller/buyer liability for damages to items in transaction.
* Create a minimum viable product by implementing the following features:
    - User Registration
        - Post
            - Username
            - First Name
            - Last Name
            - E-mail Address
            - Address
            - Short Biography
    - User Profile
        - Post
            - Edit profile
        - Delete 
            - Profile ID
    - Rate Transaction
        - Post (per transaction)
            - Rater User ID
            - Ratee User ID
            - Rating
    - Listing for furniture
        - Post
            - Title
            - Description
            - Condition
            - Tag
            - Picture
            - Pricing
        - Get
            - Listing ID
            - return: info
        - Delete
            - Listing
        - Edit
            - Edit Posting
    - Search for furniture
        - Get
            - Query Params {$Type, $MinPrice, $MaxPrice, $Style {...}, etc }
            - return: Listing IDs
        
    - Bid for furniture
    - Schedule delivery

* Prepare a demo of the product MVP
    - Write demo script;
    - Produce a video version of the demo.

#### Artifacts
> * Describe the artifacts (diagrams, interactive mock-ups, wireframes, actual code, etc.)
   that you are planning to produce by the end of (and during) this iteration.
>  * Be precise.
>    For example: "Build the website" is not precise at all, but "Build a static home page and upload it somewhere, so that it is publicly accessible" is much clearer.`