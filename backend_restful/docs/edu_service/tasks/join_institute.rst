==========
join_institute
==========

Join an institute


*  **URL Params**

No url params

* **Data Params**
.. code-block:: JSON

  {
    "task_id" : "join_institute",
    "data" : {
        "institute_id":"//the id of the institute the user want to join, type string",
        "designations":"//the name of the designations user want to associate, type array of string",
    }
  }

* **Success Response:**

When successfully stored associations data in database

* **Code:** 200
* **Content:**
.. code-block:: JSON

  {
    "...":"TODO"
  }

* **Error Response:**

When failed to store associations

* **Code:** 200
* **Content:**
.. code-block:: JSON

  {
    "...":"TODO"
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
    "task":   {
        "task_id" : "join_institute",
        "data" : {
            "institute_id":"5dd6c31cf8c8635f0a449871",
            "designations":["Parent", "Teacher"],
        }
    }
  }),
  success : function(r) {
      console.log(r);
  }
  });

* **Notes:**

No additional notes
