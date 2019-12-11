==========
/login
==========

User will provide email and password and get a session token on match

* **URL**

/login

* **Method:**

`POST`

*  **URL Params**

no ulr params

* **Data Params**
.. code-block:: JSON

  {
    "email" : "// the registered email address of the user, type: string, required",
    "password" : "// the corresponding password of the user, type: string, required"
  }

* **Success Responses:**

  **HTTP Status Code: 200**

  **Response Object:**
.. code-block:: JSON

  {
    "status_code":"login_successfull",
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

* **Error Responses:**

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
  data: JSON.stringify( { "email": "mhsn06@gmail.com", "password": "1234" }),
  success : function(r) {
      console.log(r);
  }
  });