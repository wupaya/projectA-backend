==========
/login
==========

user will provide email and password and get a session token on match

* **URL**

/login

* **Method:**

`POST`

*  **URL Params**

no ulr params

* **Data Params**

**Required:**

`email=[string]`
`password=[string]`

* **Success Response:**

* **status_code:** login_successfull <br />
* **default_description:** successfully registered <br />
* **data:**
.. code-block:: JSON

  {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiNWQ1YWU0MjExMzYxNGI0ZjcxODU2ZmQ5Iiwic2Vzc2lvbl9pZCI6IjVkNjBiYzE2Zjc1ZjhkZjcxYzQxYmE2YSJ9.ngxcHBHQ9NZQlIT9VKRgUEuGxiyvBl-WRRr7N2sKjYg"
  }

* **Error Response:**

**status_code:** login_failed <br />
    **default_description:** user not found

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

* **Notes:**

It's still under development
