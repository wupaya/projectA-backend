==========
/public_page
==========

Register and manage public page

* **URL**

/public_page

* **Method:**

`POST`

*  **URL Params**

No Params

* **Data Params**

`page_title=string`
`type_of_institute=string`
`founding_date=string`
`address_district=string`
`address_upozila=string`
`no_of_stakeholder=string`
`description=string`

* **Success Response:**

* **status_code:** page_creation_successfull
* **default_description:** successfully created page
**id:** `5d60d59ff0626c6be06ec94c`

* **Error Response:**

* **status_code:** registration_failed <br />
**default_description:** `already exist`
**id:** `5d5beb87fe6518dd9565243b`

* **Sample Call:**

```javascript
$.ajax({
url: "/public_page",
dataType: "json",
type : "POST",
contentType: 'application/json',
data: JSON.stringify( {
"page_title":"begum rokeya university, rangpur",
"type_of_institute": "university",
"founding_date":"2008",
"address_district":"rangpur",
"address_upozila":"sadar",
"no_of_stakeholder":"20",
"description":"this is a test page"
}),
success : function(r) {
console.log(r);
}
});
```

* **Notes:**

Requires authentication