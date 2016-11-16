# FrnT
> /frənt/

## Iteration 02 - Review & Retrospect

* When: November 15, 2016
* Where: In-Person

## Process - Reflection


Decisions turned out well:

* Pair programming
    * We used pair programming at the beginning to jumpstart the development process 
    * It was very useful because it helped get the team on the same page at the beginning of the development cycle, particularly to get up to speed regarding new frameworks and languages that we weren't familiar with
    * This allowed us to split up the tasks and work on our own branches remotely 
* Branches and pull requests 
    * Developing on our individual branches worked out really well, as it allowed us to create new features without interfering with working features 
    * Having another person sign off on the PR ensure that we did not merge changes that would break the working copy

Decisions did not turn out as well as you hoped:

* Data models: 
    * We created data models early on but had to change it afterwards
    * There were attributes that we missed that were important in the search/display feature
    * We should have spent more time planning out our data models at the beginning because changing the models in the middle of the development process turned out to be problematic as it affected existing functionality
* Using Django
    * The framework was too complicated for a small product 
    * Could have used a more lightweight framework instead of trying to get our MVP working with the built-in admin and authentication panel

We are planning to make the following changes to our process:
* UI phase to perform usability testing and collect user feedback 
    * More interaction with users helps ensure that we're building the right product
    * Allows us to adjust our work accordingly and improve the user experience
* More detailed testing phase 
    * Since we're limited on time, our test cases were not very comprehensive and do not handle all the possibilities for error from user input


## Product - Review

We have completed 16/17 [issues](https://github.com/csc301-fall-2016/project-team-01/milestone/2?closed=1) for Iteration 2.


Goals/tasks that were met/completed:
* Landing page
    * Layout and description/value proposition 
* Search for listing
    * Can search for listings based on location and price
* Registration/Sign-in
* Create listing
    * Can create a new listing with description, location, price 
* Edit profile
    * Can update your profile with short biography and location so prospective buyers know more about you
* View profile
    * Can view other user's profiles including their ratings to verify that they are a trustworthy source 
Goals/tasks that were planned but not met/completed:
 
Goals/tasks that were not met/completed:
* Do not have a working rating/review functionality yet 
* Uploading and storing avatars and pictures does not work yet 
* Integration with third party payment provider 
* Having tags with your listing for a more efficient search feature
* Had plans to make a guide for picking up items and releasing updates but didn't implement 

Going into the next iteration, our main insights are:
* Walk through all the interactions with the data models
    * Make sure the models contain all necessary fields, as changing the models later will likely be problematic 
* Assign tasks a priority, such that the ones that have other tasks that depend on it will have a higher priority
    * People with higher priority tasks know they need to complete it earlier to ensure a smooth workflow 