==========
register
==========

Register a user

* **URL**

/register

* **Method:**

`POST`

* **URL Params**

No Params


* **Data Params**

`email=string`

`password=string`

`name=string`

`phone_no=string`


* **Success Response:**


* **status_code:** registration_successfull <br />
**default_description:** `successfully registered`
**id:** `5d60ce0ee8dc7a242d323337`

* **Error Response:**

* **status_code:** registration_failed <br />
**default_description:** `already registered`
**id:** `5d60ce0ee8dc7a242d323337`

* **Sample Call:**

```javascript
$.ajax({
url: "/register",
dataType: "json",
type : "POST",
contentType: 'application/json',
data: JSON.stringify( { "email": "mhsn06@gmail.com", "password": "1234","name":"hassan", "phone_no":"01737343005" }),
success : function(r) {
console.log(r);
}
});
```

* **Notes:**

It's still under development.