==========
get_associated_institues
==========

It return a list of associated institutes for the user


*  **URL Params**

No url params

* **Data Params**
.. code-block:: JSON

  {
    "task_id" : "get_associated_institues",
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
    "...":"//click the appropriate task name for the response params"
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
    	"task_id": "tasks",
    	"data": {}	
    }
  }),
  success : function(r) {
      console.log(r);
  }
  });

* **Notes:**

No additional notes
