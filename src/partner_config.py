PARTNER_CONFIG = {
    "acme": {
        "delimiter": "|",
        "partner_code": "ACME",
        "column_mapping": {
            "MBI": "external_id",
            "FNAME": "first_name",
            "LNAME": "last_name",
            "DOB": "dob",
            "EMAIL": "email",
            "PHONE": "phone"
        }
    },
    "bettercare": {
        "delimiter": ",",
        "partner_code": "BETTERCARE",
        "column_mapping": {
            "subscriber_id": "external_id",
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "dob",
            "email": "email",
            "phone": "phone"
        }
    }
}
