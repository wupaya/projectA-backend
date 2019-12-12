==========
/services
==========

Get Available Services or Subscribe Services

* **URL**

/services

* **Method:**

`GET` | `POST`

*  **URL Params**

No Params

* **Data Params**
.. code-block:: JSON

  {
    "id" : "// the registered email address of the user, type: string, required",
    "title" : "// the corresponding password of the user, type: string, required",
    "description" : "// the corresponding password of the user, type: string, required"
  }

* **Success Response:**
  **HTTP Status Code: 200**

  **Response Object:**
.. code-block:: JSON

  {
    "status_code":"page_creation_successfull",
    "default_description":"successfully created page",
    "data": {
      "token": "//session token, type: string",
      "subscribed_services": ["//a list of services subscribed by the user, type: string"
          {
            "service_id" : "//an id in the system for this service, type: string",
            "title": "//A title of the service, type: string",
            "short_updates": "//a short description with lastest update, type: string"
          }
      ],
      "recent_tasks": ["//a list of recents tasks"
          {
            "title": "//title of the task, type: string",
            "link": "//a link for the task, type: string"
          }
      ]
    }
  }


* **Error Response:**

  **HTTP Status Code: 200**
  
  **Response Object:**
.. code-block:: JSON

  {
      "status": "registration_failed //user_not_found when user not found, use this to show custom message1, type: string",
      "description": "already exist, type string"
  }


* **Sample Call:**



* **Notes:**

Required authentication
