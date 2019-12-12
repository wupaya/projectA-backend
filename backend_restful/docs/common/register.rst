==========
/register
==========

Register a user

* **URL**

/register

* **Method:**

`POST`

* **URL Params**

No Params

* **Data Params**
.. code-block:: JSON

  {
    "email" : "// the registered email address of the user, type: string, required",
    "name" : "// the registered email address of the user, type: string, required",
    "phone_no" : "// the registered email address of the user, type: string, required",
    "password" : "// the corresponding password of the user, type: string, required"
  }

* **Success Response:**
.. code-block:: JSON

  {
    "status_code":"registration_successfull",
    "default_description":"Login Successfull",
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
      "status": "//user_not_found when user not found, use this to show custom message1, type: string",
      "description": "short description, type string"
  }

* **Sample Call:**
.. code-block:: javascript

  $.ajax({
  url: "/login",
  dataType: "json",
  type : "POST",
  contentType: 'application/json',
  data: JSON.stringify({
   "name":"hassan",
   "phone_no":"01737343005",
   "email": "mhsn06@gmail.com",
   "password": "1234"
  }),
  success : function(r) {
    console.log(r);
  }
  });