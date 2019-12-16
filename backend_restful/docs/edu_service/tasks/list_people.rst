==========
list_people
==========

It return a list people such as student/teacher/stuff/alumni/guardians etc


*  **URL Params**

No url params

* **Data Params**
.. code-block:: JSON

  {
    "task_id" : "get_associated_institues",
    "data" : {} //An empty object
  }

* **Success Response:**

Return a list of associated institutes

* **Code:** 200
* **Content:**
.. code-block:: JSON

    {
        "associated": [
            {
                "_id": "//id of the institute",
                "short_name": "//short name of the institute",
                "long_name": "long name of the institute",
                "designations": [
                    {
                        "_id": "//if of the designation",
                        "title": "//title of the designation"
                    }
                ]
            }
        ]
    }

* **Error Response:**

When failed to store associations

* **Code:** 200
* **Content:**
.. code-block:: JSON

  {
    "...":"//click the appropriate task name for the response params"
  }

* **Sample Call:**
.. code-block:: javascript

  $.ajax({
  url: "/service_request",
  dataType: "json",
  type : "POST",
  contentType: 'application/json',
  beforeSend: function (xhr) {
    xhr.setRequestHeader ("Authorization", "Token " + "<your token here>");
  },
  data: JSON.stringify({
    "service_name": "education",
    "task": {
        "task_id": "get_associated_institues",
        "data": {}
    }
  }),
  success : function(r) {
      console.log(r);
  }
  });

* **Notes:**

No additional notes
