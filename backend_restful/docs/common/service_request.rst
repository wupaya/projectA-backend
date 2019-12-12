==========
/service_request
==========

The tasks in any services is processed by this endpoint.

**!!!!!!! Authentication Required**

* **URL**

/service_request

* **Method:**

`POST`

*  **URL Params**

no ulr params

* **Data Params**
.. code-block:: JSON

  {
    "service_name": "education //it should be always education",
    "task": {
      "task_id": "//One of the id from the Task Index list at the bottom or left of this page.",
      "data": {
        "...":"//The data params for the above task. For data params of a specific tasks click the appropriate task name below in task index"
      }
    }
  }

* **Success Responses:**

  **HTTP Status Code: 200**

  **Response Object:**
.. code-block:: JSON

  {
    "...":"//click the appropriate task name for the response params"
  }

* **Error Responses:**

  **HTTP Status Code: 200**
  
  **Response Object:**
.. code-block:: JSON

  {
      "TODO": ""
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

.. toctree::
   :maxdepth: 2
   :caption: Tasks Index:

   ../edu_service/edu_service_tasks