==========
tasks
==========

It return a list of tasks for under a tag


*  **URL Params**

No url params

* **Data Params**
.. code-block:: JSON

  {
    "task_id" : "get_associated_institues",
    "data" : {
        "associated":"//the id of the institute",
        "designation":"//the id of the designation",
        "tag":"//the id of the tag"
    }
  }

* **Success Response:**

* **Code:** 200
* **Content:**
.. code-block:: JSON

  {
    "...":"TODO"
  }

* **Error Response:**


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
        "task_id" : "tasks",
        "data" : {
            "associated":"5ddd62ffd8639286d599dcd6",
            "designation":"5ddd62ffd8639286d599dcd7",
            "tag":"5ddd62ffd8639286d599dcd8"
        }
    }
  }),
  success : function(r) {
      console.log(r);
  }
  });

* **Notes:**

No additional notes
