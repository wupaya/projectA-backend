==========
Education Public Pages Database
==========
collection name : public_pages

Attribute Names and description
--------------------------------

_id
    :Description: this is id of the page
    :Data Type: string
    :Example: 

page_title
    :Description: title of the page
    :Data Type: string
    :Example: 

type_of_institute
    :Description: type of institute possible values school/college/university/institute/coaching etc 
    :Data Type: string
    :Example: 

creator
    :Description: the id of the user(system admin/public user) who created the page
    :Data Type: string
    :Example: 

varification_status
    :Description: is the verified
    :Data Type: string
    :Example: 

founding_date
    :Description: founded year
    :Data Type: string
    :Example: 

address_district
    :Description: address districts
    :Data Type: string
    :Example: 

address_upozila
    :Description: address upozilla
    :Data Type: string
    :Example: 

no_of_stakeholder
    :Description: total number of people involve now
    :Data Type: string
    :Example: 

description
    :Description: description of the institute
    :Data Type: string
    :Example: 

designations
    :Description: the online services offered by an institute for various stakeholder categorized by designation such as guardian/Stuff/Teacher/Alumnai etc
    :Data Type: array of json designation object mention below
    :Example: 

designation object attribute name and description
===================================================
_id
    :Description: an id for the designation
    :Data Type: string
    :Example: 

title
    :Description: title of the designation such as parent or Teacher/ stuff etc
    :Data Type: string
    :Example: 

tags
    :Description: further categorize tasks logically
    :Data Type: array of tag objects
    :Example: 

tag objects attribut names and description
------------------------------------------
_id
    :Description: an id for the tag
    :Data Type: string
    :Example: 

title
    :Description: title for the tag i. e. Class Mangagement/Stuff Management/Child Education Management etc.
    :Data Type: string
    :Example: 

tasks
    :Description:  a list of task object under this tag/category
    :Data Type: a list of task object
    :Example: 

task object attribute names and description
-------------------------------------------
_id
    :Description: an id for the task
    :Data Type: string
    :Example: 
title
    :Description: title for the task i. e. Take attendance/Add New Stuff/Check Child Progress
    :Data Type: string
    :Example: 