==========
/service_request
==========

Process system tasks through this api

* **URL**

    /service_request

* **Method:**

    `POST`

*  **URL Params**

    no ulr params

* **Data Params**


**Required:**

    `service_name=[string]`

    `task=[dictionary]`

        `task_id=[string]`
        
        `data=[dictionary]`

* **Success Response:**

    * **status_code:** process_successfull <br />
    * **default_description:** 
    **data:** 

* **Error Response:**

    **status_code:** process_failed 
        **default_description:** 

* **Sample Call:**

    ``
    javascript
    $.ajax({
        url: "/service_request",
        dataType: "json",
        type : "POST",
        contentType: 'application/json',
        data: JSON.stringify( {
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
    ``

* **Notes:**

    It's still under development

.. toctree::
   :maxdepth: 2
   :caption: task_id:

   get_association_list