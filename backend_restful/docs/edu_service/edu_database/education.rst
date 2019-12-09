==========
Education Service Root 
==========
collection name : education

Attribute Names and description
--------------------------------

_id
    :Description: user id who subscribed 
    :Data Type: string
    :Example: 

associated_institutes
    :Description: This is the list of institutes which the user is associated
    :Data Type: array of **associate_institute** objects
    :Example: 

**associate_institute** object attribute name and description
===================================================
_id
    :Description: The id of the institute 
    :Data Type: string
    :Example: 

title
    :Description: title of the institute
    :Data Type: string
    :Example: 

description
    :Description: short description of the institute
    :Data Type: string
    :Example:
 
designations
    :Description: The designations how the user is associated with the institute such as guardian/stuff/teacher/committee
    :Data Type: a list of **disgnation** object
    :Example: 

**disgnation** object attribut names and description
------------------------------------------
_id
    :Description: an id for the designation
    :Data Type: string
    :Example: 

title
    :Description: title of the designation i. e. Guardian/Office Stuff/Teacher
    :Data Type: string
    :Example: 

join_status
    :Description:  signifies wheather the join request is approved by higher authority
    :Data Type: a list of task object
    :Example: 

join_date
    :Description:  joining date in the system
    :Data Type: datatime
    :Example: 

tags
    :Description:  a list of tags that categorize the tasks logically
    :Data Type: a list of **tag** object
    :Example: 

**tag** object attribute names and description
-------------------------------------------
_id
    :Description: an id for the task
    :Data Type: string
    :Example: 
title
    :Description: title for the tag i. e. Class Management/Child education management
    :Data Type: string
    :Example: 
tasks
    :Description: a list of tasks under this tag
    :Data Type: array of **task** object
    :Example: 

**task** object attribute names and description
-------------------------------------------
_id
    :Description: an id for the task
    :Data Type: string
    :Example: 
title
    :Description: title for the task i. e. Take attendance/Add New Stuff/Check Child Progress
    :Data Type: string
    :Example: 
higher_authority_approval
    :Description: wheather this task required higher authority approval
    :Data Type: string
    :Example: 